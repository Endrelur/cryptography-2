import numpy as np
import math
from numpy.core.defchararray import array
from tabulate import tabulate


# Global defeniton of the rCon array
RCON = np.asarray(
    [
        ["00", "00", "00", "00"],
        ["01", "00", "00", "00"],
        ["02", "00", "00", "00"],
        ["04", "00", "00", "00"],
        ["08", "00", "00", "00"],
        ["10", "00", "00", "00"],
        ["20", "00", "00", "00"],
        ["40", "00", "00", "00"],
        ["80", "00", "00", "00"],
        ["1B", "00", "00", "00"],
        ["36", "00", "00", "00"],
    ]
).transpose()

# performs an xor on the provided word with the rCon column that is used this round
def DORCON(w, round):

    rCon = get_column(RCON, int(round / 4))

    return WORDOR(rCon, w)


# performs the xor computation of 2 words.
def WORDOR(w1, w2):
    result = ""
    for i in range(4):
        result += (
            hexor(
                w1[i, 0],
                w2[i, 0],
            )
            + " "
        )
    return get_linear_array(result.strip()).transpose()


# Performs AES key expasion on a 128-bit key
def KEYEXPANSION_128(key):
    # transform the key to a array with shape 4x4 where each column represents a word
    word_arr = get_linear_array(key)

    # do the expansion for n=10 rounds for a 128-bit key, which makes a array of total 44 colums
    # since each round consist of 4 new words.
    for i in range(4, 44):
        pre_word = get_column(word_arr, i - 1)
        if (
            i
        ) % 4 == 0:  # for every new round perform key expansion steps of leading word
            pre_word = DORCON(SBOX(ROTWORD(pre_word)), i)  # fir

        # add the word to the end of the array of words
        word_arr = np.append(
            word_arr, WORDOR(pre_word, get_column(word_arr, i - 4)), axis=1
        )
    return word_arr


# takes two hex values and calculates hex1 xor hex2
def hexor(hex1, hex2):
    # convert to binary
    bin1 = hex2binary(hex1)
    bin2 = hex2binary(hex2)

    # calculate
    xord = int(bin1, 2) ^ int(bin2, 2)

    # cut prefix
    hexed = hex(xord)[2:]

    # leading 0s get cut above, if not length 8 add a leading 0
    if len(hexed) != 2:
        hexed = "0" + hexed

    return hexed


# takes a hex value and returns binary
def hex2binary(hex):
    return bin(int(str(hex), 16))


# returns the column at index n of a numpy 2d array.
def get_column(array, index):
    return array[:, index].reshape(array.shape[0], 1)

def get_row(array,index):
    return array[index,:].reshape(1,array.shape[1])

# This Sbox does not alter input f(x) = x
def SBOX(w):
    return w


# Rotates the input vector 1 step.
def ROTWORD(w):
    return np.roll(w, -1, axis=0)


# Takes a string with space separated hexes and transforms it into a array
def get_linear_array(key):
    array = np.array(key.split(" "))
    return array.reshape(4, int(len(array) / 4)).transpose()

# Prints out the words in a array in a structured fashion to the terminal
def print_words(array, from_column=0, to_column=-1):

    if to_column==-1:
        to_column = array.shape[1]

    headers = []
    for i in range(array.shape[1]):
        headers.append("w" + str(i))
    table = tabulate(array[:, from_column:to_column], headers, tablefmt="psql")
    print(table)

def main():
    key = "2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C"

    expanded = KEYEXPANSION_128(key)
    print("First 6 words:")
    print_words(expanded,0,6)
    
if __name__ == "__main__":
    main()