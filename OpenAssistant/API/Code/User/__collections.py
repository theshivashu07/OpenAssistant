






class Return:

        def __init__(self,*args,**kwargs):
                #print(args,kwargs)
                self.status = kwargs.get('status',None)             # fail, pass
                self.showtype = kwargs.get('showtype',None)     # success, error, warning, info
                self.message = kwargs.get('message',None)       # "..."
                self.returned = kwargs.get('returned',None)       # object
                #self.print()
        
        def addStatus(self,given):
                self.status = given
        def addShowType(self,given):
                self.showtype = given
        def addMessage(self,given):
                self.message = given
        def addReturned(self,given):
                self.returned = given
        def add(self,*args):
                self.status, self.message, self.returned = args 
        
        def showStatus(self):
                return self.status
        def showShowType(self):
                return self.showtype
        def showMessage(self):
                return self.message
        def showReturned(self):
                return self.returned
        def show(self):
                return {
                        'Status' : self.status,
                        'ShowType' : self.showtype,
                        'Message' : self.message,
                        'Returned' : self.returned
                }
        
        def print(self):
                for key,value in self.show().items():
                        print( f"{key} : {value}" )
                





class DummyUSER:
        
        def __init__(self,*args,**kwargs):
                self.firstname = self.filter(kwargs.get('firstname',None))
                self.lastname = self.filter(kwargs.get('lastname',None))
                self.fullname = self.firstname + ' ' + self.lastname  #(default)
                self.username = self.filter(kwargs.get('username',None))
                self.email = self.filter(kwargs.get('email',None))
                self.mobile = self.filter(kwargs.get('mobilenumber',None))
                self.password = self.filter(kwargs.get('password',None))
                self.passwordagain = self.filter(kwargs.get('passwordagain',None))
                self.profile = self.filter(kwargs.get('profile',None))
                self.checked = self.filter(kwargs.get('checked',None))
                self.active = self.filter(kwargs.get('active',None))
                
                self.request = self.filter(kwargs.get('request',None))
                self.returned = self.filter(kwargs.get('returned',None))


        # if value is blank string or None return None, otherwise return original string...
        def filter(self,value):
                if value:
                        return value
                return None


        # this method resolve our value from dictionary to assignment...
        def submit(self,values):
                self.firstname = self.filter(values.get('firstname',None))
                self.lastname = self.filter(values.get('lastname',None))
                self.fullname = self.firstname + ' ' + self.lastname  #(default)
                self.username = self.filter(values.get('username',None))
                self.email = self.filter(values.get('email',None))
                self.mobile = self.filter(values.get('mobilenumber',None))
                self.password = self.filter(values.get('password',None))
                self.passwordagain = self.filter(values.get('passwordagain',None))
                self.profile = self.filter(values.get('profile',None))
                self.checked = self.filter(values.get('checked',None))
                self.active = self.filter(values.get('active',None))

                self.request = values.get('request')
                self.returned = self.filter(values.get('returned',None))


        def show(self):
                return {
                        'Full Name' : self.fullname,
                        'First Name' : self.firstname,
                        'Last Name' : self.lastname,
                        'Username' : self.username,
                        'Email' : self.email,
                        'Mobile' : self.mobile,
                        'Password' : self.password,
                        'Password Again' : self.passwordagain,
                        'Profile' : self.profile,
                        'Checked' : self.checked,
                        'Active' : self.active,
                        'Request' : self.request,
                        'Returned' : self.returned
                }
        
        def print(self):
                for key,value in self.show().items():
                        print( f"{key} : {value}" )
                

        


# def SignUp(*args,**kwargs):
class SignUp:

        def __init__(self,dummyobject):
                #dummyobject = DummyUSER()
                object = self.__checks(dummyobject)
                if object.status=='pass':
                        object = self.__run(kwargs)
                self.filter = object
                #return object 

        def __checks(self,kwargs):

            # if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
            if not checks1( kwargs.get('email',None), kwargs.get('mobilenumber',None), kwargs.get('password',None) ):
                return Return(
                    status = 'fail',
                    showtype = 'warning', # success, error, warning, info
                    message = "Email or Mobile Number and Password is must to entered !!!",
                )
            # if passwords are empty or they not matched, so go back to your 'signup' page !!! 
            if not checks2( kwargs.get('password',None), kwargs.get('passwordagain',None) ):
                return Return(
                    status = 'fail',
                    showtype = 'warning', # success, error, warning, info
                    message = "Password are not matched each other !!!"
                )
            # if user already exist, then go back to your 'signup' page again !!!
            if checks3( kwargs.get('username',None) ):
                return Return(
                    status = 'fail',
                    showtype = 'info', # success, error, warning, info
                    message = "User already exists !!!"
                )

            # default returning content, if everything okay !!!
            return Return(
                status = 'pass',
                showtype = 'success', # success, error, warning, info
                message = "Good to go chief !!!"
            )



        def __run(self,kwargs):
                
                try:
                        object = USER()
                        
                        if kwargs['firstname'] and kwargs['lastname']:
                                object.FullName = kwargs.firstname+' '+kwargs['lastname']
                        elif kwargs['firstname']:
                                object.FullName = kwargs['firstname']
                        elif kwargs['lastname']:
                                object.FullName = kwargs['lastname']

                        if kwargs['firstname']:
                                object.FirstName = kwargs['firstname']
                        if kwargs['lastname']:
                                object.LastName = kwargs['lastname']

                        if kwargs['username']:
                                object.Username = kwargs['username']
                        if kwargs['mobilenumber']:
                                object.MobileNumber = kwargs['mobilenumber']
                        if kwargs['email']:
                                object.Email = kwargs['email']
                        if kwargs['password']:
                                object.Password = kwargs['password']
                        if kwargs['profile']:
                                object.Profile = kwargs['profile']
                                
                        if kwargs['checked']:
                                object.isChecked = kwargs['checked']
                        
                        object.isActive = False
                        object.save()
                        
                        # Also submit data to Activity model...
                        activityObject = Activities(
                                user = object,
                                action = Actions.objects.get(pk=1) 
                        )
                        
                        return Return(
                            status = 'pass',
                            showtype = 'success', # success, error, warning, info
                            message = "User SignUp Successfully !!!",
                            returned = object,
                        )
                
                except:
                        return Return(
                            status = 'fail',
                            showtype = 'error', # success, error, warning, info
                            message = "This error coming from insertion data to model !!!"
                        )







