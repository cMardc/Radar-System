from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import serial


"""
class TaskForm(forms.Form):
    task = forms.CharField(label='Task name:')

    


# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, 'index.html', {
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session['tasks'] += [task]
            return HttpResponseRedirect("/todo/")
        else:
            return render(request, 'add.html', {
                'form': form
            })        
    return render(request, 'add.html', {
        'form': TaskForm()
    })

def delete(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task in request.session['tasks']:
                print(request.session['tasks'])
                print(task)
                taskClone = request.session['tasks']
                taskClone.remove(task)
                request.session['tasks'] = taskClone
                print(request.session['tasks'])
                print(task)
                return HttpResponseRedirect("/todo/")
            else:
                return render(request, 'error.html')
                
        else:
            return render(request, 'delete.html', {
                'form': form
            })        
    return render(request, 'delete.html', {
        'form': TaskForm()
    })
"""


class admin_form(forms.Form):
    password = forms.CharField(label='Admin password')

class request_form(forms.Form):
    speed = forms.IntegerField(label='Speed', max_value=165, min_value=1)

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        form = admin_form(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            if password == "__admin__":
                # return render(request, 'admin.html')
                # redirect user to admin.html
                return redirect('__admin__') 
            else:
                # return render(request, 'error.html')
                # redirect user to error.html
                return redirect('error') 
    else:
        return render(request, 'login.html', {
            'form': admin_form()
        })

def __admin__(request):
    if request.method == "POST":
        form = request_form(request.POST)
        if form.is_valid():
            speed = form.cleaned_data["speed"]
            if speed > 0 and speed < 166:
                # send speed variable (as int) to /dev/ttyACM0 (it's an arduino uno)        
                try:
                    # Open a serial connection to /dev/ttyACM0
                    ser = serial.Serial('/dev/ttyACM0', baudrate=9600)  # Adjust baudrate as needed
                    # Send the speed as an integer
                    ser.write(str(speed).encode())
                    # Close the serial connection
                    ser.close()
                except Exception as e:
                    # Handle any serial communication errors
                    print(f"Serial communication error: {e}")

    return render(request, 'admin.html', {
        'form': request_form()  
     })


def error(request):
    return render(request, 'error.html')