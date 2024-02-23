from django.contrib import admin
# Register your models here.



from .models import ICONS, APP, HEADING_GROUPS, HEADING_NAMES




# admin.site.register(ICONS)
class ICONSAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'size', 'css' ]
    list_display = ['name', 'url', 'size', 'css', 'joiningdate', 'updationdate' ]
    def __str__(self):
        return f"{self.name}"
admin.site.register(ICONS, ICONSAdmin)


# admin.site.register(APP)
class APPAdmin(admin.ModelAdmin):
    fields = [ 'name', 'url', 'ICONS' ]
    list_display = [ 'name', 'url', 'ICONS', 'joiningdate', 'updationdate' ]
    def __str__(self):
        return f"{self.name}"
admin.site.register(APP, APPAdmin)


# admin.site.register(HEADING_GROUPS)
class HeadingGroupsAdmin(admin.ModelAdmin):
    fields = [ 'name', 'url', 'APP', 'ICONS' ]
    list_display = [ 'name', 'url', 'APP', 'ICONS', 'joiningdate', 'updationdate' ]
    def __str__(self):
        return f"{self.name}"
admin.site.register(HEADING_GROUPS, HeadingGroupsAdmin)


# admin.site.register(HEADING_NAMES)
class HeadingNamesAdmin(admin.ModelAdmin):
    fields = [ 'name', 'url', 'APP', 'ICONS', 'HEADING_GROUPS' ]
    list_display = [ 'name', 'url', 'APP', 'ICONS', 'HEADING_GROUPS', 'joiningdate', 'updationdate' ]
    def __str__(self):
        return f"{self.name}"
admin.site.register(HEADING_NAMES, HeadingNamesAdmin)



















