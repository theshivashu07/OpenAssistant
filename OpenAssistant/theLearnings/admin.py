from django.contrib import admin
# Register your models here.

from .models import SkillOf, Skill, ProgrammingLanguages, TopicHeadings, TopicSubHeadings, Topic
# from .models import SkillsOf, SkillsGroup, Skills, BuildSkillSets, SkillSetsBuild




# admin.site.register(SkillsOf)
class SkillOfAdmin(admin.ModelAdmin):
    fields = [ 'name' ] 
#     fields = [ 'name', 'discription' ] 
    list_display = ['id', 'name', 'slug', 'slugs' ] 
    def __str__(self): 
        return f"{self.name}" 
admin.site.register(SkillOf, SkillOfAdmin) 


# admin.site.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    fields = [ 'skillsof', 'name' ] 
    list_display = [ 'id', 'skillsof', 'name', 'slug', 'slugs' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(Skill, SkillAdmin)







# admin.site.register(Skills)
class TopicHeadingsAdmin(admin.ModelAdmin):
    fields = [ 'skill', 'name' ] 
    list_display = [ 'id', 'skill', 'name', 'slug', 'slugs' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(TopicHeadings, TopicHeadingsAdmin)


# admin.site.register(Skills)
class TopicSubHeadingsAdmin(admin.ModelAdmin):
    fields = [ 'skill', 'headings', 'name' ] 
    list_display = [ 'id', 'skill', 'headings', 'name', 'slug', 'slugs' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(TopicSubHeadings, TopicSubHeadingsAdmin)


# admin.site.register(Skills)
class TopicAdmin(admin.ModelAdmin):
    fields = [ 'USER', 'skill', 'headings', 'subheadings', 'title', 'content', 'discription' ] 
    list_display = [ 'id', 'USER', 'skill', 'headings', 'subheadings', 'title', 'slug', 'slugs', 'updationdate' ] 
    def __str__(self): 
        return f"{self.name}" 
admin.site.register(Topic, TopicAdmin) 












# admin.site.register(Skills)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    fields = [ 'skillsof', 'name', 'extensions' ] 
    list_display = [ 'id', 'skillsof', 'name', 'slugs', 'extensions' ] 
    def __str__(self):
        return f"{self.name}" 
admin.site.register(ProgrammingLanguages, ProgrammingLanguagesAdmin)










