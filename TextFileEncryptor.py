import os
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alpha)

capAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
capAlpha_list = list(capAlpha)

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
punc_list = list(punc)

# â is " 'd " in text - some old text unicode for apostrophes vary

encrypt_value_list = []

fileName = input("Enter text file to encrypt: \n")
file1 = open(fileName, 'r')
Lines = file1.readlines()

key_stream = int(input("Enter a number to shift backwards by: "))
# can shift forwards or backwards - editable

x = 0
y = 0
hold = []
capHold = []  # initial hold for capital letters - not fully implemented
# can take capital letters as input, will convert to lowercase

encrypt_value_list = []

for line in Lines:
    # removes line breaks since they count as part of the string
    # group sentence into a list first
    line = line.replace("\n", "")
    list1 = list(line.split(" "))

    # make each word in list into own list - used for loop
    # https://www.tutorialspoint.com/convert-list-into-list-of-lists-in-python
    list1 = [[words] for words in list1]
    print(list1)
    lenList = len(list1)
    for i in range(0, lenList):
        # line below splits the word into letters
        newList = list(list1[i][0])
        lenNewList = len(newList)  # length of list

        for j in range(0, lenNewList):
            letter = newList[j]
            if letter in punc_list:
                # holds punctuation and place to put it back later
                hold.append(letter)
                x = j
                continue
            # capital letters work here - cannot keep capitalization
            if letter in capAlpha_list:
                value = capAlpha_list.index(letter)
                capHold.append(capAlpha_list[value])

                # --- HERE --- shift backwards with "-" or forwards with "+"
                encrypt_value = (value + key_stream) % 26
                encrypt_value_list.append(encrypt_value)
                continue
            else:
                value = alpha_list.index(letter)

                # --- HERE --- shift backwards with "-" or forwards with "+"
                encrypt_value = (value + key_stream) % 26
                encrypt_value_list.append(encrypt_value)
        letter_list = []
        for letter in encrypt_value_list:
            convert = alpha_list[letter]
            letter_list.append(convert)
        # adds back punctuation if any
        if hold:
            letter_list.insert(x, hold[0])
            hold.clear()
            x = ""

        # joins the individual letters
        joined_letter_list = ''.join(map(str, letter_list))
        list1[i] = joined_letter_list
        newLine = " ".join(map(str, list1))  # joins the words with spaces
        encrypt_value_list.clear()

    line = newLine
    # ----Output here - remember to change destination and how (append / write)
    file1 = open("Page3.txt", "a")
    file1.write(line + "\n")
    print(line)

file1.close()
