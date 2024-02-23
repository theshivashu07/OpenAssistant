from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify





class ICONS(models.Model):
          ''' Font Awesome Icons  '''
          name = models.CharField(max_length=100, default=None, null=True); 
          url = models.CharField(max_length=100, default=None, null=True); 
          size = models.CharField(max_length=100, default=None, null=True); 
          # class = models.CharField(max_length=100, default=None, null=True); 
          css = models.CharField(max_length=100, default=None, null=True); 
          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 


class APP(models.Model):
        ''' This is apps list '''
        ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
        name = models.CharField(max_length=100, default=None, null=True); 
        url = models.CharField(max_length=50, default=None, null=True); 
        joiningdate = models.DateTimeField(auto_now_add=True);
        updationdate = models.DateTimeField(auto_now=True); 


class HEADING_GROUPS(models.Model):
          ''' This is all heading groups '''
          APP = models.ForeignKey(APP, on_delete=models.SET_NULL, null=True, blank=True);
          ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
          name = models.CharField(max_length=100, default=None, null=True); 
          url = models.CharField(max_length=50, default=None, null=True); 
          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 


class HEADING_NAMES(models.Model):
          ''' This is all heading names '''
          APP = models.ForeignKey(APP, on_delete=models.SET_NULL, null=True, blank=True);
          ICONS = models.ForeignKey(ICONS, on_delete=models.SET_NULL, null=True, blank=True);
          HEADING_GROUPS = models.ForeignKey(HEADING_GROUPS, on_delete=models.SET_NULL, null=True, blank=True);
          name = models.CharField(max_length=100, default=None, null=True); 
          url = models.CharField(max_length=50, default=None, null=True); 
          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 








