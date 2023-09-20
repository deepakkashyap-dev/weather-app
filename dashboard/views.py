from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from datetime import datetime
import os
import requests
import pytz
from .seriaizers import SearchSerializer

ist_timezone = pytz.timezone('Asia/Kolkata')

# deepak-- Deepak@1234
#test ---test@1234

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        api_key = os.getenv("WEATHER_API_KEY")
        city_name = request.POST.get('city_name')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        weather={}
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_time = datetime.now(ist_timezone)
            temperature=  round(data['main']['temp'], 1)
            
            time_in_am_pm_format = current_time.time().strftime("%I:%M %p")
            time_in_format = current_time.strftime('%Y-%m-%dT%H:%M:%S')
            weather={
                'weather' : {
                    'city': data['name'],
                    'temperature': temperature,  
                    'humidity':data['main']['humidity'],
                    'desc': data['weather'][0]['main'],
                    'icon': data['weather'][0]['icon'],
                    'wind':data['wind']['speed'],
                    'timestamp':time_in_format
                }
            }
            serializer = SearchSerializer(data=weather['weather'])
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save(user=request.user)
            weather['weather']['time'] = time_in_am_pm_format
        elif response.status_code == 404:
            weather = {
                'error':city_name
            }
        else:
            weather = {
                'error':"There is some issue "
            }
   
        return render(request,'index.html',weather)

    return render(request,'index.html')


def loginUser(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            print(user, "is user")
            login(request=request,user=user)
            redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logotUser(request):
    logout(request)
    return redirect('/login')