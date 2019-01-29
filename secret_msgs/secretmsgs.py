message = input('Please enter a message: ')
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    newMessage = ''
    key = 3
    key2 = 5
    key3 = 10
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newPosition2 = (newPosition + key2) % 26
            newPosition3 = (newPosition2 + key3) % 26
            newCharacter = alphabet[newPosition3]
            newMessage += newCharacter
        else:
            newMessage += character
    return newMessage
    print(newMessage)
def decode(newMessage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    oldMessage = ''
    key = 3
    key2 = 5
    key3 = 10
    for character in newMessage:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition3 = (position - key3) % 26
            newPosition2 = (newPosition3 - key2) % 26
            newPosition = (newPosition2 - key) % 26
            newCharacter = alphabet[newPosition]
            oldMessage += newCharacter
        else:
            oldMessage += character
    return oldMessage
    print(oldMessage)

newMessage = encode(message)
oldMessage = decode(newMessage)
print(newMessage)
print(oldMessage)
