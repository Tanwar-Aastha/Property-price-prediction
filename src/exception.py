# For Exception Handling purpose.
import sys
from logger import logging

def error_message_detail(error, error_detail:sys):
    '''
    Whenever a error get raised this function will push this on like our own custom message.
    Inputs:
    error: The error message you are getting.
    error_detail: The detail you are getting along with your error.

    Output: You will get your own error message.
    '''
    _,_,exc_tb = error_detail.exc_info()  # tells on which file, line_num exception has occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


# Creating a custom exception class which is inheriting from Exception
class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



