from django.contrib import admin
from .models import Room, Category, RoomImage, Property
# Register your models here.


admin.site.register(Property)
admin.site.register(RoomImage)


class ImageInline(admin.TabularInline):
    model = RoomImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'visible']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ImageInline
    ]