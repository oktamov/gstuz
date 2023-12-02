from django.contrib import admin
from .models import Category, Document, Form


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'type')
    search_fields = ('title', 'type')
    list_filter = ('type',)


admin.site.register(Document, DocumentAdmin)


class FormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'organization', 'phone_number', 'email', 'desc')
    search_fields = ('full_name', 'organization', 'phone_number', 'email')


admin.site.register(Form, FormAdmin)

from django.contrib import admin
from .models import Region, District, Address, Company


class DistrictInline(admin.TabularInline):
    model = District
    extra = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class RegionAdmin(admin.ModelAdmin):
    inlines = [DistrictInline]
    list_display = ('name',)


admin.site.register(Region, RegionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name',)
    list_filter = ('region',)


admin.site.register(District, DistrictAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'district', 'lat', 'lng')
    search_fields = ('address1', 'district__name')
    list_filter = ('district',)


admin.site.register(Address, AddressAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


admin.site.register(Company, CompanyAdmin)
