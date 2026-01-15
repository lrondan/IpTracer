from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib import messages
from .forms import ToolSelectForm
from .utils import search_osint
from .models import OSINTSearch
import json

def panel(request):
    form = ToolSelectForm(request.POST or None)
    results = None
    if request.method == 'POST' and form.is_valid():
        tool = form.cleaned_data['tool']
        query = form.cleaned_data['query']
        try:
            results = search_osint(tool.name, query)
            OSINTSearch.objects.create(tool=tool, query=query, results=results)
            messages.success(request, "Búsqueda completada!")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    
    searches = OSINTSearch.objects.order_by('-searched_at')[:10] # Últimas 10 búsquedas

    pretty_results = None
    if results:
        pretty_results = mark_safe(
            json.dumps(results, indent=4, ensure_ascii=False)
        )
    context = {
        'form': form,
        'results': pretty_results,
        'searches': searches
    }

    
    return render(request, 'panel.html', context)