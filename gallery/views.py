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

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        category_search = Category.objects.filter(name__icontains=searched)
        return render (request, 'search.html', {"searched":searched,
        "category_search":category_search
        } )

    else:
        
        return render (request, 'search.html', {} )

def categories(request):
    category = request.GET.get("category")
    if category is None:
        categ = Picture.objects.order_by("image_name").filter(image_name='image_name')
    else:
        categ = Picture.objects.filter(category = category)
    categ = Category.objects.all()
    context = {"categ":categ}
    return render(request, 'category/category.html', context=context)

# def specifics(request):
#     db_categrys = Category.objects.all()
#     db_pictures = Picture.objects.all()
#     if db_categrys is None:
#         db_categry= request.GET. get(Category)
#         db_pictures = Picture.filter(db_categry = db_categry)

#     context ={"db_categrs":db_categrys,
#             "db_pictures":db_pictures,
#             "db_categry":db_categry
#     }
#     return render(request, ' category/category.html', context=context)
