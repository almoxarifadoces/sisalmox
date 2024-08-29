from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Material

def inicio(request):
    return render(request, 'core/inicio.html', {})

def lista_material(request):
    materiais = Material.objects.filter(created__lte=timezone.now()).order_by('name') 
    return render(request, 'core/materiais.html', {'materiais': materiais})
    
def lista_pesquisa(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(description__icontains=query) | Q(codigo__icontains=query)
            results= Material.objects.filter(lookups).distinct()
            context={'results': results,'submitbutton': submitbutton}
            return render(request, 'core/pesquisa.html', context)
        else:
            return render(request, 'core/pesquisa.html')
    else:
        return render(request, 'core/pesquisa.html')