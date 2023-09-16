from django.contrib import admin
from .models  import ChildrenLR, MensLR, WomenLR, TransgenderLR ,CommonsLR

# Register your models here.
admin.site.site_header="SECURE JUSTICE"

@admin.register(ChildrenLR)
class ChildrenLRAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")


@admin.register(MensLR)
class MensLRAdmin(admin.ModelAdmin):
     list_display = ("title", "content", "file","website_link","date")

@admin.register(WomenLR)
class WomenLRAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")


@admin.register(TransgenderLR )
class TransgenderLRAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "file","website_link","date")

@admin.register(CommonsLR)
class CommonsLRAdmin(admin.ModelAdmin):
        list_display = ("title", "content", "file","website_link","date")
    