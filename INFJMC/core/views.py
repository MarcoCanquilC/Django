from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    titulo = "hola a todos"

    data = {
        
        "mensaje": titulo
    }

    return render(request,'index.html',data)


def carreras(request):

    titulo="carreritas"

    carreras=("ingenieria a", "ingeniria b", "ingenieria c", "ingeniria d")

    data={

         "carreras":carreras,
         "titulo":titulo, 
    }

    return render(request, "carreras.html", data)


def profesores(request):

    titulo="profes"

    profesores=("juan", "mauro", "agusto", "enael")

    data={

        "profesores":profesores,
        "titulo":titulo, 
    }


    return render(request, "profesores.html",data )