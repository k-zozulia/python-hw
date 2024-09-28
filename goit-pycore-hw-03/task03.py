import re

def normalize_phone(phone_number):
    res = "+"
    phone_number = re.sub(r'\D', '', phone_number)
    
    if not phone_number.startswith('38'):
        res += '38'
        
    res += phone_number

    return res
