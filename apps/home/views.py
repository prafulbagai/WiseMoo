from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect,render
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout,login,authenticate
from apps.home.forms import *
from apps.data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

@cache_page(900)
@login_required
def dashboard(request):

	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.owner=request.user
			newdoc.save()

    		return redirect('/dashboard/')

	else:
		form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    
	images = Document.objects.filter(owner=request.user)
	paginator = Paginator(images,50)

	page = request.GET.get('page')
	try:
		documents = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		documents = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		documents = paginator.page(paginator.num_pages)

	return render_to_response('home/dashboard.html',{'documents': documents, 'form': form},
    							context_instance=RequestContext(request))


def register(request):
	form = RegisterForm(request.POST or None)
	
	if(form.is_valid()):
		user = form.save()
		user.backend = settings.AUTHENTICATION_BACKENDS[0]
		login(request,user)
		return redirect('/dashboard/')

	ctx = {
			'form' : form
	}

	return render_to_response('home/register.html',ctx, context_instance = RequestContext(request))