# CLI Vault Manual

This guide explains how to set up the environment and use the CLI vault along with the placeholder backend.

## Prerequisites
- **Python 3.11+**
- **Node.js 20+**
- Optional: MongoDB if you plan to extend the backend

## Setup
1. Clone this repository and navigate into the project directory.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Node.js dependencies for the backend:
   ```bash
   cd backend
   npm install
   cd ..
   ```
4. Start the backend server (optional for local testing):
   ```bash
   node backend/server.cjs
   ```

## Generating PGP Keys
Use the built‑in `key` command to generate a key pair. You will be prompted for a name, email and passphrase.
```bash
python vault.py key generate --name "Alice" --email alice@example.com --passphrase mysecret
```
Keys are stored in the `keys/` directory and ignored by git.

## Working with Notes
Create an encrypted note and save it locally:
```bash
python vault.py note create "My secret note"
```
The encrypted file is written to `note.enc`.

Read and decrypt the note:
```bash
python vault.py note read note.enc
```

### Sharing notes with multiple recipients

Use the `share` command and supply one or more public key files:

```bash
python vault.py note share "hello team" --recipients user1_pub.asc user2_pub.asc
```

## Managing Keys

List keys stored in the `keys/` directory:

```bash
python vault.py key list
```

Import an additional key file:

```bash
python vault.py key import another_pub.asc
```

Delete an unwanted key:

```bash
python vault.py key delete user2_priv.asc
```

## File and Group Commands
The `file` and `group` command groups exist but contain placeholders. They will eventually support uploading encrypted files and managing collaboration groups.

## Additional Help
Run `python vault.py --help` to see the available command groups and options.
