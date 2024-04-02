from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify




class SkillsOf(models.Model):
        ''' only name give ..... '''
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        discription = models.TextField(default=None, null=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)


class SkillsGroup(models.Model):
        skillsof = models.ForeignKey(SkillsOf, on_delete=models.SET_NULL, null=True, blank=True);
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        discription = models.TextField(default=None, null=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)


class Skills(models.Model):
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)

'''
class BuildSkillSets(models.Model):
        skillsof = models.ForeignKey(SkillsOf, on_delete=models.SET_NULL, null=True, blank=True);
        skillsgroup = models.ForeignKey(SkillsGroup, on_delete=models.SET_NULL, null=True, blank=True);
        skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True, blank=True);
        discription = models.TextField(default=None, null=True); 
        slug = AutoSlugField(populate_from='skills.slug');

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.skills.slug)
                super().save(*args, **kwargs)
'''

class SkillSetsBuild(models.Model):
        skillsof = models.ForeignKey(SkillsOf, on_delete=models.SET_NULL, null=True, blank=True);
        skillsgroup = models.ForeignKey(SkillsGroup, on_delete=models.SET_NULL, null=True, blank=True);
        skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True, blank=True);
        discription = models.TextField(default=None, null=True); 
        slug = AutoSlugField(populate_from='skills.slug');

        def __str__(self): 
                return f"{self.skills.name} | {self.skillsgroup.name} | {self.skillsof.name}" 
        # this function save title's slug automatically... 
        def save(self, *args, **kwargs): 
                self.slug = slugify(self.skills.slug) 
                super().save(*args, **kwargs) 




class SkillsPointers(models.Model):
        skillsetbuild = models.ForeignKey(SkillSetsBuild, on_delete=models.SET_NULL, null=True, blank=True);

        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name'); 
        discription = models.TextField(max_length=150, default=None, null=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)














# class SkillsRelationsType(models.Model):
#         pass

# class SkillsCoordinate(models.Model):
#         skillof = models.ForeignKey(Skills, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);
#         relation_type = models.ForeignKey(SkillsRelationsType, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);











