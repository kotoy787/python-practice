# Задание 1
word = input()
for i in range(10):
    print(i, word)

# Задание 2
n = int(input())
for i in range(n + 1):
    if i == 0:
         print("Квадрат числа", i, "равен", i ** 2)
    if i > 0 and n > 0:
         print("Квадрат числа", i, "равен", i ** 2)

# Задание 3
n = int(input())

for i in range(n):              
    for j in range(n - i):      
        print('*', end='')
    print() 

# Задание 4
m = int(input())          
p = int(input())          
n = int(input())          

multiplier = 1 + p / 100  
population = m            

for day in range(1, n + 1):       
    print(day, population)        
    population = population * multiplier   

    
         
        
    
   








    