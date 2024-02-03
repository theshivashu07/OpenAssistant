


class dummyUSER(USER):

          def __init__(self):
                  self.FirstName = None 
                  self.LastName = None 
                  self.FullName = None 
                  self. Username = None 
                  # .....

          def set_firstname(self,firstname):
                  self.FirstName = firstname
          def set_lastname(self,lastname):
                  self.LastName = lastname
          def set_fullname(self,firstname,lastname):
                  self.FullName = firstname+' '+lastname
          def set_username(self,username):
                  self.Username = username
          # .....

          def get_firstname(self):
                  return self.FirstName
          def get_lastname(self):
                  return self.LastName
          def get_fullname(self):
                  return self.FullName
          def get_username(self):
                  return self.Username
          # .....


          def all_set(self,*args,**kwargs):
                  if kwargs.firstname:
                          self.get_fullname(kwargs.firstname)
                  if kwargs.lastname:
                          self.set_firstname(kwargs.lastname)
                  .....
          
          def all_get(self):
                    return {
                            'firstname' : self.FirstName,
                            'lastname' : self.LastName,
                            'fullname' : self.FullName,
                            'username' : self.Username,
                            .....
                    }

          def all_print(self):
                    values = self.get_all()
                    for key,value in values.items():
                              print( f"{key} : {value}" )

          def transfer(self):
                    user = USER()
                    if self.FirstName:
                              user.FirstName = self.FirstName
                    if self.LastName:
                              user.LastName = self.LastName
                    .....
                    user.save()
                    return user














