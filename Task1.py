i=0
j=[]
while i<5:
    strng = input("please enter string: ")
    j.append(strng)
    i+=1

maximum=len(max(j))
print(f'Maximum length of string is {maximum}')
