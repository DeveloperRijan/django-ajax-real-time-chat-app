from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Group, Message
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')


#Send Message
def start_chat(request):
    if request.method != 'POST':
        messages.info(request, "The Method Not Allowed")
        return redirect('index')
    
    #validate input
    errors = False
    errorsMsg = []
    if request.POST['group_name'] == '':
        errors = True
        errorsMsg.append("The group name field is required")
        
    if request.POST['username'] == '':
        errors = True
        errorsMsg.append("The username field is required")
    
    if errors == True:
        messages.info(request, errorsMsg[0])
        return redirect('index')
    

    #after validation pass then
    #Check Group
    group = Group.objects.filter(name=request.POST['group_name']).first()
    if group is None:
        #create new group
        Group.objects.create(name=request.POST['group_name'])

    #create user
    user = User.objects.filter(username=request.POST['username']).first()
    if user is None:
        User.objects.create(username=request.POST['username'])

    return redirect('chats', groupName=request.POST['group_name'], username=request.POST['username'])



def chats(request, groupName, username):
    group = Group.objects.filter(name=groupName).first()
    user = User.objects.filter(username=username).first()
    if group is None or user is None:
        messages.info(request, "The group name or username is invalid")
        return redirect('index')
    
    #if valid username and group then
    return render(request, "chat.html", {'group':group, 'user':user})
        



def send_msg(request):
    pass
    
