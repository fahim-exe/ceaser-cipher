import string as str

def decode(message:str, shifter:int):
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
   
    dec_msg = ""
    
    

    for letter in message:
        if letter in lower:
            pos = lower.index(letter)
            new_pos = pos-shifter


            
            
            if new_pos>25:
                new_pos = int((int((new_pos-pos)/2)//1)+1)+25
                if new_pos<0:
                    new_pos = abs(new_pos)-1

                dec_msg = dec_msg + lower[new_pos]
                
            else:
                dec_msg = dec_msg + lower[new_pos]

    return dec_msg
