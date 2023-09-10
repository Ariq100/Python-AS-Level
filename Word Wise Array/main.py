str1 = "This is Physics Class !!! "
ch = ""
arr = []

for i in range(len(str1)):
    if str1[i] == " ":
        if ch == "Physics":
            ch = "Computer"
            arr.append(ch)
            ch = "Science"
            arr.append(ch)
            ch = ""
        elif ch == "!!!":
            ch = "###"
            arr.append(ch)
            ch = ""
        else:
            arr.append(ch)
            ch = ""
    else:
        ch = ch + str1[i]
    
print(arr)