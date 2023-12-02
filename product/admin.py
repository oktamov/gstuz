from django.contrib import admin
from .models import Product, ProductImage, AttributeName, AttributeValue


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class AttributeNameInline(admin.TabularInline):
    model = AttributeName
    extra = 1


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, AttributeNameInline]
    list_display = ('title', 'category')
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')
    search_fields = ('product__title',)


admin.site.register(ProductImage, ProductImageAdmin)


class AttributeNameAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]
    list_display = ('name', 'product')
    search_fields = ('name', 'product__title')


admin.site.register(AttributeName, AttributeNameAdmin)


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'image', 'attribute_name')
    search_fields = ('attribute_name__name',)


admin.site.register(AttributeValue, AttributeValueAdmin)
