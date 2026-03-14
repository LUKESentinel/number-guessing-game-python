'''print("hello TARA_FAMILY!")'''

#  Practice1 - Python

'''n = int(input("Enter a number: ")
        digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)'''





#2reversed no output

'''rev = 0

while n > 0:
    digit = n % 10       1l=8    2l= 5   3l = 4
    rev = rev * 10 + digit  1l = 8   2l = 85   3l = 854
    n = n // 10  1l= 45    2l = 4  3l = 0

print("Reversed number:", rev)'''


'''n = int(input("enter a no"))

count = 0

while n > 0:
     count = count + 1
     n = n // 10
print("no of digits:", count)'''


#2plaindrome no check

'''n = int(input("enter a no:"))

sum = 0

while n > 0:
   digit = n % 10
   sum = sum + digit
   n = n // 10
print("sum =",sum)'''

'''n = int(input("enter a no to check if its plaindrome or not:"))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10



if  rev == original:
 print("it is plaindrome")

else:

 print("it is not a plaindrome")'''

#armstrong no check

'''n = int(input("enter a no to check if its armstrong number or not:"))

original = n
start = 0

while n > 0:
   digit = n % 10
   cube = digit ** 3
   start = start + cube
   n = n // 10

if  start == original:

 print("its an armstrong no") 

else:  
 print("it is nor an armstrong no:")'''

#prime no check

'''n = int(input("enter a no to check if its prime no or not:"))

start = 2

while n > start:
    
    n % start
if  n % start == 0:


 print("it is not prime no")

 break 

start = start + 1  

else:
 print ("it isn't a prime no") '''  


# attempt 2

'''n = int(input("Enter a number: "))

start = 2

while start < n:
    if n % start == 0:
        print("Not a prime number")
        break
    start = start + 1
else:
    print("Prime number")'''


# count digits


'''n = int(input("enter a no:"))

count = 0

while n > 0:
    digit = n % 10

    count =  count + 1
    n = n // 10



print(" no of digits:",count ) '''



'''#reversing no


n = int(input("enter a no:"))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("reversed no =", rev)'''

#perfect no check


'''n = int(input("enter a no:"))

sum = 0

start = 1

while n > start:
    if n % start == 0:
     sum = sum + start
    start = start + 1

            
    
       

if sum == n:
 print("it is a perfect no:")

else: 
 print("it is not a perfect no")
    '''


# even odd no check

''' n = int(input("enter a no:"))

if n % 2 == 0:
 print("it is an even no") 

else:  
 print("it is an odd no")  '''
        
#prime no  check revise

'''n = int(input("enter a no:"))

sum = 0
i = 2

while n < 2:
 print("it is not prime no")

 while n > n:
   digit = n // i

   if n % i == 0: print("it is not a prime no")  

   sum = i + 1

 else: print("it is not a prime no") 
 n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        sum = sum + digit

    n = n // 10

print("Sum of even digits =", sum)
'''

#count digits

'''n = int(input("enter a no to count the even digits"))


i = 0

while n > 0:
   even = n % 10


   if even % 2 == 0:
    
    
    i = i + 1
   n = n // 10
   

print("count of even digits:",i)      



n = int(input("Enter a number: "))

count = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        count = count + 1

    n = n // 10

print("Count of even digits:", count)




#odddigit problem


n = int(input("enter a no to count the odd digits:"))

count = 0

while n > 0:

    digit = n  % 10

    if digit % 2 != 0:
        count = count + 1
    n = n // 10    


print("no of count digits:", count)    '''

'''
#largest digit prgrm


n = int(input("enter a no:"))


max_digit = 0

   

while n > 0:
    digit = n % 10

    if digit > max_digit:
        max_digit = digit

     

    n = n // 10    

print("largest digit of the number:", max_digit) '''


#numbers grater than a specific number

'''n = int(input("enter a no:"))


larno = 0


while n > 0:
    digit = n %  10

    if digit > 5:
        larno = larno + 1
        print (digit)
        
    
    

    n = n // 10

print(" no of digits greater than 5:", larno)      '''



# no greater than the specific no and the sum of those numbers



