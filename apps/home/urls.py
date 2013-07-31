from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'login/',login,kwargs = {'template_name' : 'home/login.html'}, name = 'wisemoo_login'),
	url(r'logout/', logout,kwargs = {'template_name' : 'home/logout.html'}, name = 'wisemoo_logout'),
	url(r'dashboard/','apps.home.views.dashboard', name = 'wisemoo_dashboard'),
	url(r'register/','apps.home.views.register', name = 'wisemoo_register'),
	#url(r'login/','apps.home.views.login_page', name = 'wisemoo_login'),
)