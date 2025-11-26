from django.shortcuts import render
from django.http import HttpResponse

def students(Request):
    student = [{'name':'Dharani','Role':'Software Developer','Address':'Hyderabad'}]
    return HttpResponse(student)