'''n = int(input("enter a no:"))



sum = 0


while n > 0:
    digit = n %  10
    

    if digit > 5:
        sum = sum + digit

    n = n // 10

print("sum of numbers greater than 5 is:", sum) '''



# building a number from given no

'''n = int(input("enter a no:"))

newno = 0


while n > 0:
    digit = n % 10
    if digit > 5:
        newno = newno * 10 + digit
    n = n // 10



print("new number formed:", newno) '''







# checking if all the digits of a number are even

'''n = int(input("enter a no to check if all the digits of the number are even:"))




while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        print("all the digits of the number are not even")    
        break
        

    

    n = n // 10


else: 
    print("all the number of the given number are even")'''




# "FOR LOOPS"


'''i = 1
for i in range(100):
    print(i)


for i in range (1 , 6):
    print(i)  

for i in range(0, 11, 2):
    print(i) '''


#revision problems of while loop

'''n = int(input("enter a no to check the digits of the number:"))


count  = 0


while n > 0:
    
    digit = n // 10
    count = count + 1
    n = n // 10


print("no of digits:", count)'''  




'''n = int(input("enter a no to find the sum of even digits of the number:"))

sum = 0

while n > 0:
    digit = n % 10
    if n % 2 == 0:
        sum = sum + digit

    n = n // 10


print ("sum of the even digits", sum)









n = int(input("enter a no to check if the number contains any zero:"))



while n > 0:
    digit = n % 10
    if digit  == 0:
        print("the number contain zero") 
        break
    n = n // 10

else: print("the number does not contain any zero in it")   '''




#AGAIN TO FOR LOOP


'''for i in range(1,11):
    print(i)'''


'''for i in range(2,20,2):
    print(i)'''


'''for i in range (1, 20):
    if i % 2 == 0:

     print (i)''' 


'''for i in range(1,30):
    if i % 2 == 0:
        continue
    print (i)'''


'''for i in range(1,30):
    if i % 3 != 0:
    
    
      if i % 5 != 0:    
         
         print(i)'''





'''for i in range(1, 30):  # outer loop
    for j in range(1, 11):  # inner loop
        print(i, "*", j, "=", i*j)
    print("----")  # just to separate rows'''

# revision problem (count the digits)


'''n = int(input("enter a no:"))

count = 0


while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10


print ("number of digits:",count)  ''' 



#revision problem (sum of digits)

'''n = int(input("enter a no:"))


sum = 0


while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("sum of the digits:",sum)'''


#revision problem (checking if a number is a special number)


'''n = int(input("enter a number to check if the number is special or not:"))


sum = 0
product = 1


while n > 0:
    digit = n % 10
    sum = sum + digit
    product = product * digit
    n = n // 10

if sum == product:
      print("it is a special no")  

else:
      print(" it is not a special number")'''


#checking if a number is a strong number or not


'''n = int(input("enter a no to check if the number is a strong number:"))




while n > 0: 
    digit = n % 10

    i = digit
    fact = 1
    while i > 0:
     fact = i * fact
     i = i - 1
     n = n // 10


print(fact)'''


#revioson problem
'''
n = int(input("enter a number:"))
while n > 0:
  digit = n % 10
  print(digit)
  n = n // 10'''
    

'''n = int(input("enter a number:"))


while n > 0:

    digit = n % 10
    if digit > 5:
       print(digit)   

    n = n // 10



print("digits greater than 5 are:", digit)     ''' 



'''n = int(input("enter a number:"))

count = 0
while n > 0:
     digit = n % 10
     if digit == 0:
          count = count + 1
     n = n // 10


if count == 0:
    print("there is not any zero in the entered number") 

else:
    print("no of zeros in the number is",count)'''


#practice 

'''n = int(input("enter a number:"))

count = 0

while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10

print("number of digits",count)    '''


# practice 2
#it was done


# problem 3

'''n = int(input("enter a number:"))

sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit

    n = n // 10


print ("sum of digits:", sum)    '''


#problem 4


'''n = int(input("enter a number:"))

original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n //10

if rev == original:
    print("it is a plaindrome number")

else:  print("it is not a plaindrome number")  '''  

#31/01/2026


