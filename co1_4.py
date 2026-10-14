text=input("enter a line:")
words=text.split()
for word in set(words):
    print(word,":",words.count(word))
