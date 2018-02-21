from django.conf.urls import url

from . import views

app_name="accounts"

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),

    
    url(r'profile/create_profile/$', views.create_profile, 
    	name='create_profile'),
    url(r'profile/edit_profile/$', views.edit_profile, 
    	name='edit_profile'),
    url(r'profile/$', views.profile, 
    	name='profile'),
    url(r'bio/$', views.bio, name='bio'),
    url(r'change_password/$', views.change_password, 
    	name='change_password'),
] 