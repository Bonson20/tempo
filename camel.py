"""
# In a file called camel.py, implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case. Assume that the 
# user’s input will indeed be in camel case.

def camel_to_snake(camel_case_str):

    

    
    # we assign the snake_case to "" first
    snake_case = ""

    for char in camel_case_str:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

# prompt the user to answer the question

my_prompt = input("what is the name of the variable? ")

print(camel_to_snake(my_prompt))

"""

# In a file called camel.py, implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case. Assume that the 
# user’s input will indeed be in camel case.

# prompt for question

"""
question =  input("what is the variable: ")

def camel_to_snake(camel_case):
    snake_case = ""       # we start with snake_case as ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    
    return snake_case


print(camel_to_snake(question))


"""




""""
#using while loop
i = 0
while i <  3:
    print("Miaw")
    i += 1 
    """
"""
# for loop
for i in range(3):
    print("meow")
"""
"""
print("meow\n" * 3, end= "")
"""

"""
#using while loop with for loop!


while True:
    n = int(input("what is n?  "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

"""
"""
#using while loop with for loop with FUNCTION!
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()

"""

"""
# loops: list
students =["niny", "hary", "bo"]

for i in range(len(students)):
    print(i + 1, students[i])
    """

"""
# loop: dictionary

# below, if there are different catagories,
# we put coma after } and open another ditionary  
# which is {. 
# But we should include all dictionaries{} in list[]
students = {
    "he": "g",
    "ha": "g",
    "ron": "g",
    "dr": "s",
} 

# in dictionary as opposed to in using list, we have 
# to name the actual name of the word we want to get. eg: ["he"]
#print(students["he"])

for student in students:
    print(student, students[student], sep = ": ") 

    """


"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)


main()
"""
"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end = "")
        print()

main()
"""

"""
               #OR
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)
            

main()
"""

# print("meow\n" * 3, end="")



"""
user= input("What is in camel case? ") 

def pp(Ask):
    snake = ""
    for char in Ask:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


pp(user)

"""

"""



             # Assignments for Loop section




               ASSIBNMENT FOR CAMEL CASE TO SNAKE CASE
question = input("what is your varibale: ")

def camel_to_snake(camel):
    snake = ""
    lst=[]
    for char in camel: 
        lst.append(char)
    if lst[0].isupper():
            snake+=lst[0]
    else:
        snake += lst[0]
    for i in range(1, len(lst)):
        
        if lst[i].isupper():
            snake += "_" + lst[i].lower()
        else:
            snake += lst[i]
    print(snake)

camel_to_snake(question)

"""

"""
def coke():
    total = 0
    while total < 50:
        response = int(input("insert the coin: "))
        if response not in [5, 25, 10]:
            print("please insert valid number")
            continue
        total += response

        if total < 50:
            due = 50 - total
            print(f"Amount Due: {due}")
        elif total >= 50:
            owe = total - 50
            print(f"amount owed: {owe} ")
            break
coke()

"""
"""
   # twttr project
def twitter():
    ask = input("give a string: ")
    for char in ask:
        if char not in ["a", "e", "i", "o", "u"]:
            print(char, end="")
        else:
            print("", end="")

twitter()

"""



# def main():
#     plate = input("plate: ")
#     if is_valid(plate):
#         print(plate)
#     else:
#         print("Invalid")

# def is_valid(s):
#     s = s.uppper()
#     for char in s:

#         while 2 < char.len() < 6:
#             s[0 : 2].isalpha()
            
#             return True
    



# main()


def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    # rule 1: length between 2 and 6 characters
    2 < len(s) < 6
    # rule 2: must start with atleast 2 letters
    s[0, 2].isalpha()
    is_num = False
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            is_num = True
            count+=1
        if s[i].isalpha():
            is_num = False

        if count > 0 and is_num == False:
            return False


main()

# while True:
#     try:
#         x = int(input("what is x? "))
#     except:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")




def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    # rule 1: length between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # rule 2: must start with atleast 2 letters
    if not s[0: 2].isalpha():
        return False
    # rule 3: letters and digits only
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            return False
        
    is_num = False
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            is_num = True
            count+=1
        if s[i].isalpha():
            is_num = False

        if count > 0 and is_num == False:
            return False


main()
