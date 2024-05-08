# Encryption and Decryption Tool
This script provides a command-line interface for encrypting and decrypting files using AES encryption.

## Background
### AES (Advanced Encryption Standard)
AES (Advanced Encryption Standard) is a symmetric encryption algorithm that is widely adopted due to its security and efficiency.
### CBC and CTR
- **CBC (Cipher Block Chaining):** CBC is a block cipher mode of operation that XORs each plaintext block with the previous ciphertext block before encryption.
- **CTR (Counter):** CTR mode is a block cipher mode of operation that turns a block cipher into a stream cipher. It generates a stream of key-dependent values by encrypting a counter value and XORing it with the plaintext to produce ciphertext.
### Keys and IVs
Encryption keys are used to encrypt and decrypt data securely. They must be kept confidential and should be chosen randomly for maximum security. 
Initialization vectors (IVs) are used to randomize the encryption process and ensure that the same plaintext encrypted with the same key produces different ciphertexts.

## Features
- Encrypt files using AES encryption with CBC or CTR mode.
- Generate random encryption keys and IVs for secure encryption.
- Save encryption keys and IVs to separate files for future decryption.
- Decrypt encrypted files with the correct key and initialization vector (IV).

## Installation
1. Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/encryption-decryption.git
```
2. Navigate to the project directory:
```bash
cd encryption-decryption
```
3. Install required dependencies using [pip](https://pip.pypa.io/en/stable/):
```bash
pip install -r requirements.txt
```

## Usage
1. Run the 'main.py' script:
```bash
python main.py
```
2. Follow the prompts to select an action (encrypt or decrypt), enter your filename, and choose the AES mode (CBC or CTR).
3. If encrypting, the script will generate a random encryption key and IV, save them to a separate file, and encrypt the selected file.
4. If decrypting, provide the name of the key and IV file generated during encryption.
5. View the decrypted content if desired.

## Unit Tests
Unit tests are included to ensure the correctness of the encryption and decryption functionality. To run tests, execute the following command:
```bash
python -m unittest test_encrypt_decrypt.py
```

## Author

[Arianna Luis](https://github.com/ariannaluis)































