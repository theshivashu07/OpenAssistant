from django.contrib import admin
# Register your models here.

from .models import Articals





# admin.site.register(Articals)
class ArticalsAdmin(admin.ModelAdmin):
    fields = [ 'USER', 'title' ] 
    # fields = [ 'USER', 'title', 'discription'  ] 
    list_display = ['USER', 'title', 'slug', 'discription', 'updationdate' ] 
    # list_display = ['USER', 'title', 'slug', 'discription', 'joiningdate', 'updationdate' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(Articals, ArticalsAdmin)











