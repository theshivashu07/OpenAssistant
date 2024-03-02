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

      #     MainTags = models.JSONField(default=dict(),null=True,blank=True)
      #     OtherTags = models.JSONField(default=dict(),null=True,blank=True)

          joiningdate = models.DateTimeField(auto_now_add=True);
          updationdate = models.DateTimeField(auto_now=True); 

	  # this function save title's slug automatically...
          def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)




class ContentFrom(models.Model):
        ''' tag / feature ''' 
        names = models.CharField(max_length=50, default=None, null=True) 
        def __str__(self):
                return f"{self.names.lower()}s"

class ContentOf(models.Model):
        ''' h1/h2/h3/h4/h5/h6/p/span/a/...(tags)  --or-- div/table/...(feature) ''' 
        froms = models.ForeignKey(ContentFrom, on_delete=models.SET_NULL, null=True, blank=True);
        names = models.CharField(max_length=50, default=None, null=True) 
        locations = models.CharField(max_length=100, default=None, null=True) 
        def __str__(self):
                return f"{self.names.lower()}s | {self.froms}"



class RunningNewArticals(models.Model):
          USER = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
          content = models.JSONField(default=dict,null=True,blank=True)








