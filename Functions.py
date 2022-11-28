import Globals as gl


def LetterCipher(char, delta):
    if char >= "A" and char <= "Z":
        return chr((ord(char) + delta - ord("A")) % 26 + ord("A"))
    if char >= "a" and char <= "z":
        return chr((ord(char) + delta - ord("a")) % 26 + ord("a"))
    return char


def Cesar(text, key):
    temp = ""
    for i in range(len(text)):
        temp += LetterCipher(text[i], key)
    return temp


def DeCesar(text, key):
    temp = ""
    for i in range(len(text)):
        temp += LetterCipher(text[i], -key)
    return temp


def Vigenere(text, key):
    text = text.upper()
    key = key.upper()
    size_t = len(text)
    size_k = len(key)
    key = key * (size_t // size_k) + key[: (size_t % size_k)]
    ciphered_txt = ""
    for i in range(size_t):
        ciphered_txt += LetterCipher(text[i], ord(key[i]) - ord("A"))
    return ciphered_txt


def DeVigenere(text, key):
    text = text.upper()
    key = key.upper()
    size_t = len(text)
    size_k = len(key)
    key = key * (size_t // size_k) + key[: (size_t % size_k)]
    enciphered_txt = ""
    for i in range(size_t):
        enciphered_txt += LetterCipher(text[i], 2 * ord("A") - ord(key[i]))
    return enciphered_txt


def Vernam(text, key):
    return Vigenere(text, key)


def DeVernam(text, key):
    return DeVigenere(text, key)


def result(ex):
    if ex.cryp == "Cesar":
        if ex.command == "code":
            return Cesar(ex.text, int(ex.key))
        return DeCesar(ex.text, int(ex.key))
    if ex.cryp == "Vigenere":
        if ex.command == "code":
            return Vigenere(ex.text, ex.key)
        return DeVigenere(ex.text, ex.key)
    if ex.cryp == "Vernam":
        if ex.command == "code":
            if len(ex.text) == len(ex.key):
                return Vernam(ex.text, ex.key)
            return "You enter something wrong.\n The lengh of the text should be equal to the lengh of the key"
        if len(ex.text) == len(ex.key):
            return DeVernam(ex.text, ex.key)
        return "You enter something wrong.\n  The lengh of the text should be equal to the lengh of the key"
    return "You enter something wrong.\nPlease, try again..."


def ShowText():
    ex = gl.Global()
    ex.command = gl.Global.func_in.get()
    ex.cryp = gl.Global.crypt_in.get()
    ex.text = gl.Global.txt_in.get()
    ex.key = gl.Global.keyword_in.get()
    gl.Global.label["text"] = result(ex)


def Hack(lines):
    lines = lines.lower()
    freq_dic = {}
    for letter in gl.Global.alphabet:
        freq_dic[letter] = lines.count(letter)
    sorted_freq = sorted(freq_dic.items(), key=lambda x: -x[1])
    most_freq = sorted_freq[0][0]
    return Cesar(lines, ord("e") - ord(most_freq))


def CallHack():
    path = gl.Global.txt_hack_in.get()
    file = open(path, "r")
    txt_to_hack = file.readlines()
    print(*txt_to_hack)
    print(type(*txt_to_hack))
    file.close()
    file = open(path, "a")
    hacked_txt = Hack(*txt_to_hack)
    file.writelines("\n" + hacked_txt)
    file.close()
    gl.Global.label2["text"] = "Your file was hacked"
