# 1.UNIVERSITY QUESTION:JUNE 2022

# Write a python program to generate the following type of pattern for the given N
# rows .
# 1
# 1 2
# 1 2 3
# 1 2 3 4

"""
n=int(input("ENTER THE NUMBER OF ROWS:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()


#2.UNIVERSITY QUESTION:JUNE 2022 (7 marks)
# Write a Python program to find distance between two points (x1,y1) and (x2,y2).

x1=int(input("x CO-ORDINATE OF FIRST POINT:"))
y1=int(input("y CO-ORDINATE OF FIRST POINT:"))
x2=int(input("x CO-ORDINATE OF SECOND POINT:"))
y2=int(input("y CO-ORDINATE OF SECOND POINT:"))
X=x2-x1
Y=y2-y1
print(abs((X+Y)/2))



# 3. UNIVERSITY QUESTION:JUNE 2023(7 marks)
# Write a python program to generate prime numbers within a certain range

lower=int(input("ENTER THE LOWER LIMIT:"))
upper=int(input("ENTER THE UPPER LIMIT:"))
print(f"PRIME NUMBERS BETWEEN {lower} AND {upper}:",end=" ")
if lower==0 or lower==1:
	lower=2
for i in range(lower,upper+1):
	flag=0
	for j in range(2,(i//2)+1):
		if i%j==0:
			flag=1
	if flag==0:
		print(i,end=" ")
		

# 4.UNIVERSITY QUESTION:-JUNE 2023 (7marks)
# Write a python program to generate the following type of pattern for the given N rows where N <= 26.
# A
# A B
# A B C 
# A B C D 

N=int(input("ENTER A NUMBER:"))
if N<=0 or N>26:
	print("PLEASE ENTERA NUMBER IN BETWEEN 1-26")
else:
	for i in range(0,N):
		for j in range(i+1):
			print(chr(65+j),end=" ")
		print()
		
		
# 5.UNIVERSITY QUESTION:MAY 2023 (7 marks)
# Write a Python program to check whether a number is Armstrong number or not.
# An Armstrong number is an n-digit number that is equal to the sum of the n
# th
# powers of its digits.
# Examples: 153 = 1^3+ 5^3+ 3^3, 1634= 1^4+ 6^4+ 3^4+ 4^4

"""
n=input("ENTER A NUMBER:")
l=len(n)
sum=0
x=int(n)
n=x
while x>0:
	digit=x%10
	x=x//10
	sum+=digit**l
if n==sum:
	print(f"{n} IS  AN ARMSTRONG NUMBER")
