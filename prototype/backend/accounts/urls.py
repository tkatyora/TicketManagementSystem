from django.urls import path
from . import views

urlpatterns = [
    path('',views.signIn, name = 'sign_in'),
    path('',views.signIn, name = 'dashboard'),
    path('activate-user/<uidb64>/<token>',views.activate_user, name='activate'),
    path('regester',views.Regester,name = 'create_account'),
    path('logout',views.signout , name ='logout'),  
    path('users',views.Allusers , name ='users'),  
    path('search/', views.search_users, name='search_users'),
    path('change-role/<int:pk>', views.changeRole,name ='change_role'),
    path('delete-user/<int:pk>', views.deleteUser,name ='delete_user'),

]


