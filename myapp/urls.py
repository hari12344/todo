

from django.contrib import admin
from django.urls import path,include
from .views import home
from myapp.views import Login,Signin,AddToDo,del_todo,change_status,logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("login/",Login.as_view(),name='login'),
    path("signin/",Signin.as_view(),name='signin'),
    path("add-todo/",AddToDo.as_view()),
    path("del_todo/<int:id>",del_todo),
    path("logout/",logout),
    path("change_status/<int:id>/<str:status>",change_status)
]
