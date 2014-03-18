from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from django.contrib import messages

from .forms import UserForm

def home(request):
    
    form=UserForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request,'irtibatta olalim')
        return HttpResponseRedirect('/thank-you/')
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def thankyou(request):
    
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

def aboutus(request):
    
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))


