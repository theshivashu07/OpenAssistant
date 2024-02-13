from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify




class USER(models.Model):
        # User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True);
        FullName = models.CharField(max_length=50, default=None, null=True); 
        FirstName = models.CharField(max_length=25, default=None, null=True); 
        LastName = models.CharField(max_length=25, default=None, null=True); 
        Username=models.CharField(max_length=30); 
        Mobile = models.IntegerField(default=None, null=True);
        Email = models.EmailField(max_length = 254)
        Password = models.CharField(max_length=50); 
        # Profile = models.ImageField(upload_to='_user/_profiles/', default='_user/_profiles/_default.jpeg', null=True)
        Profile = models.ImageField(upload_to='_user/_profiles/', default=None, null=True)

        # Checked=models.BooleanField(default=None, null=False);
        isChecked = models.BooleanField(default=False, null=True); 
        isActive = models.BooleanField(default=False, null=True);   #isLogin

        JoiningDate = models.DateTimeField(auto_now_add=True);
        UpdationDate = models.DateTimeField(auto_now=True); 
        def __str__(self):
                # 	user@theshivashu ( SHivam SHukla ).
                return f" user@{self.Username}  ( {self.FullName} )."; 

        def __str__(self):
                # 	user@theshivashu ( SHivam SHukla ).
                return f" user@{self.Username} - {self.FullName} );"; 



'''
class Checked(models.Model):
        def user_status(self):
                if self.status:
                        return 'Checked';
                return 'Uncheked'
        user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
        status = models.BooleanField(default=False, null=True); 
        datetime = models.DateTimeField(auto_now_add=True);   
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
'''


class Actions(models.Model):
        name = models.CharField(max_length=50, default=None, null=True);  
        discription = models.TextField(default=None, null=True);  
        datetime = models.DateTimeField(auto_now_add=True); 
        def filter(self):
                temp = ''
                for ch in self.name.lower():
                        if ch!=' ':
                                temp += ch
                return temp 
        def __str__(self):
                # action@signup ( SignUp ).
                return f" action@{self.filter()}  ( {self.name} )."; 

class Activities(models.Model):
        user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);
        action = models.ForeignKey(Actions, on_delete=models.SET_NULL, null=True, blank=True);
        discription = models.TextField(default=None, null=True);  
        datetime = models.DateTimeField(auto_now_add=True);
        def filter(self,string):
                temp = ''
                for ch in string.lower():
                        if ch!=' ':
                                temp += ch
                return temp
        def __str__(self):
                # activities@signup@theshivashu ( SignUp - SHivam SHukla ).
                return f" activities@{self.filter(self.action.name)}@{self.filter(self.user.Username)}  ( {self.action.name} - {self.user.FullName} )."; 


# class Cookies(models.Model):
#         user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True); 
#         status = 

# class AllLogInFromCookies(models.Model):


















