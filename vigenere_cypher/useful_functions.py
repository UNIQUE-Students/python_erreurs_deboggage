MAX_ORD = 1114111


def encrypt_letter(msg, key):
    enc_id = (ord(msg) + ord(key)) % (MAX_ORD + 1)
    return chr(enc_id)


def decrypt_letter(msg, key):
    dec_id = (ord(msg) - ord(key)) % (MAX_ORD + 1)
    return chr(dec_id)


def encrypt_message(message, key):
    encrypted_msg = ""
    for i_msg in range(len(message)):
        i_key = i_msg % len(key)
        msg_letter = message[i_msg]
        key_letter = key[i_key]
        encrypted_letter = encrypt_letter(msg_letter, key_letter)
        encrypted_msg += encrypted_letter
    return encrypted_msg


def decrypt_message(message, key):
    decrypted_msg = ""
    for i_msg in range(len(message)):
        i_key = i_msg % len(key)
        msg_letter = message[i_msg]
        key_letter = key[-i_key]
        decrypted_letter = decrypt_letter(msg_letter, key_letter)
        decrypted_msg += decrypted_letter
    return decrypted_msg
