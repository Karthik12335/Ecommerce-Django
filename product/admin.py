from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from product.models import (
    Attribute,
    AttributeValue,
    Brand,
    Category,
    Product,
    ProductImage,
    ProductLine,
    ProductType,
)


class EditLinkLine(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )

        if instance.pk:
            link = mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else:
            return ""


class ProductLineInline(EditLinkLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class AttributeInlineValue(admin.TabularInline):
    model = AttributeValue.product_line_attribute_value.through


class AttributeInline(admin.TabularInline):
    model = Attribute.product_type_attribute.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


class ProductImageline(admin.ModelAdmin):
    inlines = [ProductImageInline, AttributeInlineValue]


class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductImageline)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductType, ProductTypeAdmin)
