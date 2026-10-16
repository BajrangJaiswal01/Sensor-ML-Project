import sys 
import os 

"""2 -error_details on which line or in which file or what the error for that we have to create a fn"""
def error_message_detail(error,error_detail):
    _,_,exc_tb = error_detail.exc_info() 
    filename = exc_tb.tb_frame.f_code.co_filename 

    error_message = "error occured and the file name is [{0}] and the linenumber is [{1}] and error is [{2}]".format(
    filename,exc_tb.tb_lineno,str(error)) 


    return error_message



"""1 - for getting the error_message and error deatils we have created a class and inherit the exception on it to get 
the error message
"""
class SensorException(Exception): 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) 

        #calling the function 
        self.error_message = error_message_detail(error_message,error_detail=error_detail)


    """error_message will be not in the form of str so, we use dunder methon to convert into string""" 

    def __str__(self): 
        return self.error_message   