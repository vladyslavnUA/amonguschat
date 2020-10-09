from django.shortcuts import render,redirect
from .models import * 
from .forms import *
from among import settings
 
def home(request):
    forums=forum.objects.all().order_by('-date_created')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
    
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'app/index.html', context)

def ind(request):
    forums=forum.objects.all().order_by('-date_created')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'app/home.html', context)
 
def forumm(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, 'app/forum.html', context)
 
def discussionn(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, 'app/discussion.html', context)