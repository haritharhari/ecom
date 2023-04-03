from django.urls import path
from .import views

urlpatterns =[
    path("AddProduct",views.AddProduct,name="AddProduct"),
    path("ProductViewMerchant",views.ProductViewMerchant,name="ProductViewMerchant"),
    path("DeleteProduct/<int:pk>",views.DeleteProduct,name="DeleteProduct"),
    path("UpdateProduct/<int:pk>",views.UpdateProduct,name="UpdateProduct"),
    path("ViewProduct/<int:pk>",views.ViewProduct,name="ViewProduct"),
   



    
]