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
    forus=forum.objects.all().order_by('-date_created')
    count=forus.count()
    discussios=[]
    for b in forus:
        discussios.append(b.discussion_set.all())
 
    context={'forus':forus,
              'count':count,
              'discussios':discussios}
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

def detail(request, pk):
    forus=forum.objects.all().order_by('-date_created')
    # discussios=[]
    try:
        # for b in forus:
        #     discussios.append(b.discussion_set.all()) , 'discussios':discussios
        game = forum.objects.get(pk=pk)
        context={'game': game}
    except forum.DoesNotExist:
        raise Http404('Game does not exist')
    
    return render(request, 'app/detail.html', context)

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def faq(request):
    return render(request, 'app/faq.html')

def donate(request):
    return render(request, 'app/donate.html')

def sponsor(request):
    return render(request, 'app/sponsor.html')

def servers(request):
    return render(request, 'app/servers.html')

def sponsors(request):
    return render(request, 'app/sponsors.html')

def affiliate(request):
    return render(request, 'app/affiliate.html')

def dcontact(request):
    return render(request, 'app/dcontact.html')

def collaborate(request):
    return render(request, 'app/collaborate.html')




# EXTRA CODE
# {% for objs in discuss %}
#     {{ objs.discuss }}
#     <br>
#     {% if objs|length > 4 %}
#         <button onclick="myFunction()" id="myBtn">Read more</button>
#     {% endif %}
# {% endfor %}