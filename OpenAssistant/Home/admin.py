from django.contrib import admin
# Register your models here.



# from .models import USER, Checked, Active, Action, Activities
from .models import USER, Actions, Activities, Responces
# from .models import *
from .models import OptionsOf, OptionsGroup, Options


# admin.site.register(USER)
class USERAdmin(admin.ModelAdmin):
    fields = ['FullName', 'FirstName', 'LastName', 'Username', 'Profile', 'Email', 'Mobile', 'Password', 'isChecked', 'isActive' ]
    list_display = [ 'id', 'Username', 'FullName', 'Email', 'Mobile', 'Password', 'isChecked', 'isActive', 'JoiningDate', 'UpdationDate' ] 
admin.site.register(USER, USERAdmin)

'''
class CheckedAdmin(admin.ModelAdmin):
    fields = ['user', 'status', 'datetime' ]
admin.site.register(Checked, CheckedAdmin)

class ActiveAdmin(admin.ModelAdmin):
    fields = ['user', 'status', 'datetime' ]
admin.site.register(Active, ActiveAdmin)
'''


'''
class ActionsAdmin(admin.ModelAdmin):
#     fields = ['name', 'discription', 'datetime' ]
    fields = ['name', 'discription' ]
admin.site.register(Actions, ActionsAdmin)


class ActivitiesAdmin(admin.ModelAdmin):
#     fields = ['user', 'action', 'discription', 'datetime' ]
    fields = ['user', 'action', 'discription' ]
admin.site.register(Activities, ActivitiesAdmin)
'''



@admin.register(Responces)
class ResponcesAdmin(admin.ModelAdmin):
    # list_display = [ 'What', 'Status', 'From', 'Type', 'user', 'Title', 'Content', 'Discription' ] 
    list_display = [ 'User', 'What', 'Status', 'From', 'Type', 'Title', 'Discription' ] 

    def User(self, obj):
        return f"user@{format(obj.user.Username)} ({obj.user.id}) "
    # UserName.admin_order_field  = '_user'  #Allows column order sorting
    User.short_description = 'User (Username)'  #Renames column head

@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
          list_display = [ 'id', 'name', 'datetime' ] 
          # list_display = [ 'id', 'name', 'discription', 'datetime' ] 


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
          list_display = [ 'id', 'Username', 'FullName', 'Action', 'datetime' ] 
          # list_display = [ 'id', 'user', 'action', 'discription', 'datetime' ] 

          def Username(self, obj):
                    return f"@{format(obj.user.Username)} ({obj.user.id}) "
          # UserName.admin_order_field  = '_user'  #Allows column order sorting
          Username.short_description = 'User (Username)'  #Renames column head

          def FullName(self, obj):
                    return f" {format(obj.user.FullName)} "
          # FullName.admin_order_field  = '_user'  #Allows column order sorting
          FullName.short_description = 'User (Full Name)'  #Renames column head

          def Action(self, obj):
                    return f" {format(obj.action.name)} ({obj.action.id})";
          # Action.admin_order_field  = '_user'  #Allows column order sorting
          Action.short_description = 'Action'  #Renames column head






# admin.site.register(OptionsOf)
class OptionsOfAdmin(admin.ModelAdmin):
    fields = ['name' ]
    list_display = [ 'id', 'name' ] 
admin.site.register(OptionsOf, OptionsOfAdmin)


# admin.site.register(OptionsGroup)
class OptionsGroupAdmin(admin.ModelAdmin):
    fields = [ 'name', 'optionsof' ]
    list_display = [ 'id', 'name', 'optionsof' ] 
admin.site.register(OptionsGroup, OptionsGroupAdmin)


# admin.site.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    # fields = [ 'name', 'path', 'logo', 'optionsgroup' ]
    fields = [ 'name', 'path', 'logo', 'optionsof', 'optionsgroup' ]
    list_display = [ 'id', 'name', 'slug', 'slugged', 'path', 'logo', 'optionsof', 'optionsgroup' ]
admin.site.register(Options, OptionsAdmin)