def checks1(email,mobilenumber,password):
    if email and password:
        return True
    elif mobilenumber and password:
        return True
    #else : and now return for any conditions...
    return False

def checks2(password,passwordagain):
    if password in [ '', None ]:
        return False
    elif password==passwordagain:
        return True
    #else : and now return for any conditions...
    return False

def checks3(username):
    user = USER.objects.filter(Username=username )
    if user.exists():
        return True
    #else : and now return for any conditions...
    return False






'''
returned = checks1( 'theshivashu@gmail.com', '7898565074', '12345' )      # ----- > True
print(returned)
returned = checks1( None, '7898565074', '12345' )                                       # ----- > True
print(returned)
returned = checks1( 'theshivashu@gmail.com', None, '12345' )                # ----- > True
print(returned)
returned = checks1( 'theshivashu@gmail.com', '7898565074', None )      # ----- > False
print(returned)
returned = checks1( None, None, '12345' )                                                 # ----- > False
print(returned)
returned = checks1( None, '7898565074', None )                                       # ----- > False
print(returned)
returned = checks1( 'theshivashu@gmail.com', None, None )               # ----- > False
print(returned)
'''

'''
returned = checks2( '', '' )                          # ----- > False
print(returned)
returned = checks2( '', '12345' )               # ----- > False
print(returned)
returned = checks2( '12345', '' )                 # ----- > False
print(returned)
returned = checks2( '123', '12345' )            # ----- > False
print(returned)
returned = checks2( '12345', '1' )                # ----- > False
print(returned)
returned = checks2( '12345', '12345' )       # ----- > True
print(returned)

returned = checks2( None, None )       # ----- > False
print(returned)

returned = checks3('theshivashu')
print(returned)

'''


class request:
        def __init__(self):
                self.POST = {
                        'firstname' : "SHivam",
                        'lastname' : "SHukla",
                        'username' : "theshivashu",
                        'email' : "theshivashu@gmail.com",
                        'mobile' : '7898565074',
                        'password' : "12345",
                        'passwordagain' : "12345",
                        'checked' : True,
                }
        def insert(self):
                self.POST['firstname'] = input("Enter given First Name : ")
                self.POST['lastname'] = input("Enter given Last Name : ")
                self.POST['fullname'] = self.POST['firstname'] + ' ' + self.POST['lastname']
                print(f"Enter given First Name : {self.POST['fullname']} (default)")
                self.POST['username'] = input("Enter given Username : ")
                self.POST['email'] = input("Enter given Email : ")
                self.POST['mobile'] = input("Enter given Mobile : ")
                self.POST['password'] = input("Enter given Password : ")
                self.POST['passwordagain'] = input("Enter given Password Again : ")
                
                self.POST['checked'] = input("Enter given Checked ( 0 for False, 1 or else for True ) : ")
                self.POST['checked'] = ( False if self.POST['checked']=='0' else True )

        def print(self):
                for key,value in self.POST.items():
                        print(f">> {key} : {value} ")


request = request()
request.print()
#request.insert()
#request.print()

object = SignUp(
        firstname = request.POST.get('firstname',None),
        lastname = request.POST.get('lastname',None),
        username = request.POST.get('username',None),
        email = request.POST.get('email',None),
        mobile = request.POST.get('mobile',None),
        password = request.POST.get('password',None),
        passwordagain = request.POST.get('passwordagain',None),
        # profile = request.POST.get('profile',None),
        checked = request.POST.get('checked',None),
        # active = request.POST.get('active',None),
)

object

#ReturnedObject = SignUp( dummyobject )

#print(ReturnedObject)
#print(ReturnedObject.filter.print())



