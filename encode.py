import string as str

def encode(message:str, shifter:int):
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
    enc_msg = ""
    
    

    for letter in message:
        if letter in lower:
            pos = lower.find(letter)
            new_pos = pos+shifter
            
            if new_pos>25:
                pos_def = new_pos-25
                for i in range(len(lower)-1, -1, -1):
                    [i]=self.cir_arr[i-1]
            else:
                enc_msg = enc_msg + lower[new_pos]
            
    print(enc_msg)
           
            
            
    


encode("ab", 4)