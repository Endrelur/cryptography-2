from operator import xor
from aes_keyexpand import get_linear_array, get_column,get_row ,WORDOR, main, print_words
import numpy as np
message = get_linear_array("24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95")
enc_message = get_linear_array("26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D6 1E")
key = get_linear_array("67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7")

# Performs xor with the provided word and round key
def ADDROUNDKEY(w,key):

    assert w.shape[1] == key.shape[1], "The provided word does not have the same amount of colums as key" 
    assert w.shape[0] == key.shape[0], "The provided word does not have the same amount of rows as key" 

    result = np.empty((w.shape[0],0),dtype=w.dtype)

    for col_index in range(w.shape[1]):
        result = np.append(result,WORDOR(get_column(w,col_index),get_column(key,col_index)),axis=1)

    return result

# f(x) = x
def SUBBYTES(w):
    return w

# Shifts rows to the left if encrypting, to the right if not. Shifts with row index as step size.
def SHIFTROWS(w,decrypt = False):
    result = np.empty((0,w.shape[1]),dtype=w.dtype)

    multiplier = (1) if decrypt else (-1)

    for row_index in range(w.shape[0]):
        result = np.append(result,np.roll(get_row(w,row_index),multiplier*row_index,1),axis=0)
    
    return result

def bad_encrypt_stepbystep(message,key):

    print("original message:")
    print_words(message)

    addroundkey = ADDROUNDKEY(message,key)
    print("step 1: ADDROUNDKEY")
    print_words(addroundkey)

    subbytes = SUBBYTES(addroundkey)
    print("step 2: SUBBYTES(x) = x")
    print_words(subbytes)

    shiftrows = SHIFTROWS(subbytes)
    print("step 3: SHIFTROWS")
    print_words(shiftrows)



def bad_decrypt_stepbystep(enc, key):

    print("encrypted message:")
    print_words(enc)

    shiftrows = SHIFTROWS(enc,decrypt=True)
    print("step 1: (un)SHIFTROWS")
    print_words(shiftrows)

    subbytes = SUBBYTES(shiftrows)
    print("step 2: SUBBYTES⁻¹(x) = x")
    print_words(subbytes)

    addroundkey = ADDROUNDKEY(subbytes,key)
    print("step 3: ADDROUNDKEY")
    print_words(addroundkey)
    
