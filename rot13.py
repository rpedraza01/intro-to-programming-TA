# rot13.py
def rot13(text):

    alphabet         = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    output = ''
    for char in text:
        index = alphabet.find(char)
        output += alphabet_rotated[index]
    return output

rot13()