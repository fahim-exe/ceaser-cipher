import string as str

def encode(message:str, shifter:int):
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
   
    enc_msg = ""
    
    

    for letter in message:
        if letter in lower:
            pos = lower.index(letter)
            new_pos = pos+shifter
            
            if new_pos>25:
                new_pos = int((int((new_pos+pos)/2)//1)+1)-25
                if new_pos<0:
                    new_pos = abs(new_pos)-1

                enc_msg = enc_msg + lower[new_pos]
                
            else:
                
                enc_msg = enc_msg + lower[new_pos]


        if letter in upper:
            pos = upper.index(letter)
            new_pos = pos+shifter
            
            if new_pos>25:
                new_pos = int((((new_pos+pos)/25)//1)+1)-26
                
                enc_msg = enc_msg + upper[new_pos]
                
            else:
                
                enc_msg = enc_msg + upper[new_pos]
            
    return enc_msg
           
            
            
    


