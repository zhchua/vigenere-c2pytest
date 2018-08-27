# repeat key until length matches text
def rptkey(text, rkey):
    # // is for int div to get floor, since str cant * by float
    mkey = rkey*(len(text)//len(rkey))
    # cant just use for
    # need to account for when difference is 0 -> without if will still append first char
    if len(mkey) < len(text):
        for i in range(len(text)-len(mkey)):
            mkey = mkey + rkey[i]
    return mkey


# using another function to simplify formulae
# character value relative to 'A', where 'A' is 0
def crv(alpha):
    relval = ord(alpha) - ord('A')
    return relval


def encry(ptext, key):
    #  % len(key)
    # Necessary to declare ctext as list first
    ctext = []
    for i in range(len(ptext)):
        # Use append to add to rear of list
        ctext.append(chr(ord('A') + ((crv(ptext[i]) + crv(key[i])) % 26)))
    return ''.join(ctext)


def decry(ctext, key):
    ptext = []
    for i in range(len(ctext)):
        ptext.append(chr(ord('A') + ((crv(ctext[i]) - crv(key[i])) % 26)))
    return ''.join(ptext)
