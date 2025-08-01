# Vault CLI Manual

This manual provides step-by-step instructions to set up and use the Vault CLI with MongoDB logging.

## Installation
1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **(Optional) Start MongoDB**
   - Ensure a MongoDB instance is running locally or provide `MONGODB_URI` in your environment.
3. **Generate your first key pair**
   ```bash
   python vault.py key generate --name "Alice" --email alice@example.com --passphrase secret
   ```

## Basic Usage
- **Create an encrypted note**
  ```bash
  python vault.py note create "hello"
  ```
  The encrypted message is logged to MongoDB.

- **Read a note**
  ```bash
  python vault.py note read note.enc
  ```

- **Send a group message**
  ```bash
  python vault.py group chat dev-team --message "hi"
  ```

- **View recent logs**
  ```bash
  python vault.py log list --last 5
  ```

## Chat Interface
Simply run `python vault.py` to open the interactive interface and follow the menu prompts.
