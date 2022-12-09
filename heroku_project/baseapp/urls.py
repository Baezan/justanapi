from django.urls import path
from .views import RegisterView,LoginView, UserView,LogoutView,getuserId,CourseView
# ,, 

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('getID',getuserId ),
    path('course',CourseView.as_view()),
    path('course/<str:pk>',CourseView.as_view())


]