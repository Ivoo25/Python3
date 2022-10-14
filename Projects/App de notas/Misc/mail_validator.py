import re
class regex_mail_validator():
    def check(self, mail):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if(re.search(regex,mail)):  
            return True
        else:  
            return False   