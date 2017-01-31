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

# ---- API endpoints -----

def saveForm(request,cid):
	data = json.loads(request.body)
	user = request.user

	print 'test',data

	fObj = Feedback(
		rating = data['rating'],
		user_id = user.id,
	);
	#fObj.save();

	tObj = Transport(
		date = data['date'],
		type = data['type'],
		description= data['description'],
		feedback_id = fObj.id,
	);
	#tObj.save();

	ret = {
		'fid' : fObj.id,
		'tid' : tObj.id,
	};

	return JsonResponse(ret)

def questions(request,cid):
	print 'question:',cid

	qObj = Question.objects.filter(category=cid).values();
	print
	user = request.user;
	print "questions",qObj

	q = list(qObj)
	return JsonResponse(q,safe=False);


def answers(request,qid,page):
	ansObj = Answer.objects.filter(question=qid);
	user = request.user

	ansList = {};
	for a in ansObj:
		row = buildAnswerRow(a,user);
		ansList[a.id] = row;

	return JsonResponse(ansList,safe=False)

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
		'likes'			: a.likes,
		'myAns'			: False,
	}

	#check if logged in user liked this answer
	try:
   		likeObj = ALike.objects.filter(answer=a.id,user=user.id).get()
   		mylike = likeObj.like
	except ALike.DoesNotExist:
   		mylike = None
   	except AttributeError:
   		myLike = None

 	row['mylike'] = mylike

 	#check if the logged in user added this answer
	if user.id == a.user.id:
		row['myAns'] = True;

	return row
