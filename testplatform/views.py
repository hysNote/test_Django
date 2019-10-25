from django.shortcuts import render
from django.http import HttpResponse
import pika;
import json;

def mainPage(request):
    return render(request, "mainPage.html")

def mq_push(request):
    mq_message=request.POST.get('mq_message','')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.29.64.110', port=5672, virtual_host='/',
                                                                   credentials=pika.PlainCredentials('bkjkmq',
                                                                                                     'bkjkmq123456')))
    channel = connection.channel()
    channel.queue_declare(queue='q_fund_cf_lending_remit_notify_test', durable=True)
    # body为想要传入的mq消息
    body = mq_message
    channel.basic_publish(exchange='', routing_key='q_fund_cf_lending_remit_notify_test', body=body)
    connection.close()
    return HttpResponse('push success')