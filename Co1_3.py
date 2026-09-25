#list comprehensions:
#positive number
numbers=[-5,10,-3,8,0,12,-7,4]
positive=[x for x in numbers if x>0]
print(positive)
#SQUARE OF N NUMBERS
n= 4

squares=[x*x for x in range(1,n+1)]
print("Squares:",squares)
#FROM A LIST OF VOWELS SELECTED FROM A GIVEN WORD 
word= input("Enter a word ")
vowels ={x for x in word if x in"aeiouAEIOU"}
print("Vowels:",vowels)

#list ordinal value of each element of a word
word =input("enter a word: ")
values =[ord(x) for x in word]
print("Ordinal values:",values)
