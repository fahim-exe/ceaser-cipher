import encode as Enc
import decode as Dec




while True:
    #take input and shifter numeber
    print("Type 'encode' to encrypt, type 'decode' to decrypt the message.")
    choice = input("Enter your choice: ")

    if choice.lower()=="encode":
        message = input("Enter your message: ")
        shifter = int(input("Enter shifter amount: "))
        
        #print teh encoded/decoded message
        print(Enc.encode(message=message, shifter=shifter))
        
        close_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
        print()
        if close_input.lower() == "no":
            break

    if choice.lower() == "decode":
        message = input("Enter your message: ")
        shifter = int(input("Enter shifter amount: "))

        print(Dec.decode(message=message, shifter=shifter))
        close_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
        print()
        if close_input.lower() == "no":
            break

    else:
        q = input("Please enter a valid input or enter 'q' to exit the program!!!!")
        print()

        if q.lower()=="q":
            break
            

        

        










