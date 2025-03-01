import sys

passkey = None

def vigenere_cipher(text, key, decrypt=False):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    result = []
    for t,k in zip(text, key):
        shift = ord(k) - ord('A')
        new_char = chr((ord(t) - ord('A') - shift) % 26 + ord('A')) if decrypt else ((ord(t) - ord('A') + shift) % 26 + ord('A'))
        result.append(new_char)
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
                    print("RESULT", vigenere_cipher(argument, passkey))
            case "QUIT":
                break
            case _:
                print("ERROR Invalid command")

        sys.stdout.flush()

if __name__ = "__main__":
    process_command()
