code = str(input())
shuffled_alphabet = str(input())
decode = ''
original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {shuffled_alphabet[i]: original_alphabet[i] for i in range(len(original_alphabet))}

for letter in code:
    if letter in dic.keys():
        decode = decode + dic[letter]
    if letter == ' ':
        decode = decode + ' '

print(decode)