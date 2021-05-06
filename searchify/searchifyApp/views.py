from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import SnapCreationForm, tagCreationForm, searchForm, findForm, contentSearchForm

from .models import User, Post, Tag


def index(request):
    post_list = Post.objects.all()
    return render(request, "searchifyApp/index.html", {
        'post_list':post_list
    })


def find(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('searchifyApp:login'))
        else:
            form = findForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                return HttpResponseRedirect(reverse('searchifyApp:userlist', kwargs={'username':username}))
            
    return render(request, "searchifyApp/find.html", {
        'form':findForm,
    })

def userlist(request, username):
    userlist = User.objects.filter(username__icontains = username)
    return render(request, "searchifyApp/userlist.html", {
        'form':findForm,
        'userlist':userlist,
        'searchName':username
    })

def profile(request, username):
    try:
        username = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("Profile not found.")
    user_post_list = Post.objects.filter(poster__username=username)

    return render(request, "searchifyApp/profile.html", {
        'post_list':user_post_list,
        'profileName':username,
    })

def result(request, tag):
    tagList=tag.split()
    tagged_posts = Post.objects.filter(tagged_posts__tag__in = tagList)

    return render(request, "searchifyApp/result.html", {
        'post_list':tagged_posts,
        'tag':tag
    }) 

def contentResult(request, content):
    content_posts = Post.objects.filter(content__icontains = content)

    return render(request, "searchifyApp/contentResult.html", {
        'post_list':content_posts,
        'content':content
    })                       

def search(request):
    return render(request, "searchifyApp/search.html", {
    })

def searchTag(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('searchifyApp:login'))
        else:
            form = searchForm(request.POST)
            if form.is_valid():
                tag = form.cleaned_data.get('tag')
                return HttpResponseRedirect(reverse('searchifyApp:result', kwargs={'tag':tag}))
   
    return render(request, "searchifyApp/searchTag.html", {
        'form':searchForm,
    })

def searchContent(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('searchifyApp:login'))
        else:
            form = contentSearchForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data.get('content')
                return HttpResponseRedirect(reverse('searchifyApp:contentResult', kwargs={'content':content}))
   
    return render(request, "searchifyApp/searchContent.html", {
        'form':contentSearchForm,
    })

def create(request):
    if request.method == "POST":
        # Authentication check
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('searchifyApp:login'))
        else: 
            form = SnapCreationForm(request.POST, request.FILES)
            tagForm = tagCreationForm(request.POST)

            if form.is_valid() and tagForm.is_valid():
                tagValues = tagForm.cleaned_data.get('tag')
                form = form.save(commit=False)
                form.poster = request.user
                form.save()
                # Split by whitespace and store in DB
                tagArray = tagValues.split()
                for tagValue in tagArray:
                    # If tag doesn't already exists, then create.
                    newTag = Tag.objects.get_or_create(tag=tagValue)
                    relatedTag = Tag.objects.get(tag=tagValue)
                    form.tagged_posts.add(relatedTag)

                return redirect("/")

    return render(request, 'searchifyApp/create.html', {
        'createform':SnapCreationForm, 
        'tagform': tagCreationForm,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("searchifyApp:index"))
        else:
            return render(request, "searchifyApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "searchifyApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("searchifyApp:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "searchifyApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "searchifyApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("searchifyApp:index"))
    else:
        return render(request, "searchifyApp/register.html")
