from django import forms
from .models import APITool

class ToolSelectForm(forms.Form):
    tool = forms.ModelChoiceField(queryset=APITool.objects.all(), empty_label="Selecciona una herramienta")
    query = forms.CharField(max_length=500, label="Ingresa el valor a buscar (IP, email, etc.)")

class APIKeyForm(forms.ModelForm):  # Para admin o usuario autorizado
    class Meta:
        model = APITool
        fields = ['name', '_api_key', 'api_url', 'description']