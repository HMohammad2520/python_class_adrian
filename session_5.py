# Logical Operation

# if (Condition):
#    Action  -> condition == True
#
# elif (another condition)
#    Action -> another condition == True
#
# else:
#    Action  -> condition == False


"""
age = input('Enter Age: ')

if int(age) > 18:
    print('Legal Age')
    print('Hesab Baz shod')

else:
    print("Illigal Age")
"""

# Indent --> dandaneghi
# Block:
# ----Action  <- `-` = sapce

"""
score = int(input("Enter score: "))

if 18 < score <= 20:
    print("Kheyli Khoob")
    if score == 20:
        print("Jayze")

elif 16 < score <= 18:
    print("Khob")

elif 14 < score <= 16:
    print("Ghabel Ghabool")
      
elif 10 < score <= 14:
    print("niza be talashe bishtar")

elif 0 < score <= 10:
    print("Mardood")

else:
    print("Error")
"""


# Loop --> Halghe
# while -> tazamni ke 
# while (condition):
#     Action
#     break --> halghe ro mishkone
#     continue --> mire az aval halghe
# else:
#     Action --> age break nashe

"""
x = 0

while x < 10:
    print(x) 
    x = x + 1

print(x)

"""

"""
is_connected = False
attempt = 1

while not is_connected:
    print("Connecting...")

    if attempt >= 4:
        print("Failed to connect")
        break
    
    attempt = attempt + 1
"""
"""
x = 0

while x < 100: 
    x = x + 1

    if (x % 2) == 0:
        continue

    print(x)

else:
    print("Tamam")
"""

# for -> be azaye
# for (varible) in (array):

"""
fruits = ['Apple', 'cherry', 'banana']

for fruit in fruits:
    print(fruit)
"""

for i in range(0, 100):
    if (i % 2) == 0:
        continue
    print(i)
else:
    print("Tamam")
