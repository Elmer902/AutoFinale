from django.contrib import admin

from django.contrib import admin
from .models import Messages,BlogPost,License_Category,Drivers_License,detailed_List

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title__startswith']
admin.site.register(BlogPost,BlogAdmin)
class messagefilter(admin.SimpleListFilter):
    title = 'message_status'
    parameter_name = "message_status"
    def lookups(self, request, model_admin):
        return [('r','Read'),('u','Unread')]

    def queryset(self, request, queryset):
        if self.value == 'r':
            return queryset.filter(message_status='r')

        elif self.value == 'u':
            return queryset.filter(message_status = 'u')

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username','email','created_at']
    list_filter = [messagefilter]
# Register your models

admin.site.site_header = "SANCHEZESCULA"
admin.site.site_title = "SANCHEZESCULA Admin"
admin.site.index_title = "BiggerDreams"

class DriverAdmin(admin.ModelAdmin):
    search_fields = ['title__startswith']
    prepopulated_fields = {
        'slug': ['title']
    }
admin.site.register(Drivers_License,DriverAdmin)
admin.site.register(detailed_List)
admin.site.register(License_Category)
