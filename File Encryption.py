from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current directory named `secret.key`
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(encrypted_filename):
    key = load_key()
    f = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open("decrypted_" + encrypted_filename[:-4], "wb") as file:
        file.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    generate_key()  # Uncomment to generate a new key
    # Replace 'sample.txt' with your filename
    encrypt_file("sample.txt")  # Encrypt the file
    decrypt_file("sample.txt.enc")  # Decrypt the file