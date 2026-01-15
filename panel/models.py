from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet
import base64

class APITool(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ej: 'ipinfo', 'hunter'
    _api_key = models.BinaryField(max_length=512, editable=True, blank=True, null=True)  # Encriptada!
    api_url = models.URLField(blank=True)  # Base URL si aplica
    description = models.TextField(blank=True)

    @property
    def api_key(self):
        if not self._api_key:
            return None
        f = self._get_fernet()
        return f.decrypt(self._api_key).decode()

    @api_key.setter
    def api_key(self, value):
        """Encripta y guarda la clave"""
        if not value:
            self._api_key = None
            return
        f = self._get_fernet()
        self._api_key = f.encrypt(value.encode())

    def _get_fernet(self):
        """Crea la instancia Fernet con la clave secreta del proyecto"""
        key = settings.SECRET_KEY[:32]  # Fernet necesita exactamente 32 bytes
        key = base64.urlsafe_b64encode(key.encode().ljust(32)[:32])
        return Fernet(key)
    
    def __str__(self):
        return self.name

class OSINTSearch(models.Model):  # Registro de búsquedas
    tool = models.ForeignKey(APITool, on_delete=models.SET_NULL, null=True)
    query = models.CharField(max_length=500)  # IP, email, teléfono, etc.
    results = models.JSONField(blank=True, null=True)  # Almacena JSON de respuesta
    searched_at = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField(blank=True, null=True)  # Opcional, del middleware
    
    def __str__(self):
        return f"{self.tool} - {self.query} ({self.searched_at:%Y-%m-%d})"