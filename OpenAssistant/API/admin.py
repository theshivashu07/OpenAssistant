from django.contrib import admin
# Register your models here.

from .models import SkillsOf, SkillsGroup, Skills, SkillSetsBuild, SkillsPointers
# from .models import SkillsOf, SkillsGroup, Skills, BuildSkillSets, SkillSetsBuild




# admin.site.register(SkillsOf)
class SkillsOfAdmin(admin.ModelAdmin):
    fields = [ 'name' ] 
#     fields = [ 'name', 'discription' ] 
    list_display = ['id', 'name', 'slug', 'discription' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(SkillsOf, SkillsOfAdmin)


# admin.site.register(SkillsGroup)
class SkillsGroupAdmin(admin.ModelAdmin):
    fields = [ 'name', 'skillsof' ] 
    list_display = ['id', 'name', 'slug', 'skillsof' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(SkillsGroup, SkillsGroupAdmin)


# admin.site.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    fields = [ 'name' ] 
#     fields = [ 'name', 'discription' ] 
    list_display = ['id', 'name', 'slug' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(Skills, SkillsAdmin)

'''
# admin.site.register(BuildSkillSets)
class BuildSkillSetsAdmin(admin.ModelAdmin):
    fields = [ 'name', 'skillsof', 'skillsgroup', 'skills' ] 
    list_display = ['id', 'skillsof', 'skillsgroup', 'skills', 'slug' ] 
    def __str__(self):
        return f"{self.skills} | {self.skillsgroup} | {self.skillsof}" 
admin.site.register(BuildSkillSets, BuildSkillSetsAdmin)
'''


# admin.site.register(SkillSetsBuild)
class SkillSetsBuildAdmin(admin.ModelAdmin):
    fields = [ 'skillsof', 'skillsgroup', 'skills' ] 
    list_display = ['id', 'skillsof', 'skillsgroup', 'skills', 'slug' ] 
    def __str__(self):
        return f"{self.skills} | {self.skillsgroup} | {self.skillsof}" 
admin.site.register(SkillSetsBuild, SkillSetsBuildAdmin)


# admin.site.register(SkillsPointers)
class SkillsPointersAdmin(admin.ModelAdmin):
    fields = [ 'skillsetbuild', 'name', 'discription' ] 
    list_display = ['id', 'skillsetbuild', 'name', 'discription', 'slug' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(SkillsPointers, SkillsPointersAdmin)








