#Command Line Arguments

# import sys 

# print("Hello")
# print(sys.argv)

# print(sys.argv[0]) #pynew_args.py 1 2 3 4
# print(sys.argv[1:])

# print(f'file name{sys.argv[0]}')  #returns output in a list and everything in string.
# import sys
# sum = 0

# for i in sys.argv[1:]:
    
#     sum += int(i)
# print(sum)

# print(sum(int(i) for i in sys.argv[1:]))


# import argparse

# parser = argparse.ArgumentParser()      #Holds all the arguements

# parser.add_argument('Name', help = 'Enter your Name') #positional
# parser.add_argument('Phone',type = int, nargs='?', default= 12345, help = 'Enter your Phone No.') #positional
# parser.add_argument('-a', '--Age', required= True, help = 'Enter your Age') #optional
# parser.add_argument('--t','--True', action= 'store_true') #optional

# args = parser.parse_args()

# print(args.Name)
# print(type(args.Phone))
# print(args.Phone )
# print(args.Age)
# print(args.true)

# import argparse

# parser = argparse.ArgumentParser()      #Holds all the arguements

# parser.add_argument('Name', nargs= '?', default= 'ABC', help = 'Enter your Name') #accept
# parser.add_argument('Colors', nargs= '*',help = 'Enter Colors') #Variable Length
# parser.add_argument('Colors', nargs= '+',help = 'Enter Colors') #one or more

# args = parser.parse_args()

# print(args.Name) #name = 'abc', 'qwe', 'xyz'
# print(args.Colors)

# import argparse

# parser = argparse.ArgumentParser()      #Holds all the arguements

# #Positional Arguements(Order Matters)
# parser.add_argument('city', help = 'Enter your city')
# parser.add_argument('country',help = 'Enter your country')

# #Optional arguements(Can be passed using --key = value)
# parser.add_argument('--name', default= 'Unknown', help = 'Enter your name')
# parser.add_argument('--age',type= int, default=0, help = 'Enter your age')

# args = parser.parse_args()

# print(f'Name: {args.name}')
# print(f'Age: {args.age}')
# print(f'City: {args.city}')
# print(f'Country: {args.country}')


# import argparse

# parser = argparse.ArgumentParser()      #Holds all the arguements

# parser.add_argument('fruits', choices = ['apple', 'banana'], help= 'Enter fruit name')

# args = parser.parse_args()

# print(args.fruits)


# import argparse

# parser = argparse.ArgumentParser(
#     description= 'Enter the name from command line!'
# ) 

# parser.add_argument('-n', '--name', metavar= 'Name', required= True)
# args = parser.parse_args()
# msg = f'Hello {args.name}'
# print(msg)

# import argparse

# parser = argparse.ArgumentParser() 

# parser.add_argument('--limit', metavar= '1-10', type=int, help= 'Maximum value to process')

# args = parser.parse_args()

# print(args.limit)



# import argparse
# def greeting(name, lang):
#     greet={'Englis':'Hello',
#            'Spanish':'Hola',
#            'German':'Hallo',
#            'French':'Salut'}
    
#     msg = f'{greet[lang]} {name}!'
#     print(msg)

# parser = argparse.ArgumentParser(
#     'Get language from user by using cmd'
# )
    
# parser.add_argument('-n', '--name', metavar= 'Name',required=True)
# parser.add_argument('-l', '--lang', metavar= 'Language',choices= ['English', 'Spanish', 'German', 'French'],required=True)

# args = parser.parse_args()

# greeting(args.name, args.lang)



# import argparse

# parser =  argparse.ArgumentParser()

# login_group = parser.add_argument_group('Login Data')
# login_group.add_argument('-u', '--user', help = 'Enter Username')
# login_group.add_argument('-p', '--password', help = 'Enter Password')


# personal_data = parser.add_argument_group('Personal Data')
# personal_data.add_argument('-n', '--name', help= 'Enter Name')
# personal_data.add_argument('-a', '--age', help= 'Enter Age')

# args = parser.parse_args()




# import argparse

# parser =  argparse.ArgumentParser()

# group = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('--upload', action='store_true', help = 'Upload a File')
# group.add_argument('--download', action='store_true', help = 'Download a File')

# args = parser.parse_args()


