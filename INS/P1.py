# Substitution Cipher
# !pip install IPython

from IPython import get_ipython
from IPython.display import display

class SubstitutionCipher:
    def __init__(self, key):
        self.shift = ord(key[0].lower()) - ord('a')

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    encrypted_text += chr((ord(char) - ord('a') + self.shift) % 26 + ord('a'))
                else:
                    encrypted_text += chr((ord(char) - ord('A') + self.shift) % 26 + ord('A'))
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr((ord(char) - ord('a') - self.shift) % 26 + ord('a'))
                else:
                    decrypted_text += chr((ord(char) - ord('A') - self.shift) % 26 + ord('A'))
            else:
                decrypted_text += char
        return decrypted_text

# Example Usage
key = "bcde"
plaintext = "abcdefghijklmnopqrstuvwxyz"
sub_cipher = SubstitutionCipher(key)
encrypted_message = sub_cipher.encrypt(plaintext)


# Transposition Cipher
# !pip install IPython

from IPython import get_ipython
from IPython.display import display

class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        num_columns = len(self.key)
        num_rows = len(plaintext) // num_columns + (1 if len(plaintext) % num_columns != 0 else 0)

        # Fill matrix row-wise
        matrix = [[''] * num_columns for row in range(num_rows)]
        for i, char in enumerate(plaintext):
            row = i // num_columns
            col = i % num_columns
            matrix[row][col] = char

        # Read matrix column-wise based on key
        encrypted_text = ""
        for digit in sorted([(int(k), i) for i, k in enumerate(self.key)]):  # sort key in numerical order e.g. 12345
            col_index = digit[1]
            for row in matrix:
                if row[col_index]:
                    encrypted_text += row[col_index]

        return encrypted_text

    def decrypt(self, ciphertext):
        num_columns = len(self.key)
        num_rows = len(ciphertext) // num_columns + (1 if len(ciphertext) % num_columns != 1 else 0)
        total_cells = num_columns * num_rows
        padding = total_cells - len(ciphertext)

        key_tuples = sorted([(int(k), i) for i, k in enumerate(self.key)])
        col_lengths = [num_rows] * num_columns

        # Some cols will have one less character
        for i in range(padding):
            col_index = key_tuples[-(i+1)][1]
            col_lengths[col_index] -= 1

        matrix = [[''] * num_columns for row in range(num_rows)]
        index = 0
        for i, col_index in key_tuples:
            for row in range(col_lengths[col_index]):
                matrix[row][col_index] = ciphertext[index]
                index += 1
        decrypted_text = ''.join(''.join(row) for row in matrix)
        return decrypted_text

key = "4312567"
cipher = TranspositionCipher(key)
message = "ABCDEFG"

em = cipher.encrypt(message)
dm = cipher.decrypt(message)

print("Original:", message)
print("Encrypted:", em)
print("Decrypted:", dm)
decrypted_message = sub_cipher.decrypt(encrypted_message)

print("Original:", plaintext)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
