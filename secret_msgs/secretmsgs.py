alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
newMessage = ''
newMessage2 = ''
newMessage3 = ''
key = 3
key2 = 5
key3 = 10

message = input('Please enter a message: ')
print('Your original message is', message)
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is:', newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
#print('Your new message is', newMessage)

for character in newMessage:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key2) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is:', newCharacter)
        newMessage2 += newCharacter
    else:
        newMessage2 += character
#print('Your new message is', newMessage2)

for character in newMessage2:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key3) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is:', newCharacter)
        newMessage3 += newCharacter
    else:
        newMessage3 += character
print('Your new message is', newMessage3)
