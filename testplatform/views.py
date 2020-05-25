from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import pika;
import json;


def mainPage(request):
    return render(request, "mainPage.html")

def mq_push(request):
    mq_message={
	"requestId": "8c9c0a2d-3ddf-4a8f-8c0d-7157018f81ff",
	"createTime": "2019-12-06 19:14:16",
	"statusDate": "2019-12-06 19:14:16",
	"loanAppCode": "LA1320191206192449250930008",
	"loanAppStatus": "AUDIT_RESULT_SUCCEEDED"
}




def TestCase(request):
    return render(request,"TestCase.html")
