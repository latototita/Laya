from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.orders import Order
from .models.brand import Brand

from .models.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_posted')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content', 'author')
    list_per_page = 20


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post',
                    'approved_comment', 'created_date')
    list_display_links = ('id', 'author', 'post')
    list_filter = ('author', 'created_date')
    list_editable = ('approved_comment', )
    search_fields = ('author', 'post')
    list_per_page = 20


admin.site.register(Comment, CommentAdmin)


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price','stock', 'category','image','description']


class AdminBrand(admin.ModelAdmin):
    list_display = ['name']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminOrder(admin.ModelAdmin):

    list_display = ['customer','product','price','quantity','address','phone','date','status','ordering_code']





# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Order, AdminOrder )
admin.site.register(Brand,AdminBrand )
