print("---menue---")
print("press 1 for lenth")
print("press 2 for minimum")
print("press 3 for maximum")
print("press 4 for sum of all ")
print("press 5 for avrage ")
print("press 6 for sote all the list ")
print("press 7 for exit....")
option=int(input("enter option you want : "))


while True:
   
    if option ==1:
        ls=int(input("enter value you want: "))
        arr=[]
        for i in range(ls):
            val=int(input("enter list value : "))
        print(len(val))
        break

    if option==2:
        ls=int(input("enter value you want: "))
        arr=[]

        for i in range(ls):
            val=int(input("enter list value : "))
        print(min(ls))
        break
        
    if option==3:
        ls=int(input("enter value you want: "))
        arr=[]

        for val in ls:
             val=input("enter list value : ")
             print(max(val))
        break

    if option==4:
        ls=int(input("enter value you want: "))
        arr=[]

        total=0
        for val in ls:
             val=input("enter list value : ")
             total=total+val
             print(total)
        break

    if option==5:
        ls=int(input("enter value you want: "))
        arr=[]

        total=0
        for i in ls:
             val=input("enter list value : ")
             total=total+val/2
             print(total)
        break

    if option==6:
        print("---6th option menue---")
        print("press 1 for asending...")
        print("press 2 for disending...")
        ls=int(input("enter value you want: "))
        arr=[]


        for i in ls:
            val=int(input("enter list vlue6: "))
        print(ls.sote(val))
        break

    if option==7:
        print("thenk you for exiting......")
        break
        
            
