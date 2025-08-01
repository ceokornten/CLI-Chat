# Secure CLI Vault

This project provides a command-line interface for creating and managing encrypted notes and files. It uses PGP for asymmetric encryption and Fernet for password-based encryption. Group chat and group management are also supported. A Node.js backend will be added in the future.

See [docs/USAGE.md](docs/USAGE.md) for a step-by-step guide.

## Requirements
- Python 3.11+
- `pgpy` and `cryptography`

## Usage
Install dependencies:
```bash
pip install -r requirements.txt
```

Start the interactive chat assistant:
```bash
python vault.py
```

Generate a keypair and create a note:
```bash
python vault.py key generate --name "User" --email user@example.com --passphrase yourpass
python vault.py note create "My secret"
python vault.py note read note.enc
python vault.py note share "hello team" --recipients user1_pub.asc user2_pub.asc
python vault.py key list
python vault.py group create dev-team
python vault.py group add-member dev-team user1_pub.asc
python vault.py group chat dev-team --message "Hi team"
```
