from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request, 'generator/home.html')
	
def password(request):
	character=list('qwertyuiopasdfghjklxcvbnm')	
	if request.GET.get('uppercase'):
		character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
	if request.GET.get('numbers'):
		character.extend(list('1234567890'))
	if request.GET.get('special'):
		character.extend(list('!@#$%^&*'))
	
	length=int(request.GET.get('length', 10))
	thepassword=''
	
	for x in range(length):
		thepassword += random.choice(character)
		
	return render(request, 'generator/password.html',{'password':thepassword})
	
def about(request):
	return render(request, 'generator/about.html')