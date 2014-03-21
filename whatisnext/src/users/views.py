#python first
#django second
#our apps
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from django.http import HttpResponse

from django.core.context_processors import csrf

from django.views.decorators.vary import vary_on_headers

from .forms import UserForm
@vary_on_headers('User-Agent')
def home(request): 
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def thankyou(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        subject="thank you for joining"
        message="we are very welcome to join us./n We will be in touch"
        from_email=settings.EMAIL_HOST_USER
        to_list=[save_it.email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=True) 
        
        messages.success(request,'irtibatta olalim')
        return HttpResponseRedirect('/thank-you/')
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

def aboutus(request):   
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))


def signin(request):
    language='tr_TR'
    session_language='tr_TR'
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
    if 'lang' in request.session:
        session_language=request.session['lang']
    return render_to_response("signin.html",{'language':language,'session_language':session_language})

def language(request,language='tr_TR'):
    response=HttpResponse("setting language to %s " % language)
    response.set_cookie('lang',language)
    request.session['lang'] =language
    
    return response

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
def loggedin(request):
    return render_to_response('loggedin.html',{'first_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

