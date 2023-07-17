from django.shortcuts import render
from app.models import Languages,Review
from googletrans import Translator
from .forms import Form
def home(request):
    l = Languages.objects.get(id=1)
    l_all = Languages.objects.all()[::1]
    n=''
    o=''
    t=Translator()
    fm=Form()
    if request.method == 'POST':
            n = str(request.POST.get('input'))
            o = t.translate(n,dest='hi').text
            fm = Form(request.POST)
            if fm.is_valid():
                 t = fm.cleaned_data['user_rewiew']
                 s = Review(rewiew=t)
                 s.save()
                 fm = Form()
            else:
                 fm = Form()
    return render(request,'index.html',{'l':l,'o':l_all,'output':o,'form':fm})

def language(request,id):
      l = Languages.objects.get(pk=id)
      l_all = Languages.objects.all()[::1]
      n=''
      o=''
      fm=Form()
      t=Translator()
      if id == '2':
            if request.method == 'POST':
                n = str(request.POST.get('input'))
                o = t.translate(n,dest='en').text  
      elif id == '3':
            if request.method == 'POST':
                n = str(request.POST.get('input'))
                o = t.translate(n,dest='zh-cn').text
      elif id == '4':
            if request.method == 'POST':
                n = str(request.POST.get('input'))
                o = t.translate(n,dest='es').text
      elif id == '5':
            if request.method == 'POST':
                n = str(request.POST.get('input'))
                o = t.translate(n,dest='ur').text
      else:
           if request.method == 'POST':
            n = str(request.POST.get('input'))
            o = t.translate(n,dest='hi').text
      return render(request,'language.html',{'o':o,'l':l,'ol':l_all,'output':o})