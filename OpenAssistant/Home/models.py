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
        Email = models.EmailField(max_length = 254); 
        Password = models.CharField(max_length=50); 
        # Profile = models.ImageField(upload_to='_user/_profiles/', default='_user/_profiles/_default.jpeg', null=True) 
        Profile = models.ImageField(upload_to='_user/_profiles/', default=None, null=True) 

        # Checked=models.BooleanField(default=None, null=False); 
        isChecked = models.BooleanField(default=False, null=True); 
        isActive = models.BooleanField(default=False, null=True);   #isLogin

        JoiningDate = models.DateTimeField(auto_now_add=True);
        UpdationDate = models.DateTimeField(auto_now=True); 

        def __str__(self):
                # user@theshivashu ( SHivam SHukla ).
                # return f" user@{self.Username}  ( {self.FullName} )."; 
                # user@theshivashu - SHivam SHukla );
                # return f" user@{self.Username} - {self.FullName} );"; 
                return f" user@{self.Username} - {self.FullName} ({self.id}) );"; 







from model_utils import Choices


class Responces(models.Model):

        WHAT = Choices( 'Report', 'Suggestion', 'Ask' )
        STATUS = Choices( 'Activated', 'Declined', 'Resolved' )
        FROM = Choices( 'Artical', 'Problem', 'Youtube' )
        TYPE = Choices( 'Add Link', 'Missleading Content', 'Verify Content', 'Others' )

        What = models.CharField(choices=WHAT,max_length=25)
        Status = models.CharField(choices=STATUS, default=STATUS.Activated, max_length=25)
        From = models.CharField(choices=FROM, max_length=25) 
        Type = models.CharField(choices=TYPE, default=TYPE.Others, max_length=100) 

        user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True);

        Title = models.CharField(max_length=50, default=None, null=True); 
        Content = models.TextField(default=None, null=True); 
        Discription = models.CharField(max_length=100, default=None, null=True); 







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

        def filter(self,string):
                return "".join( string.lower().split( ' ' ) ) 
        def __str__(self):
                # action@signup ( SignUp ).
                return f" action@{self.filter(self.name)}  ( {self.name} )."; 

class Activities(models.Model):
        user = models.ForeignKey(USER, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);
        action = models.ForeignKey(Actions, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);
        discription = models.TextField(default=None, null=True);  
        datetime = models.DateTimeField(auto_now_add=True); 

        def filter(self,string):
                return "".join( string.lower().split( ' ' ) ) 
        def __str__(self):
                # activities@signup@theshivashu ( SignUp - SHivam SHukla ).
                return f" activities@{self.filter(self.action.name)}@{self.filter(self.user.Username)}  ( {self.action.name} - {self.user.FullName} )."; 


# class Cookies(models.Model):
#         user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True); 
#         status = 

# class AllLogInFromCookies(models.Model):












class OptionsOf(models.Model):
        ''' Articals, Problems, Youtube, Aadhyatm '''
        name = models.CharField(max_length=50, default=None, null=True);  
        def __str__(self):
                return f" optionsof@{self.name} )."; 



class OptionsGroup(models.Model):
        ''' Default, ..... (According to requirements ) ''' 
        name = models.CharField(max_length=50, default=None, null=True);  
        optionsof = models.ForeignKey(OptionsOf, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);

        def __str__(self):
                return f" optionsgroup@{self.name} | {self.optionsof.name} )."; 



class Options(models.Model):
        ''' Default, ..... (According to requirements ) ''' 
        name = models.CharField(max_length=100, default=None, null=True);  
        slug = AutoSlugField(populate_from='name');
        slugged  = AutoSlugField(populate_from='name');
        path = models.CharField(max_length=100, default=None, null=True);  
        logo = models.CharField(max_length=100, default=None, null=True);  
        optionsof = models.ForeignKey(OptionsOf, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);
        optionsgroup = models.ForeignKey(OptionsGroup, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True);

        def __str__(self): 
                return f" options@{self.name} | {self.optionsgroup.name} )."; 

	# this function save title's slug automatically...
        def save(self, *args, **kwargs): 
                self.slug = slugify(self.name) 
                self.slugged = slugify(self.name) 
                # if not self.slugged:
                #         self.slugged = slugify(self.name) 
                super().save(*args, **kwargs) 










