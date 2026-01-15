import requests
from django.conf import settings
import sherlock
from .models import APITool
import datetime

def get_api_key(tool_name):
    try:
        tool = APITool.objects.get(name=tool_name)
        return tool.api_key
    except APITool.DoesNotExist:
        return None

def search_osint(tool_name, query):
    key = get_api_key(tool_name)
    if not key and tool_name not in ['whois', 'sherlock']:  # Algunos no necesitan key
        raise ValueError(f"Clave API requerida para {tool_name}")
    
    if tool_name == 'ipinfo':
        url = f"https://ipinfo.io/{query}/json?token={key}"
        return requests.get(url).json()
    
    elif tool_name == 'hunter':
        url = f"https://api.hunter.io/v2/email-verifier?email={query}&api_key={key}"
        return requests.get(url).json()
    
    elif tool_name == 'numverify':
        url = f"http://apilayer.net/api/validate?access_key={key}&number={query}"
        return requests.get(url).json()
    
    elif tool_name == 'whois':
        import whois
        data = whois.whois(query)  # Para dominios

        result_dict = data.__dict__

        for key, value in data.items():
            if isinstance(value,list) and value and isinstance(value[0], datetime.datetime):
                data[key] = value[0].isoformat()
            elif isinstance(value, datetime.datetime):
                result_dict[key] = value.isoformat()

        return result_dict

    elif tool_name == 'sherlock':
        from sherlock import sherlock  # Instala sherlock-project
        results = sherlock(query)  # Búsqueda username en redes
        return {site: data for site, data in results.items() if data['exists']}
    
    # Agrega más herramientas aquí...
    else:
        raise ValueError("Herramienta no soportada")