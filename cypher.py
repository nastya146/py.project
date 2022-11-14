command = input("Choose command: code or decode\n")
cryptographer = input("Choose type of cryptographer: Cesar, Vigenere, Vernam\n") 
text = input("Write your text\n")
key = input("Write keyword\n")



class File:
    def __init__(self, t, k, c, cr):
        self.text = t
        self.key = k
        self.command = c
        self.cryp = cr

ex = File(text, key, command, cryptographer)

def LetterCipher(char, delta):
    if char >= 'A' and char <= 'Z':
        return chr((ord(char) + delta - ord('A')) % 26 + ord('A'))
    if char >= 'a' and char <='z':
        return chr((ord(char) + delta - ord('a')) % 26 + ord('a'))
    return char

def Cesar(text, key):
    temp = ''
    for i in range(len(text)):
        temp += LetterCipher(text[i], key)
    return temp

def DeCesar(text, key):
    temp = ''
    for i in range(len(text)):
        temp += LetterCipher(text[i], -key)
    return temp

def Vigenere(text, key):
    text = text.upper()
    key = key.upper()
    size_t = len(text)
    size_k = len(key)
    key = key * (size_t // size_k) + key[:(size_t % size_k)]
    ciphered_txt = ''
    for i in range(size_t):
        ciphered_txt += LetterCipher(text[i], ord(key[i])-ord("A"))
        print(ciphered_txt)
    return ciphered_txt

def DeVigenere(text, key):
    text = text.upper()
    key = key.upper()
    size_t = len(text)
    size_k = len(key)
    key = key * (size_t // size_k) + key[:(size_t % size_k)]
    enciphered_txt = ''
    for i in range(size_t):
        enciphered_txt += LetterCipher(text[i], 2 * ord("A") - ord(key[i]))
    return enciphered_txt

def Vernam(text, key):
    pass

def DeVernam(text, key):
    pass

if ex.cryp == "Cesar":
    if ex.command == "code":
        print(Cesar(ex.text, int(ex.key)))
    else:
        print(DeCesar(ex.text, int(ex.key)))
elif ex.cryp == "Vigenere":
    if ex.command == "code":
        print(Vigenere(ex.text, ex.key))
    else:
        print(DeVigenere(ex.text, ex.key))
else:
    if ex.command == "code":
        print(Vernam(ex.text, ex.key))
    else:
        print(DeVernam(ex.text, ex.key))
