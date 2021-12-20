from App.models import Brand, Category, ImageLibrary, Product, ProductDetails, ProductTest, UsedFor
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(ProductDetails)
admin.site.register(Brand)
admin.site.register(ProductTest)
admin.site.register(UsedFor)


class ImageLibraryAdmin(admin.StackedInline):
    model = ImageLibrary


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageLibraryAdmin]

    class Meta:
        model = Product


@admin.register(ImageLibrary)
class ImageLibraryAdmin(admin.ModelAdmin):
    pass
