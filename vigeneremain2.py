# input is basically printf and scanf combined
text = input('Enter text (preferably without spaces):\n')
key = input('Enter key\n')
# force uppercase for simplicity
text = text.upper()

from vigenereenc import rptkey
key = rptkey(text, key.upper())


def cmd():
    # This doesnt work without the int
    act = int(input('1 for ENC \n2 for DEC\n'))
    if act is 1:
        # conditional selective importing
        from vigenereenc import encry
        print(encry(text, key))
    elif act is 2:
        from vigenereenc import decry
        print(decry(text, key))
    else:
        print('Invalid input')
        return

cmd()