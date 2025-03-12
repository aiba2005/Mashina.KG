from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Network)
class NetworkTranslationOptions(TranslationOptions):
    fields = ('network_name', 'title',)


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('company_name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Color)
class LessonTranslationOptions(TranslationOptions):
    fields = ('color_name',)
