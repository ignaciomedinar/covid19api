from django.shortcuts import render
import requests, json

# Create your views here.
def ok(request):
    return render(request,'ok.html')

def home(request):
    args = {}
    #args.update(csrf(request))
    response=requests.get('https://api.covid19api.com/summary')
    args['contents'] = response.json()
    #order_by = request.GET.get('order_by', 'defaultOrderField')
    #Model.objects.all().order_by(order_by)
    return render(request,'getapiinfo/home.html',args)