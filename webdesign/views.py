from django.shortcuts import render
from django.http import HttpResponse



def home_page(request):
	return render(request,'front_page_RFAPL.html')
	

def about_page(request):
	return render(request,'about_us.html')
	
def home1(request):
	return render(request,'front_page_RFAPL.html')	