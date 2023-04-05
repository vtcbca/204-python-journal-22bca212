#python script to check string is palindrome or not
p=input("Enter any String :")
s=p[::-1]
if(p==s):
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")
