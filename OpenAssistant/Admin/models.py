from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

from Home.models import USER





class Articals(models.Model):

          USER = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
        #   LinkedSkillsObjects = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);

          title = models.CharField(max_length=150, default=None, null=True) 
          slug = AutoSlugField(populate_from='title');
          discription = models.TextField(default=None, null=True) 

          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 

	  # this function save title's slug automatically...
          def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)



































# class ICONS(models.Model):
#           ''' Font Awesome Icons  '''
#           name = models.CharField(max_length=100, default=None, null=True); 
#           url = models.CharField(max_length=100, default=None, null=True); 
#           size = models.CharField(max_length=100, default=None, null=True); 
#           # class = models.CharField(max_length=100, default=None, null=True); 
#           css = models.CharField(max_length=100, default=None, null=True); 
#           joiningdate = models.DateTimeField(auto_now_add=True);
#           updationdate = models.DateTimeField(auto_now=True); 


# class APP(models.Model):
#         ''' This is apps list '''
#         ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
#         name = models.CharField(max_length=100, default=None, null=True); 
#         url = models.CharField(max_length=50, default=None, null=True); 
#         joiningdate = models.DateTimeField(auto_now_add=True);
#         updationdate = models.DateTimeField(auto_now=True); 


# class HEADING_GROUPS(models.Model):
#           ''' This is all heading groups '''
#           APP = models.ForeignKey(APP, on_delete=models.SET_NULL, null=True, blank=True);
#           ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
#           name = models.CharField(max_length=100, default=None, null=True); 
#           url = models.CharField(max_length=50, default=None, null=True); 
#           joiningdate = models.DateTimeField(auto_now_add=True);
#           updationdate = models.DateTimeField(auto_now=True); 


# class HEADING_NAMES(models.Model):
#           ''' This is all heading names '''
#           APP = models.ForeignKey(APP, on_delete=models.SET_NULL, null=True, blank=True);
#           ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
#           HEADING_GROUPS = models.ForeignKey(HEADING_GROUPS, on_delete=models.SET_NULL, null=True, blank=True);
#           name = models.CharField(max_length=100, default=None, null=True); 
#           url = models.CharField(max_length=50, default=None, null=True); 
#           joiningdate = models.DateTimeField(auto_now_add=True);
#           updationdate = models.DateTimeField(auto_now=True); 




