from django.contrib import admin
from .models  import Children_law, Mens_law, Women_law, Transgender_law,Commons_law

# Register your models here.
admin.site.site_header="SECURE JUSTICE"

@admin.register(Children_law)
class Children_lawAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")


@admin.register(Mens_law)
class Mens_lawAdmin(admin.ModelAdmin):
     list_display = ("title", "content", "file","website_link","date")

@admin.register(Women_law)
class Women_lawAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")


@admin.register(Transgender_law)
class Transgender_lawAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")

@admin.register(Commons_law)
class Commons_lawAdmin(admin.ModelAdmin):
        list_display = ("title", "content", "file","website_link","date")
    