'''n = int(input("enter a number to chech how many even digits are there:"))

count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count = count + 1
    n = n // 10

print("number of even digits:",count)   '''   


'''n = int(input("enter a number to check how many digits are greater than 5:"))

count = 0

while n > 0:
    digit = n % 10
    if digit > 5:
        count = count + 1

    n = n // 10

print("digits greater than 5 are:",count)  '''    


'''n = int(input("enter a number to check if the number contains any zero:"))

count = 0
while n > 0:
    digit = n % 10
    if digit == 0:
        count = count + 1

    n = n // 10    
        
print("there are",count, "zeros in the entered number")'''

'''list = [2, 5, 9, 8, 5]
print(list[1])'''


'''list = [2, 4, 6, 4, 10, 3, 7, 2, 1]
i = 0
count = 0

while i < len(list):
    
    if list[i] % 2 == 0:
        print(list[i])
        count = count + 1
    i = i + 1

print("no of even digits",count)'''


'''numbers =[2, 5, 7, 5, 10, 8, 73, 98]


i = 0
count = 0'''

'''while i < len(numbers):
    if numbers[i] % 2 != 0:
        print(numbers[i])
        count = count + 1
    i = i + 1

print("no of odd digits in the list:",count)'''     


'''Numbers = [7, 8, 86, 90, 5, 4, 9, 34, 23, 12, 56, 78, 69, 34]

i = 1
lrge = Numbers[0]

while i < len(Numbers):
    if Numbers[i] > lrge:  
        lrge = Numbers[i]
    i = i + 1    
    
        

print("largest digit in the list:",lrge)'''



'''Numbers = [7, 8, 86, 90, 5, 4, 9, 34, 23, 12, 56, 78, 69, 34]

i = 1
smallest = Numbers[0]

while i < len(Numbers):
    if Numbers[i] < smallest:
        smallest = Numbers[i]
    i = i + 1    

print("smallest digit in the list:",smallest)'''    


'''numbers = [7, 8, 86, 90, 5, 4, 9, 34, 23, 12, 56, 78, 69, 34]

i = 0
count = 0

while i < len(numbers):
    if numbers[i] > 50:
        count = count + 1
    i = i + 1    
    

print("no of digits greater than  50 are:",count)'''        


#next class doubt that when to use ">" and "<"



'''numbers =[2, 4, 6]

sum = 0
i = 0

while i < len(numbers):
    sum = sum + numbers[i]
    i = i + 1

print("sum of the numbers in the list = ",sum)'''    


'''numbers =[2, 4, 6, 8]
sum = 0
i = 0
count = 0
greater = 0
hum = 0

while i < len(numbers):
    number = greater + numbers[i]
    greater = greater + 1

    sum = sum + numbers[i]
    i = i + 1
    count = count + 1

Average  = sum / count 

if number > Average:
    hum = hum + 1

print ("numbers greater than Average number are = ",hum)'''


'''numbers =[2, 4, 6, 8]

i = 0
count = 0
while i < len(numbers):
    digit = numbers[i]
    i = i + 1
    count = count + 1

print("no of digits:", count)'''


'''n = int(input("enter a number:"))

count = 0
while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10
print("no of digits:",count)'''

'''n = int(input("enter a number:"))

count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit)
        count = count + 1
    n = n // 10

print("number of even digits:",count) '''
























'''import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

n = 120   # number of circles

for i in range(n):
    color = colorsys.hsv_to_rgb(i/n, 1, 1)
    t.pencolor(color)
    t.circle(100)
    t.right(360 / n)

turtle.done()'''





















'''import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(2)

n = 360   # smoothness

for i in range(n):
    color = colorsys.hsv_to_rgb(i/n, 1, 1)
    t.pencolor(color)

    t.circle(150)
    t.left(59)   # magic angle ✨

turtle.done()'''





















