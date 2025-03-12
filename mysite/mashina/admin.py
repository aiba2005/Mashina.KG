from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1



@admin.register(Car)
class CarAdmin(TranslationAdmin):
    inlines = [CarPhotoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Network, Color, Category, Company)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(User)
admin.site.register(Client)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(Cart)
admin.site.register(CartItem)
