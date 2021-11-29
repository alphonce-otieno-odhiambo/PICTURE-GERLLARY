from django.shortcuts import render,redirect
#from django.http  import HttpResponse
from .models import Category, Picture, Category
from .forms import PictureForm

# Create your views here.
def home(request):
    category = request.GET.get("category")
    if category is None:
        categ = Picture.objects.order_by("image_name").filter(image_name='image_name')
    else:
        categ = Picture.objects.filter(category = category)
    images = Picture.objects.all()
    categ = Category.objects.all()
    context = {
        "images":images,
        "categ":categ
        }
    return render(request, 'home.html', context)

def pictures(request):
    if request.method == "POST":
        form =PictureForm(data= request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render( request,'pictures/pics.html', {"obj": obj})

    else:
        forms = PictureForm()
        picture = Picture.objects.all()
    

    return render(request, 'pictures/pics.html', {"form":forms, "picture":picture})

def formation(request):
    context ={}
    if request.method =="POST":
        image_name =request.POST.get("image_name")
        image_discription = request.POST.get("image_discription")
        object_value = Picture.objects.create(image_name=image_name,image_discription=image_discription )
        context['object'] = object_value 
        context['created'] = True


    return render (request, 'pictures/pics.html', context =context )
