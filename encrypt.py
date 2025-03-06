import sys

passkey = None

def vigenere_cipher(text, key, decrypt=False):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    result = []
    index_key = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[index_key].upper()) - ord('A')
            if decrypt:
                new_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A')) 
            else: 
                new_char = chr(((ord(char.upper())- ord('A') + shift) % 26) + ord('A'))
            result.append(new_char.lower() if char.islower() else new_char)
            index_key += 1
        else:
            result.append(char)
    return "".join(result)

def process_command():
    global passkey
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split(" ",1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        match command:
            case "PASS":
                passkey = argument
                print("RESULT")
            case "ENCRYPT":
                if passkey is None:
                    print("ERROR Password not set")
                else:
                    print("RESULT", vigenere_cipher(argument, passkey))
            case "DECRYPT":
                if passkey is None:
                    print("ERROR Password not set")
                else:
                    print("RESULT", vigenere_cipher(argument, passkey, decrypt=True))
            case "QUIT":
                break
            case _:
                print("ERROR Invalid command")

        sys.stdout.flush()

if __name__ == "__main__":
    process_command()
