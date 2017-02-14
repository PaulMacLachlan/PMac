from django.conf.urls import url
from . import views
# from django.contrib import admin

def index(request):
    print ("8"*100)
    print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
    print "By the way, here's the request object that Django automatically passes us:", request
    print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
    print ("8"*100)

urlpatterns = [
    url(r'^$', views.index)
]

print "I will be your future routes; HTTP requests will be captured by me."
