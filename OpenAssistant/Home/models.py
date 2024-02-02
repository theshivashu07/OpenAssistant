from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify




class USER(models.Model):
        # User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True);
        FullName = models.CharField(max_length=50, default=None, null=True); 
        FirstName = models.CharField(max_length=25, default=None, null=True); 
        LastName = models.CharField(max_length=25, default=None, null=True); 
        Username=models.CharField(max_length=30, default=None, null=True); 
        MobileNumber = models.IntegerField(default=None, null=True);
        Email = models.EmailField(max_length = 254)
        Password = models.CharField(max_length=50); 
        Profile = models.ImageField(upload_to='user/')

        # Checked=models.BooleanField(default=None, null=False);
        isChecked = models.BooleanField(default=False, null=True); 
        isActive = models.BooleanField(default=False, null=True);   #isLogin

        JoiningDate = models.DateTimeField(auto_now_add=True);
        UpdationDate = models.DateTimeField(auto_now=True);           
        def __str__(self):
                return f" user@{self.Username}  ( {self.FullName} ) ."; 




class Checked(models.Model):
        user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
        status = models.BooleanField(default=False, null=True); 
        datetime = models.DateTimeField(auto_now_add=True);   
        def user_status(self):
                if self.status:
                        return 'Checked';
                return 'Uncheked'
        def __str__(self):
                return f" user@{self.user.Username}  is {self.user_status}."; 

class Active(models.Model):
        def user_status(self):
                if self.status:
                        return 'Active';
                return 'Unactive'
        user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
        status = models.BooleanField(default=False, null=True); 
        datetime = models.DateTimeField(auto_now_add=True);   
        def __str__(self):
                return f" user@{self.user.Username}  is {self.user_status}."; 























