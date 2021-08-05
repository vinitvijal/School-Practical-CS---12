def fun(string, word):
    s = string.split(" ")
    for i in s:
        if (i == word):
            return True
    return False
 
line = input("Enter Your Sentence : ")
word = input("Word to Find : ")
 
if (fun(line, word)):
    print(word," is Present in Your String!!!")
else:
    print(word," is Not Present in Your String!!!")