from django.urls import re_path
import managoose.views

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'managoose.views.home', name='home'),
    # re_path(r'^blog/', include('blog.re_paths')),



	re_path(r'^$', managoose.views.home),
	re_path(r'^search/$', managoose.views.search), 

]
