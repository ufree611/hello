from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import contact
from google_play_scraper import app
import requests

# Create your views here.

def index(request):
    # return render(request, 'index.html')
    return HttpResponse("Not A Valid Api")
# def contact(request):
#     titles =[]
#     titlea = []
#     # if request.method == "POST":        
#     #     text2 = request.POST.get('text1')
#     #     text2 = text2.splitlines()
#     #     for x in text2:
#     #         result = app(
#     #             x,
#     #         )
#     #         title = result["title"]
#     #         version= result["version"]

#             # titles.append(version)
#             # titlea.append(version)
#     context = {
#                 "title":titles,
#                 "titles":titlea,
#             }
#     return render(request, 'contact.html', context) 
# #testing

def contact(request):
    return redirect('https://alphaxtools.com/play-version/')


def testing(request):
    if request.method == "GET":
        url = request.GET['url']
        checkurl = "https://play.google.com/store/apps/details?id="+url
        x = requests.get(checkurl)
        v = x.status_code
        if v == 404:
            return HttpResponse(f"<td style='background:red;color:white'>404 Not Found</td><td>-</td>")
        else:       
            result = app(
                url,
            )
            title = result["title"]
            version = result["version"]
            return HttpResponse(f"<td>{title}</td><td>{version}</td>")
    















def about(request):
    x = "hello"
    thhis = ["etc","et","e"]
    for j in thhis:
        print(thhis)
    return HttpResponse("THis is about "+x)