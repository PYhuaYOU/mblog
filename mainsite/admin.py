from django.contrib import admin
from mainsite.models import Post,NewTable,Product,User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class NewAdmin(admin.ModelAdmin):
    list_display = ('text_f','bigint_f', 'char_f', 'date_f', 'datetime_f')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'sku')

admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(NewTable, NewAdmin)
admin.site.register(User)