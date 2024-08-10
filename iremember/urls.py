from django.urls import path, reverse
from myapp.views.home_views import index, info_page
from myapp.views.auth_views import login_view, register_view
from myapp.views.user_views import user_details
from myapp.views.create_post_view import create_post

urlpatterns = [
    #path('', index, name='index'),
    path('info/', info_page, name='info'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('user-details/', user_details, name='user_details'),
    #path('create_post/', create_post, name='create_post'),
    path('', create_post, name='create_post'),
]
