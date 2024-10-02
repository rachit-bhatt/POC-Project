# File Encryption and Decryption POC

## Overview

This is a proof of concept (POC) project that demonstrates file encryption and decryption using Python. It utilizes the `cryptography` library to securely encrypt and decrypt files, providing a simple way to protect sensitive data.

## Features

- **Generate Encryption Key**: Automatically generates a unique key for file encryption.
- **Encrypt Files**: Encrypts specified files, making their contents unreadable without the key.
- **Decrypt Files**: Decrypts previously encrypted files to restore their original content.

## Prerequisites

- Python 3.x
- `cryptography` library

## Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd file_encryption
   ```

2. **Install Dependencies**:

    ```bash
    pip install cryptography
    ```

### Usage:
1. **Generate Key:** Uncomment the `generate_key()` line in the main script to create a new encryption key.
2. **Encrypt a File:** Modify the `encrypt_file("sample.txt")` line to specify the file you want to encrypt.
3. **Decrypt a File:** Modify the `decrypt_file("sample.txt.enc")` line to specify the encrypted file you want to decrypt.

## Sample Files:
- `sample.txt`: A sample text file containing the messsage to be encrypted.
- `secret.key`: The generated key file used for encryption and decryption.

## Running the Project:

Run the script to encrypt and decrypt files:
    
    ```bash
    python file_encryption.py
    ```

## Important Notes:
- Ensure the `secret.key` file is kept safe; losing this file will result in permanent loss of access to encrypted files.
- This POC is intended for educational purposes. Do not use for production-level security without further enhancements and security measures.

## Code:

    ```python
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
    ```

## License:

This project is an open-source project.