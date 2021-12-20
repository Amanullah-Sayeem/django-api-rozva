from django.urls import path

from App.views import Brnad_CRUD, UserFor_CRUD, Category_CRUD, Product_CRUD, productByBrand, productByCategory, productByUsedFor
urlpatterns = [
    path("brand", Brnad_CRUD.as_view(), name=""),
    path("category", Category_CRUD.as_view(), name=""),
    path('usedfor', UserFor_CRUD.as_view(), name=""),
    path("product", Product_CRUD.as_view(), name=""),
    path("brand/category/usedfor/<id>", productByUsedFor, name=""),

    # path('product/usedfor/<id>', productByUsedFor, name=""),
    path('product/brand/<id>', productByBrand, name=""),
    path('product/category/<id>', productByCategory, name="")


]
