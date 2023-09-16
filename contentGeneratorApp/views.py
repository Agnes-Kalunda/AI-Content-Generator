from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.contrib.auth.decorators import login_required , user_passes_test 
from .forms import *
from .models import *
from .functions import *


# Create your views here.
def home(request):
    return render (request, 'landing/index.html', {})


def about(request):
    return render(request, 'landing/about.html', {})

   

def anonymous_required(function=None , redirect_url=None):
     if not redirect_url:
        redirect_url = 'dashboard'

        actual_decorator = user_passes_test(
            lambda u:u.is_anonymous,
            login_url=redirect_url
        )

        if function:
            return actual_decorator(function)
        return actual_decorator

@anonymous_required 
def login(request):
    user = None
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password= request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user:
            #login successful
            auth.login(request,user )
            return redirect('dashboard')

        else:
            messages.error(request,'Invalid Credentials, please register first')
            return redirect("register")

    return render(request, 'authorization/login.html', {})

@anonymous_required
def register(request):
    user = None
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2:
            messages.error(request, 'Passwords do not match')

        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with the email address: {} already exists, please use a different email".format(email))

        user = User.objects.create_user(email=email, username=email, password=password1)
        user.save()

        user = user  # Assign new user to user
        auth.login(request, user)
        return redirect('login')
    return render(request, 'authorization/register.html', {})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    context = {}
    return render (request,"dashboard/home.html",context)


@login_required
def profile(request):
    context = {}


    if request.method == 'GET':
        form = ProfileForm(instance=request.user.profile)
        image_form = ProfileImageForm(instance=request.user.profile)
        context['form']= form
        context['image_form']=image_form
        return render (request, 'dashboard/profile.html', context)
    

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        image_form= ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
       
        if form.is_valid():
            form.save()
            return redirect ('profile')
        
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')
          

   
    return render (request, 'dashboard/profile.html', context)



def blogTopic(request):
    context = {}

    if request.method == "POST":
        blogIdea = request.POST['blogIdea']
        request.session['blogIdea']=blogIdea


        keywords = request.POST['keywords']
        request.session['keywords']=keywords


        audience= request.POST['audience']
        request.session['audience']=audience

        blogTopics = generateBlogTopicIdeas(blogIdea, audience, keywords)
        if len(blogTopics) >0:
            request.session['blogTopics'] = blogTopics
            return redirect ('blog-sections')
        
        else:
            messages.error(request,'OOPs, we could not generate blog ideas for yoi, retry')
            return redirect('blog-topic')

    return render(request, 'dashboard/blog-topic.html', context)




def blogSections(request):
     
     if 'blogTopics' in request.session:
         pass
     else:
         messages.error(request, "start by creating blog ideas")
         return redirect('blog-topic')
     
     context = {}
     context['blogTopics'] = request.session['blogTopics']

     return render(request, 'dashboard/blog-sections.html' , context)
     

     


def saveBlogTopic(request, blogTopic):
    if "blogIdea" in request.session and "keywords" in request.session and "audience" in request.session and 'blogTopics' in request.session:
        blog = Blog.objects.create(
        title = blogTopic,
        topic = request.POST['blogIdeas'], 
        keywords = request.POST['keywords'], 
        audience = request.POST['audience'], 
        profile = request.user.profile),
        blog.save()

        blogTopic = request.session['blogTopics']
        blogTopic.remove(blogTopic)
        request.session['blogTopic'] = blogTopic

        return redirect('blog-sections')

    else:
        return redirect('blog-topic')



def useBlogTopic( request, blogTopic):
    context = {}

    if "blogIdea" in request.session and "keywords" in request.session and "audience" in request.session :

        blog = Blog.objects.create(
        title=blogTopic,
        blogIdea=request.session['blogIdea'],
        keywords= request.session['keywords'],
        audience= request.audience['audience'],
        profile= request.user.profile)
        blog.save()
        
        blogSections=generateBlogSectionTitles(blogTopic, request.session['audience'], request.session['keywords'])
        

    else:
        return redirect('blog-topic')
    
    if len(blogSections)>0:

        request.session['blogSections'] = blogSections

        context['blogSections'] = blogSections

    else:
        messages.error(request, "OOpsie doosie, we could not generate any blog fo you. PLease try again")
        return redirect('blog-topic')
    
    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val:
                section = generateBlogSectionDetails(blogTopic, val, request.session['audience'], request.session['keywords'])

                blogSec= BlogSection.objects.create(
                title = val,
                body =section,
                blog=blog)
                blogSec.save()
                
            return redirect('view-generated-blog', slug=blog.slug)
                
    return render(request, 'dashboard/select-blog-sections', context)




def viewGeneratedBlog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except:
        messages.error(request, 'something went wrong')
        return redirect('blog-topic')
    
    blogSections = BlogSection.objects.filter(blog=blog)

    context = {}
    context["blog"]  = blog
    context['blogSections'] = blogSections

    return render (request, 'dashboard/view-generated-blog.html', context)
    