'''mport turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)

man = turtle.Turtle()
man.hideturtle()
man.speed(0)
man.pensize(3)

def draw_man(x, y, leg_angle):
    man.penup()
    man.goto(x, y)
    man.setheading(0)
    man.pendown()

    # head
    man.circle(10)

    # body
    man.right(90)
    man.forward(30)

    # left leg
    man.left(30 + leg_angle)
    man.forward(25)
    man.backward(25)

    # right leg
    man.right(60 + leg_angle * 2)
    man.forward(25)
    man.backward(25)

    # arms
    man.left(30 + leg_angle)
    man.backward(15)
    man.left(40)
    man.forward(20)
    man.backward(20)

    man.right(80)
    man.forward(20)
    man.backward(20)

# animation loop
x = -200
angle = 20

while x < 200:
    man.clear()
    draw_man(x, 0, angle)
    screen.update()

    x += 5
    angle = -angle  # switch leg position
    time.sleep(0.05)

turtle.done()'''






















'''import turtle
import colorsys
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

layers = 6
petals = 120

def draw_petal(radius, angle, color):
    t.pencolor(color)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

for layer in range(layers):
    r = 80 + layer * 30

    for i in range(petals):
        hue = (i / petals + layer / layers) % 1
        color = colorsys.hsv_to_rgb(hue, 1, 1)

        t.penup()
        t.goto(0, 0)
        t.setheading(i * (360 / petals))
        t.forward(layer * 20)
        t.pendown()

        draw_petal(r, 60, color)

    t.right(360 / layers)

screen.update()
turtle.done()'''





'''n = int(input("enter a number: "))

count = 0

while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10
print("number of digits:",count)'''    


'''n = input("enter a number: ")

count = 0

while n != "0":
    count += 1
    n = n + 1

print("number of digits:", count)'''


     
'''n = int(input("enter a number:"))

if n > 10:
    if n % 2 == 0:
        print("the number is even and greater than 10")

else:
    print("it is not even and greater than 10")'''


'''numbers = [12, 7, 45, 23, 89, 34, 56, 90, 11, 67,
           3, 19, 72, 38, 44, 5, 29, 61, 17, 80,
           92, 14, 26, 31, 48, 53, 9, 70, 64, 21,
           6, 39, 84, 27, 15, 96, 33, 58, 41, 73,
           2, 77, 50, 62, 88, 36, 24, 69, 13, 55]'''




'''for i in range (len(numbers)):  
    if numbers[i] % 2 == 0:
        print(i,"it is an even number")
    elif numbers[i] % 2 != 0:
        print(i,"it is an odd number") '''

'''numbers = [12, 7, 45, 23, 89, 34, 56, 90, 11, 67] 


i = 0

for i in numbers:
    if i % 2 == 0:
      if i > 50:
        print(i, "-> greater than 50")'''



'''numbers = [12, 7, 45, 23, 89, 34, 56, 90, 11, 67] 


smallest = numbers[0]
largest = numbers[0]

for i in numbers:
    if  i < smallest:
        smallest = i
    if i > largest:
        largest = i

print("smallest number: ",smallest)        
print("largest number: ",largest)'''


'''numbers = [12, 7, 45, 23, 89, 34, 56, 90, 11, 67]


for i in numbers:
        
    if i % 2 == 0:
        print(i)'''

'''numbers = [12, 7, 45, 23, 89, 34, 56, 90, 11, 67,78, 21, 44, 59, 63, 72, 18, 95, 31, 40,52, 26, 84, 13, 37, 64, 29, 73, 91, 15,88, 47, 62, 39, 54, 20, 96, 33, 71, 24,60, 42, 81, 19, 68, 53, 75, 27, 49, 100]
    
largest = numb--ers[0]
second_largest = numbers[0]

for i in numbers:
    '''

'''numbers = [12, 7, 45, 23, 89, 34]

for i in range(len(numbers)):
      if numbers[i] == 23:
            print(i)'''
         
'''for i, num in enumerate(numbers):
    print(i, num)       

numbers = [12, 7, 45, 23, 89, 34]'''



'''numbers = [23, 87, 45, 12, 99, 34, 76, 54, 88, 67, 21, 90, 43, 65, 78, 32, 56, 91, 11, 73, 84, 29, 60, 47, 82]

largest = numbers[0]
second_largest = float('-inf') 


for i in numbers:
      if i > largest:
             second_largest = largest
             largest = i

      elif i > second_largest and i != largest:
            second_largest = i  


print("second largest number in the list:", second_largest)'''  





