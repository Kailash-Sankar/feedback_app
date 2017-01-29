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
	return render( request, 'base/dashboard.html')

@login_required()
def category(request,cid):
	return render( request, 'base/categories.html', {})

@login_required()
def questions(request):
	user = request.user;
	return render( request, 'base/questions.html')

@login_required()
def profile(request):
	return render( request, 'base/user_profile.html')

# ---- API endpoints -----

def question(request,qid):
	print 'question:',qid

	qObj = Question.objects.get(id=qid);
	user = request.user;

	q = {
		'qid'			: qObj.id,
		'summary' 		: qObj.summary,
		'description' 	: qObj.description,
		'user' 			: qObj.user.username,
		'created_date' 	: qObj.created_date,
		'updated_date' 	: qObj.updated_date,
		'likes'			: qObj.likes,
		'myQ'		    : False,
		'myLike'		: None,
	}

	#check if logged in user liked this answer
	try:
   		likeObj = QLike.objects.filter(question=qid,user=user.id).get()
   		mylike = likeObj.like
	except QLike.DoesNotExist:
   		mylike = None
   	except AttributeError:
   		myLike = None

 	q['mylike'] = mylike

	#check if it's logged in user's question
 	if qObj.user.id == user.id:
		q['myQ'] = True

	#get question tags
	q['tags'] = QTags(qid)

	print q;
	return JsonResponse(q,safe=False);


def answers(request,qid,page):
	ansObj = Answer.objects.filter(question=qid);
	user = request.user

	ansList = {};
	for a in ansObj:
		row = buildAnswerRow(a,user);
		ansList[a.id] = row;

	return JsonResponse(ansList,safe=False)


def saveAnswer(request,qid):
	data = json.loads(request.body)
	user = request.user

	aObj = Answer(
		description=data['description'],
		user_id = user.id,
		likes=0,
		question_id=qid,
	);
	aObj.save();

	aRow = buildAnswerRow(aObj,user);

	return JsonResponse(aRow)


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
