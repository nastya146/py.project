from tkinter import *
from tkinter import ttk

class File:
    def __init__(self, t = "", k = "", c = "", cr = ""):
        self.text = t
        self.key = k
        self.command = c
        self.cryp = cr
        
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

window = Tk()
window.title('Crypt')

window.geometry('500x500')

frame = Frame(window, padx = 10, pady = 10);
frame.pack(expand = True)

func = Label(frame, text = "Choose command(code or decode)")
func.grid(row=3, column = 1)

func_in = Entry(frame)
func_in.grid(row = 4, column = 1)

crypt = Label(frame, text = "Choose type of cryptographer (Cesar, Vigenere, Vernam)")
crypt.grid(row = 5, column = 1)

crypt_in = Entry(frame)
crypt_in.grid(row = 6, column = 1)

txt = Label(frame, text = "Write your text")
txt.grid(row = 7, column = 1)

txt_in = Entry(frame, width = '50')
txt_in.grid(row = 8, column = 1)

keyword = Label(frame, text = "Write keyword")
keyword.grid(row = 9, column = 1)

keyword_in = Entry(frame)
keyword_in.grid(row = 10, column = 1)

def result(ex):
    if ex.cryp == "Cesar":
        if ex.command == "code":
            return (Cesar(ex.text, int(ex.key)))
        return (DeCesar(ex.text, int(ex.key)))
    if ex.cryp == "Vigenere":
        if ex.command == "code":
            return (Vigenere(ex.text, ex.key))
        return (DeVigenere(ex.text, ex.key))
    if ex.cryp == "Vername":
        if ex.command == "code":
            #return (Vernam(ex.text, ex.key))
            return ("Vername in progress...")
        #return(DeVernam(ex.text, ex.key))
        return("DeVernam in progress")
    return "You enter someting wrong, try again"

def ShowText():
    ex = File()
    ex.command = func_in.get()
    ex.cryp = crypt_in.get()
    ex.text = txt_in.get()
    ex.key = keyword_in.get()
    label['text'] = result(ex)
    
on_btn = Button(frame, text = 'perform', command=ShowText)
on_btn.grid(row = 11, column = 1)

txt_hack = Label(frame, text = "If you want hack cipher, enter path to txt file")
txt_hack.grid(row = 13, column = 1)


txt_hack_in = Entry(frame, text = "If you want hack cipher, enter path to txt file")
txt_hack_in.grid(row = 14, column = 1)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Hack(lines):
    lines = lines.lower()
    freq_dic={}
    for letter in alphabet:
        freq_dic[letter] = lines.count(letter)
    sorted_freq = (sorted(freq_dic.items(), key = lambda x: -x[1]))
    most_freq = sorted_freq[0][0]
    return Cesar(lines, ord('e') - ord(most_freq))

def CallHack():
    path = txt_hack_in.get()
    file = open(path, 'r')
    txt_to_hack = file.readlines()
    print(*txt_to_hack)
    print(type(*txt_to_hack))
    file.close()
    file = open(path, 'a')
    hacked_txt = Hack(*txt_to_hack)
    file.writelines('\n'+ hacked_txt)
    file.close()
    label2['text'] = "Your file was hacked"
    
    

hacker_btn = Button(frame, text = 'hack', command=CallHack)
hacker_btn.grid(row = 15 , column = 1)


label = ttk.Label(frame)
label.grid(row = 12, column = 1)

label2 = ttk.Label(frame)
label2.grid(row = 16, column = 1)

window.mainloop()