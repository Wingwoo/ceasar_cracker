#Define variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Functions
def ceasar_cipher(string, shift):
    string = string.lower()
    output = ""
    index = ""
    for i in string:
        if i == " ":
            output = output + " "
        elif i in letters:
            if letters.index(i) + shift >= 25:
                shift = shift - 25
            index = letters.index(i)
            shiftedletter = letters[index + shift]
            output = output + shiftedletter
        else:
            output = output + "#"
    return (output)

def ceasar_cracker(known, string):
    count = 0
    while count < 52:
        if known in string:
            return string
        else:
            string = ceasar_cipher(string, -1)
        count = count + 1
        

#Main
print("Ceasar Cipher Cracker | V0.1 | Made By WingwooGaming")
crack = input("What is the string to crack? ")
known_value = input("What is a value that is known to be in the decoded key? ")
print(ceasar_cracker(known_value, crack))

