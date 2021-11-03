ALPHABET = list("abcdefghijklmnopqrstuvwxyzæøå")

def key_idx(key, idx):
    idx = idx % len(key)
    return key[idx]


def abc_index(char):
    return ALPHABET.index(char)


def autokey_encrypt(message, key_arr):

    message = list(message)
    keyword = list([ALPHABET[digit] for digit in key_arr])
    key = (list(keyword)+message)[:len(message)]
    
    result = ""
    for idx in range(len(message)):

        res = str(abc_index(message[idx]) + abc_index(key[idx])%len(ALPHABET))
        if len(res)==1:
            res = "0"+res
        
        result += res +" " 
        
    return result.strip()


def autokey_decrypt(enc_message,key_arr):
    enc_message = [int(num) for num in enc_message.split(" ")]

    result = ""
    for idx in range(len(enc_message)):
        res = enc_message[idx]-key_arr[idx]%len(ALPHABET)
        key_arr.append(res)
        result+= ALPHABET[res]

    return result.strip()

def main():
    k1 = [17]
    message = "goddag"
    print("a)\nencrypting %s, with k=%s"%(message,k1))
    encrypted = autokey_encrypt(message,k1)
    print("result:\n"+encrypted)

    k2 = [5]
    enc_message = "23 08 23 12 21 02 04 03 17 13 19"
    print("\nb)\ndecrypting %s, with k=%s"%(enc_message,k2))
    print("result:\n"+autokey_decrypt(enc_message,k2))

main()