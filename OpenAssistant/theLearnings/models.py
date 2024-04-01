from django.db import models

# Create your models here.


from Home.models import USER




class SkillsOf(models.Model):
        " Programming / Database / Advanced / Framework / Cloud / Others "
        name = models.CharField(max_length=150, default=None, null=True)   





class Skills(models.Model):

          skillsof = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);








