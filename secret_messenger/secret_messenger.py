import os

DATA_FILE = "data/message.txt"

def encode_message(message, key):
    encoded = ""
    for ch in message:
        encoded += hex(ord(ch) + key)[2:] + " "
    return encoded.strip()

def decode_message(encoded, key):
    key = int(key)
    decoded = ""
    parts = encoded.split()
    for p in parts:
        num = int(p, 16) - key
        decoded += chr(num)
    return decoded

def save_message(encoded):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(encoded + "\n")

def show_saved_message():
    if not os.path.exists(DATA_FILE):
        print("No message saved")
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        print("\nSaved Messages are")
        print("-----------------------------------")
        print(f.read())

def main():
    print("""
======================================

   Welcome to my Secret Messenger Console

======================================

1) Encode a secret message
2) Decode a secret message
3) View saved encrypted message
4) Exit

""")
    while True:
        choice = input("Choose an option (1 to 4): ")

        if choice == "1":
            msg = input("Enter your message here: ")
            key = int(input("Enter secret key (numbers only): "))
            encoded = encode_message(msg, key)
            print("\nEncoded:", encoded)
            save_message(encoded)
            print("Message Saved\n")

        elif choice == "2":
            encode = input("Enter the encoded text: ")
            key = input("Enter the key which you used to save it: ")
            decoded = decode_message(encode, key)
            print("\nDecoded:", decoded, "\n")

        elif choice == "3":
            show_saved_message()

        elif choice == "4":
            print("BYE, Good BYE.......")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
