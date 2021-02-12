from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.views import View
from catalog.models import Category,Image
import cloudinary.uploader


class CatalogView(View):
    view_name='catalogue'
    template=f'{view_name}.html'
    def get(self, request, *args, **kwargs):
        cate_filter=request.GET.get('category')
        if cate_filter is None:
            images=Image.objects.all()
        else:
            cate=get_object_or_404(Category,label=cate_filter)
            images=Image.objects.filter(category=cate)
        context={
            'images':images,
            'categories':Category.objects.all()
        }
        return render(request, self.template,context)
        
class CreateimageView(View):
    view_name='create_image'
    template=f'{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'categories':Category.objects.all()})
        

    def post(self, request, *args, **kwargs):
        title=request.POST.get('title')
        description=request.POST.get('description')
        category=request.POST.get('category')
        image=request.FILES['image']
        print(request.POST)
        if(title =='' or description =='' or category ==''):

            return redirect('createimage')

        try:
            print("HHHHHH")
            response=cloudinary.uploader.upload(image)
            cate=get_object_or_404(Category,label=category)
            url=response['secure_url']
            print(url)
            Image.objects.create(image=url,title=title,description=description,category=cate)
        except:
            return redirect('createimage')

        return redirect('catalog')
