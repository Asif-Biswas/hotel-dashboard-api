from django.contrib import admin
from . models import Location, Feature, Season, Category, CategoryTag
# Register your models here.
class SeasonInline(admin.TabularInline):
    model = Season
    extra = 2

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 5

class CustomLocation(admin.ModelAdmin):
    list_display = [
        'l_name',
        'tags',
    ]
    inlines = [SeasonInline]

class CustomSeasonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        's_name',
        'location',
    ]
    inlines = [FeatureInline]

class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sf_title',
        'season',
    ]

class CustomTagInline(admin.TabularInline):
    model = CategoryTag
    extra = 4

class CustomCategory(admin.ModelAdmin):
    list_display = [
        'c_name'
    ]
    inlines = [CustomTagInline]

admin.site.register(Location, CustomLocation)
admin.site.register(Feature, CustomFeatureAdmin)
admin.site.register(Season, CustomSeasonAdmin)
admin.site.register(Category, CustomCategory)