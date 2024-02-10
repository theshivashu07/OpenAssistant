

from django.contrib import messages



from API.Views.Management.messages import Messages

class Messages:

          def __init__(self,request,ReturnObject):

                    try: 
                              if ReturnObject.status=="pass":
                                        messages.success(request, ReturnObject.showtype ) 

                              elif ReturnObject.status=="fail":
                                        if ReturnObject.showtype=="error": 
                                                  messages.error(request, ReturnObject.showtype ) 
                                        elif ReturnObject.showtype=="warning": 
                                                  messages.warning(request, ReturnObject.showtype ) 
                                        elif ReturnObject.showtype=="info": 
                                                  messages.info(request, ReturnObject.showtype ) 
                                                  
                    except Exception as e:
                                        messages.success(request, "Error coming from Messages.py file. || " + e ) 
                            






