'''numbers = [34, -12, 78, 5, -45, 92, 11, -3, 67, 54, -89, 23, 41, -7, 0, 19, 88, -56, 73, 6, -14, 39, 81, -22, 47, 2, -99, 65, 31, -8, 58, 90, -34, 12, 76, -1, 4, 69, -27, 83, 15, -62, 97, 28, -16, 53, 71, -40, 36, 60]

largest = numbers[0]
second_largest = float('-inf')
third_largest = float('-inf')



for i in numbers:
      if i > largest:
            third_largest = second_largest
            second_largest = largest
            largest = i


      elif i > second_largest and  i != largest:
            third_largest = second_largest
            second_largest = i


print("largest number in the list:",largest)
print("second largest number in the list:",second_largest)     
print("third largest number in the list:",third_largest)'''




'''numbers = [34, -12, 78, 5, -45, 92, 11, -3, 67, 54, -89, 23, 41, -7, 0, 19, 88, -56, 73, 6,
           -14, 39, 81, -22, 47, 2, -99, 65, 31, -8, 58, 90, -34, 12, 76, -1, 4, 69, -27,
           83, 15, -62, 97, 28, -16, 53, 71, -40, 36, 60]

largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')
fourth_largest = float('-inf')
fifth_largest = float('-inf')

for num in numbers:

    if num > largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = num

    elif num > third_largest and num != second_largest and num != largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = num

    elif num > fourth_largest and num != third_largest and num != second_largest and num != largest:
        fifth_largest = fourth_largest
        fourth_largest = num

    elif num > fifth_largest and num != fourth_largest and num != third_largest and num != second_largest and num != largest:
        fifth_largest = num


print("Largest:", largest)
print("Second Largest:", second_largest)
print("Third Largest:", third_largest)
print("Fourth Largest:", fourth_largest)
print("Fifth Largest:", fifth_largest)'''




#this code was writtes by me myself!
'''numbers = [34, 12, 78, 45, 9, 23, 67, 89, 54, 31]

largest = numbers[0]
second_largest = float('-inf')
third_largest = float('-inf')
fourth_largest = float('-inf')
fifth_largest = float('-inf')


for i in numbers:
    if i > largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = i

    elif i > third_largest and i != second_largest:
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = i         


    elif i > fourth_largest and i != third_largest:
        fifth_largest = fourth_largest
        fourth_largest = i

    elif i > fifth_largest and i != fourth_largest:
        fifth_largest = i   



print("largest:", largest)    
print("second largest:", second_largest)    
print("third largest:", third_largest) 
print("fourth largest:", fourth_largest)
print("fifth largest:", fifth_largest)'''





    
'''numbers = [56, 12, 89, 3, 45, 67, 23, 1]
    
smallest = numbers[0]
second_smallest = float('inf')
third_smallest = float('inf')


for i in numbers:
    if i < smallest:
        third_smallest = second_smallest
        second_smallest = smallest
        smallest = i


    elif i < second_smallest and i != smallest:
        third_smallest = second_smallest
        second_smallest = i

    elif i < third_smallest and i != second_smallest:
        third_smallest = i


print("smallest:", smallest) 
print("second smallest:", second_smallest)
print("third smallest", third_smallest )'''       


'''numbers = [56, 12, 89, 3, 45, 67, 23, 1]

count = 0

for i in numbers:
    if i % 2 != 0:
        count = count + 1

print("no of odd digits in the list:", count)  '''      


    

'''numbers = [34, -12, 78, 5, -45, 92, 11, -3, 67, 54, -89, 23, 41, -7, 0, 19, 88, -56, 73, 6,
           -14, 39, 81, -22, 47, 2, -99, 65, 31, -8, 58, 90, -34, 12, 76, -1, 4, 69, -27,
           83, 15, -62, 97, 28, -16, 53, 71, -40, 36, 60]

sum = 0
for i in numbers:
    if i > 50:
        sum = sum + i


print("sum of the numbers greater than 50:", sum)'''
        

