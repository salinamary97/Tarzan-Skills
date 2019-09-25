if LOOP CONDITION EXAMPLES
1) Age=int(input("Enter your Age : "))
if Age>=18:

    print(f"{Age} is your age and you are eligible for Voting")
else:

    print(f'{Age} is my age and is not eligible for voting')
2) Marks= int(input('Enter your score obtained: '))
if Marks>=90 and Marks<=100:
    print(f"{Marks} is under Grade A")
elif Marks>=80 and Marks<=90:
    print(f"{Marks} is under Grade B")
elif Marks>=70 and Marks <=80:
    print(f"{Marks} is under Grade C")
elif Marks>=60 and Marks<=70:
    print(f"{Marks} is under Grade D")
else:
    print(f"{Marks} is under Grade E")
3)Num = int(input("Enter a Number :"))
if Num%2==0:
    print(f"{Num} is Even Number")
else:
    print(f"{Num} is Odd Number")
X=1
while X<=10:
    print(X)
    X+=1
print('END')

