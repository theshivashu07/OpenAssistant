from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

from Home.models import USER





class Articals(models.Model):

          USER = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
          # LinkedSkillsObjects = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);

          title = models.CharField(max_length=150, default=None, null=True) 
          slug = AutoSlugField(populate_from='title');
          discription = models.TextField(default=None, null=True) 

          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 

	  # this function save title's slug automatically...
          def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)






















