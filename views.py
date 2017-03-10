from django.shortcuts import render
from django.shortcuts import HttpResponse
import time
import urllib
from subprocess import *
# Create your views here.

def handle_request(request):
	f = open('myfile.mzn','w',0)
	f.write(urllib.unquote(request.GET['code']))
	print urllib.unquote(request.GET['code'])
	f.close
	time.sleep(10)
	test = check_output(["minizinc","myfile.mzn"])
	response = request.GET['callback'] + '({"test" : "' + urllib.quote(test) + '"})'
	return HttpResponse(response)
