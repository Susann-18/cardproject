from django.shortcuts import render,redirect
from.models import Bag
from.forms import BagForm



def index(request):
    bag_list = Bag.objects.all()
    return render(request, 'index.html', {'Bages': bag_list})

def create(request):
    if request.method =='POST':
        name=request.POST.get('name')
        image=request.FILES['image']
        color=request.POST.get('color')
        a=Bag(name=name,image=image,color=color)
        a.save()
    return render(request,"create.html")

def delete(request,id):
    if request.method == "POST":
        movie=Bag.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    user=Bag.objects.get(id=id)
    form=BagForm(request.POST or None,request.FILES,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,"bag":user})


# Create your views here.
