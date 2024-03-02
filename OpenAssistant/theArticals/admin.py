from django.contrib import admin
# Register your models here.

from .models import Articals
from .models import ContentFrom, ContentOf, RunningNewArticals





# admin.site.register(Articals)
class ArticalsAdmin(admin.ModelAdmin):
    fields = [ 'USER', 'title' ] 
    # fields = [ 'USER', 'title', 'discription'  ] 
    list_display = ['USER', 'title', 'slug', 'discription', 'updationdate' ] 
    # list_display = ['USER', 'title', 'slug', 'discription', 'joiningdate', 'updationdate' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(Articals, ArticalsAdmin)



# admin.site.register(ContentFrom)
class ContentFromAdmin(admin.ModelAdmin):
    fields = [ 'names' ] 
    list_display = ['id', 'names' ]
    def __str__(self):
        return f"{self.name}" 
admin.site.register(ContentFrom, ContentFromAdmin)


# admin.site.register(ContentOf)
class ContentOfAdmin(admin.ModelAdmin):
    fields = [ 'froms', 'names', 'locations' ] 
    list_display = ['id', 'froms', 'names', 'locations' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(ContentOf, ContentOfAdmin)


# admin.site.register(RunningNewArticals)
class RunningNewArticalsAdmin(admin.ModelAdmin):
    fields = [ 'USER', 'content' ] 
    list_display = ['id', 'USER', 'content' ] 
    def __str__(self):
        return f"{self.content}" 
admin.site.register(RunningNewArticals, RunningNewArticalsAdmin)






