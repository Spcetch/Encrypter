def read_menu(): 
    print ('''
            A. Encrypt a Message 
            B. Quit

            ''')
    runMenu = True 
    while runMenu == True:
        typeAnswer = input ("Enter In Option").lower() 
        if typeAnswer == "a":
            encrypt() 
        elif typeAnswer =="b":
            runMenu = False 
        else:
            print ("Unknown Function")
def encrypt():
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    message = input ("Please enter what you want to encrypt").lower() 
    encryptedMessage = "" 
    key = input ("Please enter the key: ") 
    key = int (key) 
    for char in message: 
        if char in alphabet:
            position = alphabet.find(char) 
            newPosition = (position + key) % 26
            encryptedMessage = encryptedMessage + alphabet [newPosition]
        else:
            encryptedMessage = encryptedMessage + char
            print ("Your encrypted message is:", encryptedMessage) 
    with open('cypher.txt','a+') as myFile:
            myFile.write (encryptedMessage)
            myFile.write('\n') 
    read_menu ()
    
    
read_menu ()