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
    listed = []
    while count < 52:
        if known in string:
            if string in listed:
                pass
            else:
                listed.append(string)
                print ("Possible value is: " + string)
        else:
            string = ceasar_cipher(string, -1)
        count = count + 1

def ceaser_no_key_cracker(string):
    commonwords = ["the", "of", "and", "to", "in", "is", "you", "that", "it", "he", "her", "was", "for", "on", "are", "as", "with", "his", "hers", "they", "at", "be", "this", "have", "from", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "do", "how", "their", "if", "will"]
    debugwords = ["the", "of"]
    count = 0
    listed = []
    while count < 1000000:
        for word in commonwords:
            if word in string:
                if string in listed:
                    pass
                else:
                    listed.append(string)
                    print ("Possible value is | " + string + " | with the word " + word)
        string = ceasar_cipher(string, -1)
        count = count + 1

def organise(listedstrings):
    listed = listedstrings
    dictionary = {}

    
#Main
print("Ceasar Cipher Cracker | V0.3 | Made By WingwooGaming")
crack = input("What is the string to crack? ")
#known_value = input("What is a value that is known to be in the decoded key? ")
#print(ceasar_cracker(known_value, crack))
ceaser_no_key_cracker(crack)
