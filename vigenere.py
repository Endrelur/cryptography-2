ALPHABET = list("abcdefghijklmnopqrstuvwxyzæøå")


def key_idx(key, idx):
    idx = idx % len(key)
    return key[idx]


def abc_index(char):
    return ALPHABET.index(char)


def encrypt_vigenere(plainText, key):
    result = ""

    plainText = list(plainText.lower())
    key = list(key.lower())
    for idx in range(len(plainText)):
        newLetter = (abc_index(plainText[idx]) + abc_index(key_idx(key, idx))) % len(
            ALPHABET
        )
        result += ALPHABET[newLetter]
    return result.upper()


def decrypt_vigenere(encryptedText, key):
    result = ""
    encryptedText = list(encryptedText.lower())
    key = list(key.lower())

    for idx in range(len(encryptedText)):
        decryptedLetter = (
            abc_index(encryptedText[idx]) - abc_index(key_idx(key, idx)) + len(ALPHABET)
        ) % len(ALPHABET)
        result += ALPHABET[decryptedLetter]
    return result.lower()


enc = "LPÆLZJWKKBGYÅMFGWÆÆYYMBKVÆRYAÆFOFJGOMDDZIVGFÆØRXMYYRLZQÆIBXYÅÆYGKHSKLING"
key = "ELSKLING"
result = decrypt_vigenere(enc, key)
print("Decrypting:\n" + "'" + enc + "'" + "\nWith key:\n" + "'" + key + "'")
print("result:\n" + result)
