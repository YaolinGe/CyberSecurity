"""
This script is trying to decrypt the information of a text. 

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2023-10-10
"""


def decipher_text(text, n): 
    """
    This function is trying to decipher the text.
    """
    text_deciphered = ''
    texts = text.split(' ')
    for text in texts: 
        print(text)
        for l in text: 
            # only shift it in the alphabet, not in ascii
            if ord(l) >= 97 and ord(l) <= 122: # lower case
                text_deciphered += chr((ord(l) - 97 + n) % 26 + 97)
            elif ord(l) >= 65 and ord(l) <= 90: # upper case
                text_deciphered += chr((ord(l) - 65 + n) % 26 + 65)
            else: 
                text_deciphered += l
        text_deciphered += ' '
    # reoganize the text
    print(text_deciphered)
            

if __name__ == "__main__": 
    # print("Hello World!")
    # for i in range(26): 
    decipher_text("Otkz D zvmizy v amzz kjdio! di ocz wjs wzgjr.", 8)
