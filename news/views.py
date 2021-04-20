from django.shortcuts import render
from django.http import HttpResponse
from .models import Story

# Create your views here.
def index(request):
	latest_story_list = Story.objects.order_by('-pub_date')[:10]
	#for story in latest_story_list:
		
	output = ', \n '.join([s.__str__() for s in latest_story_list])
	return HttpResponse(output)