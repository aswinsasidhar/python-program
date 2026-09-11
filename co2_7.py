str=input("Enter a string:")
length=len(str)
if length>2:
    if str[-3:]=="ing":
        str+="ly"
    else:
        str+="ing"
    print("new string:",str)
else:
    print("invalid string:",str)
        
        
        