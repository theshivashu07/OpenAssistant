from django.contrib import admin
# Register your models here.



# from .models import USER, Checked, Active, Action, Activities
from .models import USER, Actions, Activities
# from .models import *



# admin.site.register(USER)
class USERAdmin(admin.ModelAdmin):
    fields = ['FullName', 'FirstName', 'LastName', 'Username', 'Profile', 'Email', 'Mobile', 'Password', 'isChecked', 'isActive' ]
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





