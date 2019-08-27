from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.request_pacient_of_doc, name='request1'),
    path('2', views.request_pacient_of_dep, name='request2'),
   # path('contest/<str:contest_id>/page/<str:page>', views.contest, name='contest'),
]