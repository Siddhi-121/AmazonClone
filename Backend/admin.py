from django.contrib import admin
from amazon_backend_api.models import (
    Amazonuser,
    UserAddress,
    Brand,
    Category,
    Subcategory,
    Size,
    Product,
    ProductDetail,
    Color,
    Cart,
)

admin.site.register(Amazonuser)
admin.site.register(UserAddress)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Color)
admin.site.register(Cart)
