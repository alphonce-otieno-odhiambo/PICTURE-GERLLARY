from django.shortcuts import render,redirect
#from django.http  import HttpResponse
from .models import Picture
from .forms import PictureForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pictures(request):
    if request.method == "POST":
        form =PictureForm(data= request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'pictures.html', {"obj": obj})

    else:
        form = PictureForm()
        picture = Picture.objects.all()
    

    return render(request, 'pictures/pics.html', {"form":form, "picture":picture})

def formation(request):
    context ={}
    if request.method =="POST":
        image_name =request.POST.get("image_name")
        image_discription = request.POST.get("image_discription")
        object_value = Picture.objects.create(image_name=image_name,image_discription=image_discription )
        context['object'] = object_value 
        context['created'] = True


    return render (request, 'pictures/pics.html', context =context )
