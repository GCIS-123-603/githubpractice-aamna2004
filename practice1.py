#2.2.2 Activity

def bday_message():
    name=input("enter name : ")
    birthmonth=input("enter birth month : ")
    day=int(input("enter day of your birthday :"))
    year=int(input("enter year of your birthday :"))
    print(name , "your birthday is on " , birthmonth, day , " , " , year ,"!")


bday_message()


def calculator ( num1 ,num2):
    print("the sum of ", num1 ,"and ",num2 , "is ", num1+num2)
    print("the difference of " , num1, "and" , num2 , "is ", num1-num2)
    print("the product of " , num1, "and" , num2 , "is ", num1*num2)
    print("the quotient of " , num1, "and" , num2 , "is ", num1/num2)

def main():
    num1=float(input("enter number 1 : "))
    num2=float(input("enter number 2 : "))
    calculator(num1,num2)

main()

#end


