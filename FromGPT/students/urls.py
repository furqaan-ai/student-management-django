from django.urls import path
from .views import student_views

urlpatterns = [
    path('',student_views.GoTo,name="GoTo"),
    path('ShowData/',student_views.ShowData,name="show_data"),
    path('Complete/',student_views.ShowComplete,name="show_complete"),
    path('AddData/',student_views.AddData,name="AddData"),
    path('DeleteData/<int:id>/',student_views.DeleteData,name="DeleteData"),
    path('UpdateData/<int:id>/',student_views.UpdateData,name='UpdateData'),
    path('school/<int:id>/',student_views.StudentsBySchool),
    path('ShowSchool/',student_views.StudentsBySchool,name="StudentsBySchool"),

]