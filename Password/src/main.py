import random


#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1 = int(random.randint(0,10))
digit2 = int(random.randint(0,10))
ponctuationSign1 = chr(random.randint(33,47))
ponctuationSign2 = chr(random.randint(33,47))

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + ponctuationSign1  + ponctuationSign2
password = shuffle(password)

#Ouput
print(password)