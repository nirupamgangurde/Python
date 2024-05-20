ask = input("type encode to 1 a word and 2 to decode a word : ")

if(ask == "1"):
    encode = input("Enter the word you want to encode of 2 characters or more than 2 characters : ")
    random = 'kid'
    encode2 = random + encode[1:] + encode[0] + random

    if(len(encode) > 3):
        print(encode2)

    elif(1 < len(encode) <= 3):
        print(encode[::-1])


    else:
        print('Please type more than 1 character')

elif(ask == '2'):
    decode = input("Enter the word you want to decode of 2 characters or more than 2 characters : ")
    decode2 = decode[3:-3]
    decode2 = decode2[-1] + decode2[:-1]


    if(len(decode) > 3):
        print(decode2)


    elif(1 < len(deocde) <= 3):
        print(decode[::-1])

    else:
        print('Please type more than 1 character')