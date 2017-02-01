from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from base.models import *
import logging
import json
from django.db.models import F
from django.db.models import Count
from django.contrib.auth.decorators import login_required

#logger instance
logger = logging.getLogger(__name__)

def home(request):
	return render( request, 'base/home.html', {})


def display_meta(request):
    values = request.META.items()
    values.sort()
    return render( request, 'base/utils/meta.html', { 'values' : values })

#---- auth -------

def user_login(request):
	error = "";
	if request.META.get('REQUEST_METHOD') == 'POST':
		u = request.POST.get('username',"");
		p = request.POST.get('password',"");
		#nxt = request.POST.get('next')
		if u and p:
			user = authenticate(username=u, password=p)
			if user is not None:
			    # the password verified for the user
			    if user.is_active:
			        print("User is valid, active and authenticated")
			        login(request, user)
			        return redirect(dashboard)
			        #return HttpResponseRedirect("/dashboard/")
			    else:
			        error = "The password is valid, but the account has been disabled!"
			else:
			    # the authentication system was unable to verify the username and password
			    error = "The username and password were incorrect."
	else:
		error = "Username & Password are mandatory."


	if error != "":
		print 'nothing'
		return redirect(dashboard)
		#return HttpResponseRedirect("/dashboard/")

	return render( request, 'base/home.html', { 'error' : error })


def user_logout(request):
    logout(request)
    return render( request, 'base/home.html', { 'status': 'logout successfull'})
    # Redirect to a success page.


#---- pages ----
@login_required()
def dashboard(request):
 	cats = Category.objects.all();
	return render( request, 'base/dashboard.html', { 'cats' : cats })

@login_required()
def category(request,cid):
	cat = Category.objects.get(id=cid);
	ratings = Rating.objects.all().order_by('id');
	return render( request, 'base/category.html',
		{ 'cat' : cat, 'ratings' :ratings }
	)

@login_required()
def profile(request):
	return render( request, 'base/user_profile.html')

@login_required()
def viewFeedback(request,fid):
	fObj = Feedback.objects.get(id=fid)
	cat = fObj.category

	if cat.id == 1:
		sObj = Transport.objects.get(feedback_id=fObj.id)

		types = { 1 : 'Pickup', 2: 'Drop', 3: 'Pickup & Drop'}
		sObj.type = types[sObj.type]

	aObj = Answer.objects.filter(feedback_id=fObj.id)

	return render( request, 'base/view_feedback.html',
		{ 'f' : fObj, 't' : sObj, 'answers' : aObj, 'cat' : cat }
	)

# ---- API endpoints -----

def saveForm(request,cid):
	data = json.loads(request.body)
	user = request.user

	print 'test',data

	fObj = Feedback(
		rating_id = data['rating'],
		user_id = user.id,
		category_id = cid,
	);
	fObj.save()
	ret = { 'fid' : fObj.id	}

	if cid == '1':
		tObj = Transport(
		date = data['date'],
		type = data['type'],
		description= data['description'],
		feedback_id = fObj.id,
		)
		tObj.save()
		ret['tid'] = tObj.id

	return JsonResponse(ret)

def questions(request,cid):
	print 'question:',cid

	qObj = Question.objects.filter(category=cid).values();
	print
	user = request.user;
	print "questions",qObj

	q = list(qObj)
	return JsonResponse(q,safe=False);


def saveAnswers(request,cid):
	data = json.loads(request.body)
	user = request.user

	fObj = Feedback.objects.get(id=data['fid']);

	aidList = [];
	for q in data['questions']:
		ansObj = Answer(
			description	= q['answer'],
			user_id = user.id,
			question_id = q['id'],
			feedback_id = fObj.id
		)
		ansObj.save()
		aidList.append(ansObj.id)

	return JsonResponse(aidList,safe=False)

def me(request):
	user = request.user

	profile = {
		'username' : user.username,
		'first_name' : user.first_name,
		'last_name' : user.last_name,
		'about' : 'lorem ipsum',
	}
	profile['tags'] = UTags(user.id);

	return JsonResponse(profile,safe=False)

# ---------- local routines -----------

def RecentlyAnsweredQuestions():
	#list( Question.objects.all()[:5].values('summary','likes','id') )
	x = Question.objects.annotate(noa=Count('answer')).order_by('-noa')[:5]	.values()
	print 'QA',x;



#build row for one answer
def buildAnswerRow(a,user):
	row = {
		'aid' 			: a.id,
		'description' 	: a.description,
		'username' 		: a.user.username,
		'uid'			: a.user.id,
		'created_date' 	: a.created_date,
		'updated_date' 	: a.updated_date,
	}

	return row
