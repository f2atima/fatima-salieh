import math,re

def calculate_area(r):
 return math.pi*r**2

calculate_circumference=lambda r:2*math.pi*r

radius=float(input("Enter radius: "))
area=calculate_area(radius)
circumference=calculate_circumference(radius)

print("Area:",round(area,2))
print("Circumference:",round(circumference,2))

text=input("Enter a string: ")
numbers=re.findall(r'\d+',text)
numbers=[int(n) for n in numbers]

def calculate_sum(n):
 return sum(n)

double=lambda x:x*2

total=calculate_sum(numbers)
doubled=double(total)

print("Numbers:",numbers)
print("Sum:",total)
print("Double:",doubled)

input_numbers=input("Enter numbers separated by commas: ")
numbers=[float(x) for x in input_numbers.split(",")]

def square_numbers(n):
 return list(map(lambda x:x**2,n))

squares=square_numbers(numbers)

print("Squares:",squares)
print("Max square:",max(squares))
print("Sqrt sum:",math.sqrt(sum(squares)))

password=input("Enter password: ")

if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'\d',password):
 strength="Strong"
else:
 strength="Weak"

scores_input=input("Enter 5 scores: ")
scores=[float(s) for s in scores_input.split()]

def calculate_average(n):
 return sum(n)/len(n)

round_avg=lambda x:round(x)

average=calculate_average(scores)

print("Password:",strength)
print("Rounded avg:",round_avg(average))

paragraph=input("Enter paragraph: ")

vowel_words=re.findall(r'\b[aeiouAEIOU]\w*',paragraph)

def count_vowels(t):
 return len(re.findall(r'[aeiouAEIOU]',t))

total_vowels=count_vowels(paragraph)

word_lengths=list(map(lambda w:len(w),vowel_words))

if word_lengths:
 average_length=round(sum(word_lengths)/len(word_lengths),2)
else:
 average_length=0

print("Vowel words:",vowel_words)
print("Total vowels:",total_vowels)
print("Avg length:",average_length)