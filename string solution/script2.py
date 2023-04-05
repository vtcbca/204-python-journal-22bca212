#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def paliwordcount(p):
    s=p.split(" ")
    x=0
    y=[]
    for i in s:
        if (i==i[::-1]):
            x=x+1
            y.append(i)
    if x>0:
        print(" Palindrome Word In Sentence Is {x} And Palindrome Words Are:{y}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
p=input("enter a sentece:")
paliwordcount(p)
