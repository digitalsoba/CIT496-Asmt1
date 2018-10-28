PMAX_KEY_SIZE = 26
message = 'HUKUUEUUYREUYYKGRRGNZZKXNGNOLKXTSAQNZYEGNZTRGTOYALSSEHSYGRVSOOLEGIKVKNZOEJYX'
#JUST REALIZED I WASNT REGISTERED WITH HACKTOBERFEST OOF

def getTranslatedMessage(message,key):

    key = -key
    translated = ""

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num >ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

for key in range(1,MAX_KEY_SIZE + 1):
        f = open('wow.txt','a')
        wow = str(getTranslatedMessage(message,key))
        f.write(wow)
        f.write("\n")

        print (key, getTranslatedMessage(message,key))
        print (' ')
print ('All done!')
