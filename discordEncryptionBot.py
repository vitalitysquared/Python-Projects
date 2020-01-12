##run in 3.6.2

import discord as dc
import time
from datetime import datetime
from threading import Timer



#################################Encryption
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
           '.', ' ', '?', ',', '-', '+', '=', '[', ']', ';', ':', '<', '>', '/',
           "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", '"', "'", '|']


##Assigns all the letters a unique number
def letter_to_num(character):
    return letters.index(character)

##Converts back to letters given a number
def num_to_letter(num):

    return letters[num]

##Converts words to numbers
def text_to_nums(text):
    
    indexList = []

    for letter in text:
        indexList.append(letter_to_num(letter))

    return indexList

##converts numbers to words
def nums_to_text(numList):

    string = ''
    for i in numList:
        string += num_to_letter(i)
    return string

##Creates a new encryption key
def append_new(numList, number):
    
    if number in numList:
        return numList
    else:
        numList.append(number)
        return numList

##Takes out duplicate letters in the keyword
def remove_dup(numList):
    
    nonDup = []
    for i in numList:
        if i not in nonDup:
            nonDup.append(i)
    return nonDup
    
##Rearranges the numbers
def extend(numList):

    longList = range(0, len(letters))

    for i in longList:
        if i not in numList:
            numList.append(i)
    return numList

##Cycles the number list once
def cycle1(numList):

    numList.insert(0, numList.pop())
    return numList

##Detemines how many times to cycle
def cycle(numList, nCycles):  

    cycleCount = 0
    while cycleCount < nCycles:
        cycle1(numList)
        cycleCount += 1
    return numList


##Goes and remaps the numbers and letters
def mapping(keyword, letter):

    numList = remove_dup(text_to_nums(keyword))
    extend(numList)
    nCycles = letter_to_num(letter)
    cycle(numList, nCycles)
    return numList

##Finds an intem inside the num list
def find_item(numList, n):

    return numList[n]

##Does the inverse, finds an index for an item
def find_index(numList, n):
    
    return numList.index(n)

##Encrypts the list
def enc_list(key, numList):

    encryptedList = []
    for i in numList:
        encryptedList.append(find_item(key, i))
    return encryptedList

##Decrypts the list                
def dec_list(key, numList):

    decryptedList = []  
    for i in numList:
        decryptedList.append(find_index(key, i))
    return decryptedList

##Uses above to encyrpt
def encrypt(key, letter, message):

    keyWord = mapping(key, letter)
    messageNums = text_to_nums(message)
    encryptedNums = enc_list(keyWord, messageNums)
    encryptedMessage = nums_to_text(encryptedNums)
    return encryptedMessage

##Uses above to decrypt
def decrypt(key, letter, ciphertext):

    encryptedNums = text_to_nums(ciphertext)
    keyWord = mapping(key, letter)
    decryptedList = dec_list(keyWord, encryptedNums)
    decryptedWords = nums_to_text(decryptedList)
    return decryptedWords

##END ENCRYPTION
######################
#######################

##Date for encryption
day = time.strftime('%a')
dayLetter = day[0]
calendarDate = time.strftime('%d %b %Y')
combined = dayLetter + calendarDate
print(combined)







##Bot start
client = dc.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=dc.Game(name="Encrypting Stuff"))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == "Hello":
        await client.send_message(message.channel, "World")

    if message.content.startswith('!encrypt'):
        shortenedMessage = message.content[9:]
        await client.send_typing(message.channel)
        await client.send_message(message.channel, encrypt(calendarDate, dayLetter, shortenedMessage))
        ##await client.send_message(message.channel, combined)
        await client.delete_message(message)

    if message.content.startswith('!decrypt'):
        shortenedMessage = message.content[9:]
        await client.send_typing(message.channel)
        await client.send_message(message.channel, decrypt(calendarDate, dayLetter, shortenedMessage))
        ##await client.send_message(message.channel, combined)
        await client.delete_message(message)


    if message.content.lower() == ('!commands'):
        cmdList = ('! then any of the following: [encrypt or decrypt, followed by text] Ex: !encrypt test')
        await client.send_typing(message.channel)
        await client.send_message(message.channel, cmdList)




client.run('DISCORD KEY HERE')
