from django.urls import path
from blog import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('logout/',views.user_logout,name='logout'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.user_login,name='login'),
   path('addpost/',views.add_post,name='addpost'),
   path('update/<int:id>/',views.update_post,name='updatepost'),
   path('delete/<int:id>/',views.delete_post,name='deletepost'),
]
