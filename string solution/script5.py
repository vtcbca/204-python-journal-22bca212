#WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
#strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.
#Example:
#Enter string : KhoKho
#String is Symmetrical.


def symmetric(m):
    half=(len(m)//2)
    first=m[:half]
    second=m[half:]
    if first==second:
        print(f"String {m} is symmetric!!!!")
    else:
        print(f"String {m} is not symmetric!!!")

def input1():
     a=input("Enter a string:")
     symmetric(a)
     
input1()  
