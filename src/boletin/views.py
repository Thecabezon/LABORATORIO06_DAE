from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'boletin/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'boletin/detalle_noticia.html', {'noticia': noticia})
