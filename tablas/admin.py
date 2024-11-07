from django.contrib import admin
from .models import Ubicacion
from .models import Tipo
from .models import Estado
from .models import Producto
from .models import Lote

# Register your models here.
admin.site.register(Ubicacion)
admin.site.register(Tipo)
admin.site.register(Estado)
admin.site.register(Producto)
admin.site.register(Lote)