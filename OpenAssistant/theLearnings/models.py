from django.db import models

# Create your models here.


from Home.models import USER

from autoslug import AutoSlugField
from django.template.defaultfilters import slugify



class SkillsOf(models.Model):
        ''' Programming / Database / Advanced / Framework / Cloud / Others '''
        name = models.CharField(max_length=150, default=None, null=True)   
        slug = AutoSlugField(populate_from='name');
        slug_ = AutoSlugField(populate_from='name');

        def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                if not self.slug_:
                        self.slug_ = slugify(self.title)
                super().save(*args, **kwargs)




class Skills(models.Model):

          skillsof = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);








