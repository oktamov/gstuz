from django.contrib import admin
from .models import Product, ProductImage, AttributeCategory, AttributeValue


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


class AttributeCategoryInline(admin.TabularInline):
    model = AttributeCategory
    # inlines = [AttributeValueInline]  # Nested inline for AttributeValue
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'category')
    search_fields = ('title',)
    list_filter = ('category',)


class AttributeCategoryAdmin(admin.ModelAdmin):

    inlines = [AttributeValueInline]
    list_display = ('name', 'product')


admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImage)
admin.site.register(AttributeCategory, AttributeCategoryAdmin)
# admin.site.register(AttributeValue)
