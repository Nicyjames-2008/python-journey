colour = input("Colour of light : ").strip().lower()  # .lower makes the input into lower case
if(colour == "red"):   #here ("") should be used to represent text
        
        print("stop")               #here .strip used to remove space brfore and after input word
elif(colour == "yellow" ):       
        print("look")                 
elif(colour == "green" ):        
        print("you may move")
else :
        print("light broken")
