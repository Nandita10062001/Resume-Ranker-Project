import textract
import re

def get_content_as_string(filename):
    text = textract.process(filename)
    lower_case_string =  str(text.decode('utf-16')).lower()
    #final_string = re.sub('[^a-zA-Z0-9 \n]', '', lower_case_string)
    return lower_case_string