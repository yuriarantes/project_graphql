from django.contrib import admin

from .models import Product, Store

class StoreAdmin(admin.ModelAdmin):
    list_display=['id','created_at','name','cnpj','name']
    search_fields=['name','cnpj']
    list_filter = ['created_at','updated_at']
    list_per_page = 20
    ordering = ['-created_at']
    readonly_fields = ['created_at','updated_at','cnpj']
    fieldsets = [
        ('Informações Loja', {'fields': ['name','cnpj']}),
        ('Datas', {'fields': ['created_at', 'updated_at']}),
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        else:
            return ['created_at','updated_at']

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','created_at','name','value','store']
    search_fields=['name','store']
    list_filter = ['created_at','updated_at']
    list_per_page = 20
    ordering = ['-created_at']
    readonly_fields = ['created_at','updated_at','store']
    fieldsets = [
        ('Informações Produto', {'fields': ['name','value','store']}),
        ('Datas', {'fields': ['created_at', 'updated_at']}),
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        else:
            return ['created_at','updated_at']


admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)