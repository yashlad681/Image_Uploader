from calendar import c
from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Image



def home(request):
    # import ipdb;ipdb.set_trace()
    img= ''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    img = Image.objects.all()
    form = ImageForm()
    return render(request, 'myapp\home.html', {'form': form,'img':img})

# def home(request):
#     import ipdb;ipdb.set_trace()
#     img= ''
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
            
#             # return redirect('home')
#     img = Image.objects.all()
#     # form = ImageForm()
#     return render(request, 'myapp\home.html', {'form': form,'img':img})    