# if args.upload:
#     print("Uploading...")
# elif args.download:
#     print("Downloading...")


################ COMMAND LINE ARGUMENTS #################

# 1. Take a list of numbers as arguments and print their average.

# import sys
# sum = 0
# a = sys.argv[1:]
# for i in sys.argv[1:]:
#     sum += int(i)
    
# print(sum/len(a))


# 2. Accept a filename and count how many lines it has.

# import sys

# with open(sys.argv[1], 'r') as f:
#     print(len(f.readlines()))


# 3. Pass two words and print the longer one.

# import sys

# if(len(sys.argv[1]) > len(sys.argv[2])):
#     print(sys.argv[1])
# else:
#     print(sys.argv[2])


# 4. Check if a number passed is prime.

# import sys

# for i in range(2, int(sys.argv[1])):
#     if(int(sys.argv[1]) % i == 0):
#         print("Not Prime")
#         break
# print("Prime")


# 5. Accept multiple filenames and print which ones exists.

# for i in sys.argv[1:]:
#     try:
#         with open(i, 'r') as file:
#             a = file.readlines()
#             print(a)
#     except FileNotFoundError as e:
#         print(e)






################ ARGPARSE #################

# 1. Add Two numbers using argparse

# import argparse

# parser = argparse.ArgumentParser()  

# parser.add_argument('num1', type= int, help = 'Enter First No.')
# parser.add_argument('num2', type= int, help = 'Enter Second No.')

# args = parser.parse_args()
# print(args.num1 + args.num2)



# 2.Repeat a Word
# Goal: Accept a word and a count as arguments, print the word that many times.

# import argparse

# parser = argparse.ArgumentParser()  

# parser.add_argument('word', type= str, help = 'Enter a word of your choice')
# parser.add_argument('count', type= int, help = 'Enter the no. of counts')

# args = parser.parse_args()
# n = (args.word + " ") * args.count

# print(n.strip())



# 3.Choose Operation (Add, Subtract)
# Goal: Accept two numbers and an operation (--op add or --op sub)

# import argparse

# parser = argparse.ArgumentParser()  

# parser.add_argument('num1', type= int, help = 'Enter first number')
# parser.add_argument('num2', type= int, help = 'Enter second number')
# parser.add_argument('--op', choices= ['add', 'sub'], required = True, help = 'Enter the Operation to be peformed')

# args = parser.parse_args()

# if args.op == 'add':
#     ans = args.num1 + args.num2

# elif args.op == 'sub':
#     ans = args.num1 - args.num2

# else:
#     print("Enter a valid operation!")

# print(ans)



# 4.Multiple File Inputs
# Goal: Use nargs='+' to accept a list of file names

# import argparse

# parser = argparse.ArgumentParser()  

# parser.add_argument('fname', nargs = '+',  help = 'List of file names')

# args = parser.parse_args()

# print(args.fname)


# 5.Word Counter
# Description:
# Accept a sentence and count number of words.

# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("sentence", type=str, nargs='+', help="The sentence to count words in.")

# args = parser.parse_args()

# sentence = ' '.join(args.sentence)
# n = sentence.split()

# print(len(n))



# 6.Create a User Profile
# Description:
# Collect user's name, age, and gender from command line and print profile.

# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("name", help="Enter your name")
# parser.add_argument("-a","--age", required=True, help="Enter your age")
# parser.add_argument("-g", "--gender", choices=['Male', 'Female'], help="Enter your Gender")

# args = parser.parse_args()

# print(f"The name is {args.name}.")
# print(f"The age is {args.age}.")
# print(f"The gender is {args.gender}.")


# 7.File Analyzer
# Description:
# Take a file name as input, and return:

# Number of lines

# Number of words

# Number of characters
# Based on flags passed.

# Arguments:

# filename (positional)

# --lines (store_true)

# --words (store_true)

# --chars (store_true)

# 8.Temperature Converter
# Description:
# Convert temperature from Celsius to Fahrenheit or vice versa.

# Arguments:

# --value (required, float)

# --to (choices=['C', 'F'], required)

# 9.Search for Word in File
# Description:
# Search for a word in a text file and print line numbers containing that word.

# Arguments:

# filename (positional)

# --word (required)

# 10.Try to give a example using all types of arguments in parser.add_argument()
