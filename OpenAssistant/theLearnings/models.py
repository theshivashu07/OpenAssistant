
from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

from Home.models import USER
from ckeditor_uploader.fields import RichTextUploadingField





class SkillOf(models.Model):
        ''' Programming Languages, Frameworks, Database, Cloud, Advanced, Others '''
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        slugs = models.TextField(default=None, null=True, blank=True); 
        discription = models.TextField(default=None, null=True, blank=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                self.slugs = self.slug
                super().save(*args, **kwargs)



class Skill(models.Model):
        skillsof = models.ForeignKey(SkillOf, on_delete=models.SET_NULL, null=True, blank=True);

        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        slugs = models.TextField(default=None, null=True, blank=True); 
        
        status = models.BooleanField(default=True, null=True, blank=True); 
        image = models.TextField(max_length=150, default=None, null=True, blank=True); 

        tags = models.TextField(default=None, null=True, blank=True); 
        discription = models.TextField(default=None, null=True, blank=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                self.slugs = self.slug
                super().save(*args, **kwargs)




class TopicHeadings(models.Model):
        skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True);
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        slugs = models.TextField(default=None, null=True, blank=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                self.slugs = self.slug
                super().save(*args, **kwargs) 




class TopicSubHeadings(models.Model):
        
        skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True);
        headings = models.ForeignKey(TopicHeadings, on_delete=models.SET_NULL, null=True, blank=True);

        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        slugs = models.TextField(default=None, null=True, blank=True); 

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                self.slugs = self.slug
                super().save(*args, **kwargs) 





class Topic(models.Model):
        
        USER = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);

        skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True);
        headings = models.ForeignKey(TopicHeadings, on_delete=models.SET_NULL, null=True, blank=True);
        subheadings = models.ForeignKey(TopicSubHeadings, on_delete=models.SET_NULL, null=True, blank=True);
        
        title = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='title');
        slugs = models.TextField(default=None, null=True, blank=True); 
        
        content = RichTextUploadingField() 
        discription = models.TextField(default=None, null=True, blank=True) 
        
        joiningdate = models.DateTimeField(auto_now_add=True);
        updationdate = models.DateTimeField(auto_now=True); 

        def __str__(self):
                return f"{self.title}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                self.slugs = self.slug
                super().save(*args, **kwargs) 











class ProgrammingLanguages(models.Model):
        skillsof = models.ForeignKey(SkillOf, on_delete=models.SET_NULL, default=None, null=True, blank=True);
        name = models.CharField(max_length=50, default=None, null=True); 
        slug = AutoSlugField(populate_from='name');
        slugs = models.TextField(default=None, null=True, blank=True); 
        tags = models.TextField(default=None, null=True, blank=True); 
        extensions = models.CharField(max_length=10, default=None, null=True, blank=True); 
        discription = models.TextField(default=None, null=True, blank=True);  

        def __str__(self):
                return f"{self.name}"
        # this function save title's slug automatically...
        def save(self, *args, **kwargs):
                self.skillsof = SkillOf.objects.filter( slug="programming=languages" )[0]
                self.slug = slugify(self.name)
                self.slugs = self.slug
                super().save(*args, **kwargs)




# help.theshivashu@gmail.com 
# work.theshivashu@gmail.com 
# social.theshivashu@gmail.com 
# trials.theshivashu@gmail.com 
# secure.theshivashu@gmail.com 
# resume.theshivashu@gmail.com 
