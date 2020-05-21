"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from classroom import views as room
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html') ,name='logout'),
    path('lessons/',room.Lessons, name='subject'),
    path('',room.Lessons, name='subject'),
    path('lessons/chapters/<int:pk>',room.subject, name='detail'),
    path('student/assignment/<int:pk>/', room.solution_assignment, name='sol_ass'),
    path('student/video/<int:pk>', room.Videodetail.as_view(), name='video'),
    path('student/quiz/<int:pk>/', room.take_quiz, name='take_quiz'),
    path('student/quiz/<int:pk>/result', room.result, name='result'),
    path('assignment/',room.Assignments, name='assignment'),
    path('assignments/<int:pk>',room.pdf, name='detail_ass'),
    path('assignment/solution/<int:pk>/', room.solution_assignment_student, name='sol_ass_stu'),
    path('assignment/video/<int:pk>/', room.Video_assdetail.as_view(), name='ass_video'),
    path('assignment/video/seen/<int:pk>/', room.Videocomplete, name='ass_seen'),
    path('assignment/student/quiz/<int:pk>/', room.take_quiz_ass, name='take_quiz_ass'),
    path('assignment/student/quiz/<int:pk>/result', room.result_quiz_ass, name='result_ass'),
 
]
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   