'''numbers = [34, -12, 78, 5, -45, 92, 11, -3, 67, 54, -89, 23, 41, -7, 0, 19, 88, -56, 73, 6,
           -14, 39, 81, -22, 47, 2, -99, 65, 31, -8, 58, 90, -34, 12, 76, -1, 4, 69, -27,
           83, 15, -62, 97, 28, -16, 53, 71, -40, 36, 60]

sum = 0
for i in numbers:
    if i > 50:
        sum = sum + i


print("sum of the numbers greater than 50:", sum)'''
        


'''numbers = [34, -12, 78, 5, -45, 92, 11, -3, 67, 54, -89, 23, 41, -7, 0, 19, 88, -56, 73, 6,
           -14, 39, 81, -22, 47, 2, -99, 65, 31, -8, 58, 90, -34, 12, 76, -1, 4, 69, -27,
           83, 15, -62, 97, 28, -16, 53, 71, -40, 36, 60]


positive = 0
negative = 0
zeros = 0

for i in numbers:
    if i > 0:
        positive = positive + 1

    elif i < 0:
        negative = negative + 1

    elif i == 0:
        zeros = zeros + 1

print("positive numbers", positive)                
print("negative numbers:", negative)
print("zeros",zeros)'''

# 11/03/2026

'''numbers = [12, 67, 45, 89, 23, 76, 34, 90]

count = 0

for i in numbers:
    if i > 50:
        count = count + 1

print(count)'''

'''numbers = [12, 67, 45, 89, 23, 76, 34, 90]

odd = 0
even = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1

    elif i % 2 !=  0:
        odd = odd + 1

print("no of odd numbers:",odd)        
print("no of even numbers:",even)'''


'''numbers = [12, 7, 18, 21, 4, 9, 10]


total = 0

for i in numbers:
    if i % 3 == 0:
        total += i

print("sum:", total)'''


'''numbers = [23, 56, 12, 89, 34, 67]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    
print(numbers.index(largest))'''

'''
numbers = [45, 12, 78, 3, 67, 23]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(numbers.index(smallest))'''


'''numbers = [45, 12, 78, 3, 67, 23]

smallest = numbers[0]
second_smallest = float('inf')
index = 0

for i in range(len(numbers)):
    if numbers[i] < smallest:
        second_smallest = smallest
        smallest = numbers[i]
        i = index
        
    elif numbers[i] < second_smallest and numbers[i]  != smallest:
        print("second smallest =", second_smallest)


print("second smallest:", second_smallest)
print("index:", index)'''


#12/0/2026

'''
numbers = [34, -5, 12, -67, 0, 89, -23, 45, -1]


count = 0

for  i in numbers:
    if i < 0:
        count = count + 1

print("no on ODD numbers:",count)        
  '''

'''
numbers = [45, 12, 78, 3, 90, 23, 1, 67]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print("smallest number in the list: ",smallest)        
'''
'''
numbers = [10, 15, 22, 33, 41, 50, 63]

total = 0

for i in numbers:
    if i % 2 != 0:
        total = total + i

print("sum of odd numbers:",total)        
'''


'''
numbers = [12, 7, 5, 18, 21, 30, 9, 14]

odd = 0
even = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1

    if i % 2 != 0:
        odd = odd + 1

print("odd numbers:",odd)
print("even numbers:", even)  '''          

'''
numbers = [12, 7, 5, 18, 21, 30, 9, 14]

largest = float('-inf')
smallest = float('inf')

for i in  numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i    


print("largest no:",largest)
print("smallest no:",smallest)
'''
'''
numbers = [12, 7, 5, 18, 21, 30, 9, 14]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i


print("largest no:",largest)        
print("second largest no:",second_largest) '''       

'''
numbers = [12, 7, 5, 18, 21, 30, 9, 14]

reversed_list = []


for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
    
print(reversed_list)   '''

'''for i in range(10,0,-1):
    print(i)'''
        
'''for i in range(20,-1,-4):
    print(i)'''

'''
table = 23
for i in range(1,11):
    print(table, "x",i,"=",table * i)
    '''

