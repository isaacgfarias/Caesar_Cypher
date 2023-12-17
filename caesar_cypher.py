import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


ALPH_SIZE = 26

# ord('a') = 97
# ord('A') = 65


def shift_letter(letter, key):
    if letter.isalpha:
        base = ord('a') if letter.islower else ord('A')
        return chr((ord(letter) - base + key) % ALPH_SIZE + base)


def crypt(word, key):
    return "".join(shift_letter(w, key) for w in word)


def decrypt(word, key):
    return "".join(shift_letter(w, -key) for w in word)


def right_input(prompt, *options):
    while True:
        user_input = input(prompt)
        if any(str(user_input) == str(option) for option in options):
            return user_input
        print("Insira", " ou ".join(map(str, options)))


def caesar_cypher():
    crypted, decrypted = [], []
    while True:
        clear_console()

        task = int(right_input(
            "Do you want to:\n\t1 - Crypt\n\t2 - Decrypt\n\t3 - Quit\n", 1, 2, 3))
        match task:
            case 1:
                crypted.append(crypt(input("What word do you want to encode? "),
                      int(input("Type the cryption's key. "))))
            case 2:
                decrypted.append(decrypt(input("What word do you want to encode? "),
                      int(input("Type the cryption's key. "))))
            case 3:
                print(f'Crypted:', ', '.join(word for word in crypted))
                print(f'Decrypted:', ', '.join(word for word in decrypted))
                break


caesar_cypher()
