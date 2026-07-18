
name = "Python"
version = 0.9
year = 1991

print(name)
print(version)
print(year)

num, num2 = 9, 89
print(num == num2)   
print(num != num2)   
num, num_2, num_3 = 12, 13, 14
print(num, num_2, num_3)
num = num_2 = num_3 = 48
print(num, num_2, num_3)

num = 9
num_2 = 90

num, num_2 = num_2, num

print(num)
print(num_2)
