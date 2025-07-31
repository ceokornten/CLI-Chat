# Secure CLI Vault

This project provides a command-line interface for creating and managing encrypted notes and files. It uses PGP for asymmetric encryption and Fernet for password-based encryption. A Node.js backend will be added in the future.

## Requirements
- Python 3.11+
- `pgpy` and `cryptography`

## Usage
Install dependencies:
```
pip install -r requirements.txt
```

Generate a keypair (to be implemented) and run:
```
python vault.py note create "My secret"
python vault.py note read note.enc
```
