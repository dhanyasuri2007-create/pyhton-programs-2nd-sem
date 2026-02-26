year=int(input("Enter the number"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Non Leap year")