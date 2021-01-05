from django.shortcuts import render
import requests, json
# from .filters import OrderFilter

# Create your views here.
def ok(request):
    return render(request,'ok.html')

def home(request):
    args = {}
    response=requests.get('https://api.covid19api.com/summary')
    args['contents'] = response.json()

    # query = request.GET.get('query')
    # api_key = locu_api
    # url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    # locality = query.replace(' ', '%20')
    # final_url = url + "&locality=" + locality + "&category=restaurant"
    # json_obj = urllib2.urlopen(final_url)
    # data = json.load(json_obj)

    return render(request,'getapiinfo/home.html',args)