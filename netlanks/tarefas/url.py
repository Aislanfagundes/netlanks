from django.urls.conf import path

from netlanks.tarefas import views

app_name = 'tarefas'

urlpatterns=[
    path('', views.home, name='home')
]