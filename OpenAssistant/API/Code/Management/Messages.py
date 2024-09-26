

from django.contrib import messages



# from API.Views.Management.messages import Messages

class __Messages:

          def __init__(self,request,ReturnObject):

                    try: 
                              if ReturnObject.status=="pass":
                                        messages.success(request, ReturnObject.message ) 

                              elif ReturnObject.status=="fail":
                                        if ReturnObject.showtype=="error": 
                                                  messages.error(request, ReturnObject.message ) 
                                        elif ReturnObject.showtype=="warning": 
                                                  messages.warning(request, ReturnObject.message ) 
                                        elif ReturnObject.showtype=="info": 
                                                  messages.info(request, ReturnObject.message ) 
                                                  
                    except Exception as e:
                                        messages.success(request, "Error coming from Messages.py file. || " + e ) 
                            






















