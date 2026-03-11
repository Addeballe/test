alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
word = "läxa"
outputword = ""
key = 3
for letter in word.lower():
    if letter == " " or letter == "." or letter == "'" or letter == "-" or letter ==",":
        continue
    if alphabet.index(letter)+key > len(alphabet)-1:
        outputword += (alphabet[alphabet.index(letter)-key])
    else:
        outputword += (alphabet[alphabet.index(letter)+key])
print(outputword.capitalize())