else:
	print(f"{n} IS NOT AN ARMSTRONG NUMBER"
	
	
	
#6.UNIVERSITY QUESTION:MAY 2023 (7 marks)
#Write a Python program to find the roots of a quadratic equation, ax^2+ bx + c =0 . Consider the cases of both real and imaginary roots.
"""
print("ax^2+bx+c")
a=float(input("ENTER VLUE FOR a:"))
b=float(input("ENTER VLUE FOR b:"))
c=float(input("ENTER VLUE FOR c:"))
desc=(b**2)-(4*a*c)
if desc<0:
	print(f"root1={(-1*b)/(2*a)}+{(-desc)/(2*a)}i")
	print(f"root2={(-1*b)/(2*a)}-{(-desc)/(2*a)}i")
else:
	desc=(desc)**0.5
	print(f"root1={((-1*b)+desc)/(2*a)}")
	print(f"root2={((-1*b)-desc)/(2*a)}")
	
          
# 7.UNIVERSITY QUESTION :JUNE 2023(7 marks)
# Write a python program to find X^Y or pow(X,Y) without using standard function 

x=int(input("ENTER VALUE FOR X:"))
y=int(input("ENTER VALUE FOR Y:"))
res=1
for i in range(1,y+1):
	res=res*x
print(f" {x} ^{y} = {res}")


# 8.Write a python program to generate the following type of pattern for the given N
# rows .
# 1 2 3 4
# 1 2 3 
# 1 2 
# 1

n=int(input("Enter no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#9. UNIVERSITY QUESTION:JUNE 2023 ( 7 marks )
# Write a python program to find the sum of the cosine series 1 - x^2/2! + x^4/4!-.......

x=float(input("ENTER THE VALUE OF X:"))
n=int(input("ENTER THE NUMBER OF TERMS:"))
sum=1
power=2
sign=-1
for i in range(2,n+1):
	fact=1
	for j in range(1,power+1):
		fact*=j
	res=(x**power)/fact
	sum=sum+(res*sign)
	power=power+2
	sign*=-1	
print(f"SUM={sum}")


# 10.Consider the mathematical expression (a+b)^2=a^2+2ab+b^2. Write a Python
# program that takes user input for values of a and b, then evaluates both sides of
# the expression. Finally, compare the results and print whether the equation holds
# true or false.   (UQ-MAY 2024)'''  

a =int(input("Enter the value of a: "))
b =int(input("Enter the value of b: "))
lhs = (a + b)**2  
rhs = a**2 + 2*a*b + b**2  
if lhs == rhs:
    print("The equation holds true.")
else:
    print("The equation does not hold true.")



#11.Write a Python program to print all prime factors of a given number.(UQ-JAN 2024)
n = int(input("Enter a number: "))
print("Prime factors of", n, "are:")

for i in range(2, n + 1):
    is_prime = True  
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and n % i == 0:
        print(i, end=" ")
       
       

# 12.UNIVERSITRY QUESTION:JANUARY 2024(6 marks)
# Write a Python program to print all numbers between 100 and 1000 whose sum
# of digits is divisible by 9.

"""
for i in range(100,1001):
	n=i
	sum=0
	while n>0:
		digit=n%10
		sum+=digit
		n=n//10
	if sum%9==0:
		print(i)
    
          		
# 13.UNIVERSITY QUESTION: JANUARY 2024
# Write a program that accepts the lengths of three sides of a triangle as inputs and
# outputs whether or not the triangle is a right triangle.(3 marks)


s1=float(input("BASE:"))
s2=float(input("HEIGHT:"))
s3=float(input("HYPOTENUSE:"))
if s3**2==(s1**2)+(s2**2):
	print("RIGHT ANGLED TRIANGLE!")
else:
	print("NOT A RIGHT ANGLED TRIANGLE!")
	
	
	
"""
#14.UNIVERSITY QUESTION:MAY 2024(7 marks)
#Consider the mathematical expression (a+b)2=a2+2ab+b2. Write a Python
#program that takes user input for values of a and b, then evaluates both sides of
#the expression. Finally, compare the results and print whether the equation holds
#true or false.
"""
a=int(input("ENTER VALUE FOR \'a\':"))
b=int(input("ENTER VALUE FOR \'b\':"))
rhs=(a+b)**2
lhs=(a**2)+(2*a*b)+(b**2)
if rhs==lhs:
	print("TRUE")
else :
	print("FALSE")
	
	
	
	
"""
#15.UNIVERSITY QUESTION:MAY 2024(7 marks)
#Write a python program to find out the eldest and youngest of three individuals ,
#with their ages being input through the keyboard.(without using max, min
#functions)
"""
age1=int(input("ENTER TH EAGE OF FIRST PERSON:"))
age2=int(input("ENTER THE AGE OF SECOND PERSON:"))
age3=int(input("ENTER THE AGE OF THIRD PERSON:"))
if age1>age2 and age1>age3:
	print("FIRST PERSON IS ELDEST")
elif age2>age1 and age2>age3:
	print("SECOND PERSON IS ELDEST")
else:
	print("THIRD PERSON IS ELDEST")
if age1<age2 and age1<age3:
	print("FIRST PERSON IS YOUNGEST")
elif age2<age1 and age2<age3:
	print("SECOND PERSON IS YOUNGEST")
else:
	print("THIRD PERSON IS YOUNGEST")


