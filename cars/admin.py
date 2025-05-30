from django.contrib import admin
from cars.models import Car, Brand

# Aqui, registramos nossos modelos

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model','brand',)

admin.site.register(Brand, BrandAdmin) #primeiro a classe/tabela e depois a configuração de admin desse modelo
admin.site.register(Car, CarAdmin)

