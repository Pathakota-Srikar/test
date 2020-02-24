from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import College
from .forms import CollegeForm

def viewcollege(request):
    col=College.objects.all()
    return render(request,'myapp/view.html',{'col':col})

def createcollege(request):
    if request.method=='POST':
        form=CollegeForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            form.save()
            # return HttpResponse('college Created',name)
            return redirect('view')
    form=CollegeForm()
    return render(request,'myapp/create.html',{'form':form})

def updatecollege(request,id):
    col=College.objects.get(id=id)
    if request.method=='POST':
        form=CollegeForm(request.POST,instance=col)
        if form.is_valid():
            form.save()
            # return HttpResponse('college updated')
            return redirect('view')
    form=CollegeForm()
    return render(request,'myapp/update.html',{'form':form})

def deletecollege(request,id):
    col=College.objects.get(id=id)
    col.delete()
    return HttpResponse('college Deleted')


