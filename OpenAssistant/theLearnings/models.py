from django.db import models

# Create your models here.


from Home.models import USER




class SkillsOf(models.Model):
        
        name = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);





class Skills(models.Model):

          skillsof = 