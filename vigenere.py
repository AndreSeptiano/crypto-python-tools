def init():
    alphabet_chars   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_mapping = {char:idx for idx,char in enumerate(alphabet_chars)}
    return alphabet_chars, alphabet_mapping

def cipher(key, plaintext, chars, mapping):
    return ''.join([chars[(mapping[plaintext[i]] + mapping[key[i]]) % 26] for i in range(len(plaintext))])

def decipher(key, ciphertext, chars, mapping):
    return ''.join([chars[(mapping[ciphertext[i]] - mapping[key[i]]) % 26] for i in range(len(ciphertext))])

def get_true_key(key,text):
    true_key = []
    while len(true_key) * len(key) < len(text):
        true_key.append(key)
    return ''.join(true_key)[:len(text)]

def main(key='KEREN',plaintext='CEPATLARI',ciphertext='MIGEGVEIM', to_cipher=True):
    chars, mapping = init()
    if to_cipher:
        key = get_true_key(key,plaintext)
        print('Cipher result: ',end='')
        print(cipher(key, plaintext, chars, mapping))
    else:
        key = get_true_key(key,ciphertext)
        print('Decipher result: ',end='')
        print(decipher(key, ciphertext, chars, mapping))


if __name__=='__main__':
    main(key='DECEPTIVE',plaintext='WEAREDISCOVEREDSAVEYOURSELF',to_cipher=True)