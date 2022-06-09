#!/usr/bin/env python
import argparse
import os
from useful_functions import encrypt_message, decrypt_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, help="Message to be encrypted or decrypted.")
    parser.add_argument("--key", type=str, help="Key to use to encrypt or decrypt the message.")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["enc", "dec"],
        help="Wether to encrypt ('enc') or decrypt ('dec') the message.",
    )
    args = parser.parse_args()
    encrypt = args.mode == "enc"
    if encrypt:
        processed_message = encrypt_message(args.message, args.key)
    else:
        processed_message = decrypt_message(args.message, args.key)
    adjective = "encrypted" if encrypt else "decrypted"
    print(f"The {adjective} message is :\n{processed_message}")