'''numbers = [12, 7, 5, 18, 21, 30, 9, 14]

largest = float('-inf')
second_largest = float('-inf')

largest_index = -1
second_largest_index = -1

for i in range(len(numbers)):
    current = numbers[i]

    if current > largest:
        second_largest = largest
        second_largest_index = largest_index

        largest = current
        largest_index = i

    elif current > second_largest and current != largest:
        second_largest = current
        second_largest_index = i

print("Second largest number:", second_largest)
print("Index of second largest:", second_largest_index)'''


'''numbers = [34, 12, 78, 5, 90, 23]

largest = numbers[0]
second_largest = -999999

largest_index = 0
second_largest_index = -1

for i in range(len(numbers)):

    if numbers[i] > largest:
        second_largest = largest
        second_largest_index = largest_index

        largest = numbers[i]
        largest_index = i

    elif numbers[i] > second_largest and numbers[i] != largest:
        second_largest = numbers[i]
        second_largest_index = i

print("Second largest:", second_largest)
print("Index:", second_largest_index)'''
'''
numbers = [27, 93, 14, 65, 42, 88, 31]

largest = numbers[0]
largest_index = 0

for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
        largest_index = i

print("largest no:",largest)
print("index:",largest_index)  '''  

'''numbers = [12, 45, 67, 23, 89, 34, 56]

largest = numbers[0]
largest_index = 0

second_largest = numbers[0]
second_largest_index = -1

for i in range(len(numbers)):
    if numbers[i] > largest:
        second_largest = largest
        second_largest_index = largest_index

        largest = numbers[i]
        largest_index = i

    elif numbers[i] > second_largest:
        second_largest = numbers[i]
        second_largest_index = i

print("second largest:",second_largest)
print("index:",second_largest_index)  '''



'''numbers = [34, 12, 78, 5, 90, 23]

smallest = numbers[0]
smallest_index = 0

for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
        smallest_index = i
        
print("smallest no:",smallest)
print("index:",smallest_index)'''


'''numbers = [12, 45, 67, 23, 89, 34, 56]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    elif i < smallest:
        smallest = i

print("largest:",largest)
print("smallest",smallest)        
print("difference:",largest - smallest)'''


'''numbers = [12, 45, 67, 23, 89, 34, 56]

odd = 0
even = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1

    if i % 2 != 0:
        odd = odd + 1

print("odd no:",odd )
print("even no:",even)'''

'''
numbers = [56, 23, 89, 12, 67, 34, 78]

smallest = numbers[0]
second_smallest = float['inf']
smallest_index = 0
second_smallest_index = -1

for i in range(len(numbers)):
    if numbers[i] < smallest:
        second_smallest = smallest
        second_smallest_index = smallest_index

        smallest = numbers[i]
        smallest_index = i

    elif numbers[i] < second_smallest and numbers[i] != smallest:
        second_smallest = numbers[i]
        second_smallest_index = i

print("second smallest no:", second_smallest)
print("index:",second_smallest_index)'''


 #14/03/2026 NUMBER GUISSING GAME GITHUB 2ND PROJECT:


'''import random

number = random.randint(1,100)


attempts = 7

print("total attemts to guess the number: 7")

guess = int(input("pick a number from 1 to 100:"))

while attempts > 0:
    if guess > number:
      print("TOO HIGH!")

    elif guess < number:
        print("TOO LOW!")

    else:
         print("congratulations!! you won") 
         break
    
    attempts = attempts - 1
    
    guess = int(input("try again!:"))
    
    print("attempts left:",attempts)  

if attempts == 0 and guess != 0:
    print("☠️ GAME OVER! the number was:",number)'''


import random

number = random.randint(1,100)

print("you only have 7 attempts to guess the number")

guess = int(input("pick a number from 1 to 100:"))

attempts = 7

while attempts > 0:

    if guess > number:
        print("CHOOSE A MORE LOWER NUMBER")
    
    elif guess < number:
        print("CHOOSE A MORE HIGHER NUMBER")

    else:
        print("CONGRATULATIONS!! YOU WON🥳")
        break

    attempts = attempts - 1     

    guess = int(input("TRY AGAIN:"))
    print("ATTEMPTS LEFT:",attempts)

           

if attempts == 0 and guess != number:
    print("☠️GAME OVER! THE NUMBER WAS =", number)    





































































































































































































































































































































































































































































































































































































































































































































































































































































