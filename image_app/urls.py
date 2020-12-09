from django.urls import path
from . import views

app_name = 'image_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('like/', views.like, name='like'),
]
