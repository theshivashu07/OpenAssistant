

from django.contrib.auth import authenticate as Authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired


from Home.models import *


class SignUp:
	
	# def validate(request, *args,**kwargs):
	def validate(*args,**kwargs):

		# if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
		if ( kwargs.get('email',False) or kwargs.get('mobilenumber',False) ) and kwargs.get('password',False):
			return {
				'status' : 'fail',
				'message' : "Email or Mobile Number and Password is must to entered !!!"
			}
		# if passwords are empty or they not matched, so go back to your 'signup' page !!! 
		if kwargs.password=='' or kwargs.password!=kwargs.passwordagain:
			return {
				'status' : 'fail',
				'message' : "Password are not matched each other !!!"
			}

		# if user already exist, then go back to your 'signup' page again !!! 
		user = USER.objects.filter(Username=kwargs.username)
		if user.exists():
			return {
				'status' : 'fail',
				'message' : "User already exists !!!"
			}
		
                # default returning content, if everything okay !!!
		return{
			'status' : 'pass',
			'message' : "Good to go chief !!!"
		}
        

	def run(*args,**kwargs):

		object = USER()
                
		if kwargs.firstname and kwargs.lastname:
			object.FullName = kwargs.firstname+' '+kwargs.lastname
		elif kwargs.firstname:
			object.FullName = kwargs.firstname
		elif kwargs.lastname:
			object.FullName = kwargs.lastname

		if kwargs.firstname:
			object.FirstName = kwargs.firstname
		if kwargs.lastname:
			object.LastName = kwargs.lastname

		if kwargs.username:
			object.Username = kwargs.username
		if kwargs.mobilenumber:
			object.MobileNumber = kwargs.mobilenumber
		if kwargs.email:
			object.Email = kwargs.email
		if kwargs.password:
			object.Password = kwargs.password
		if kwargs.profile:
			object.Profile = kwargs.profile
                              
		if kwargs.checked:
			object.isChecked = kwargs.checked
		
		object.isActive = False
		object.save()
		return object



class LogIn:
	
	# def validate(request, *args,**kwargs):
	def validate(*args,**kwargs):

		# if user already not exist, then go back to your 'login' page !!! 
		user = USER.objects.filter(Username=kwargs.username)
		if not user.exists():
			return {
				'status' : 'fail',
				'message' : "User not exists !!!"
			}
		user = user[0]  # because we got queryset, because of filter search
		userauth = Authenticate(username=kwargs.username, password=kwargs.password)
                # if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
		if userauth is None:
                        return {
				'status' : 'fail',
				'message' : "Invalid User, username and password not matched !!!"
                        }
		# default returning content, if everything okay !!!
		return {
		        'status' : 'pass',
			'message' : "Invalid User, username and password not matched !!!",
			'object' : userauth,
		}

	def run(*args,**kwargs):
                
                object.Username = None
                object.Email = None
                object.Password = None

                if kwargs.username:
                        object.Username = kwargs.username
                if kwargs.email:
                        object.Email = kwargs.email
                if kwargs.password:
                        object.Password = kwargs.password
                              
                if kwargs.checked:
                        object.isChecked = kwargs.checked
                object.isActive = True

                object.save()
                return object



class LogOut:
	
	def validate(*args,**kwargs):
                
		user = USER.objects.get(id=kwargs.id) 
		if kwargs.user: 
                        pass
        
        def run(*args,**kwargs):
                pass




class dummyUSER(USER):

          def __init__(self):
                    self.FullName = None
                    self.FirstName = None
                    self.LastName = None
                    self.Username = None
                    self.MobileNumber = None
                    self.Email = None
                    self.Password = None
                    self.Profile = None
                    self.isChecked = None
                    self.isActive = None
                    # self.JoiningDate = None
                    # self.UpdationDate = None

          #######################################

          def set_firstname(self,firstname):
                  self.FirstName = firstname
          def set_lastname(self,lastname):
                  self.LastName = lastname
          def set_fullname(self,firstname,lastname):
                  self.FullName = firstname+' '+lastname
          def set_username(self,username):
                  self.Username = username
          def set_mobilenumber(self,mobilenumber):
                  self.MobileNumber = mobilenumber
          def set_email(self,email):
                  self.Email = email
          def set_password(self,password):
                  self.Password = password
          def set_profile(self,profile):
                  self.Profile = profile

          def set_checked(self): 
                  self.isChecked = True 
          def set_unchecked(self): 
                  self.isChecked = False 
          def set_checked_reversed(self,checked): 
                  self.isChecked = not checked 

          def set_active(self):
                  self.isActive = True
          def set_unactive(self):
                  self.isActive = False
          def set_active_reversed(self,active):
                  self.isActive = not active

          #######################################
          
          def get_firstname(self):
                  return self.FirstName
          def get_lastname(self):
                  return self.LastName
          def get_fullname(self):
                  return self.FullName
          def get_username(self):
                  return self.Username
          def get_mobilenumber(self):
                  return self.MobileNumber
          def get_email(self):
                  return self.Email
          def get_password(self):
                  return self.Password
          def get_profile(self):
                 return self.Profile

          def get_checked(self): 
                  return self.isChecked
          def get_active(self):
                  return self.isActive

          #######################################
          
          def set_all(self,*args,**kwargs):

                    if kwargs.firstname and kwargs.lastname:
                              self.FullName = kwargs.firstname+' '+kwargs.lastname
                    elif kwargs.firstname:
                              self.FullName = kwargs.firstname                    
                    elif kwargs.lastname:
                              self.FullName = kwargs.lastname
                              
                    if kwargs.firstname:
                              self.FirstName = kwargs.firstname
                    if kwargs.lastname:
                              self.LastName = kwargs.lastname

                    if kwargs.username:
                              self.Username = kwargs.username
                    if kwargs.mobilenumber:
                              self.MobileNumber = kwargs.mobilenumber
                    if kwargs.email:
                              self.Email = kwargs.email
                    if kwargs.password:
                              self.Password = kwargs.password
                    if kwargs.profile:
                              self.Profile = kwargs.profile
                              
                    if kwargs.checked:
                              self.isChecked = kwargs.checked
                    if kwargs.isActive:
                              self.isActive = kwargs.active

          #######################################
          
          def get_all(self):
                    return {
                            'firstname' : self.FirstName,
                            'lastname' : self.LastName,
                            'fullname' : self.FullName,
                            'username' : self.Username,
                            'mobilenumber' : self.MobileNumber,
                            'email' : self.Email,
                            'password' : self.Password,
                            'profile' : self.Profile,
                            'ischecked' : self.isChecked,
                            'isactive' : self.isActive,
                    }
          
          def print_all(self):
                    values = self.get_all()
                    for key,value in values.items():
                              print( f"{key} : {value}" )


          #######################################
          
          def transfer(self):
                  
                    user = USER()

                    if self.FirstName:
                              user.FirstName = self.FirstName
                    if self.LastName:
                              user.LastName = self.LastName
                    if self.FullName:
                              user.FullName = self.FullName
                    if self.Username:
                              user.Username = self.Username
                    if self.MobileNumber:
                              user.MobileNumber = self.MobileNumber
                    if self.Email:
                              user.Email = self.Email
                    if self.Password:
                              user.Password = self.Password
                    if self.Profile:
                              user.Profile = self.Profile
                              
                    if self.isChecked:
                              user.isChecked = self.isChecked
                    if self.isActive:
                              user.isActive = self.isActive
                    
                    user.save()
                    return user



