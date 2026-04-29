# Password Manager

A command-line password manager built in Python that securely encrypts and stores your passwords using the `cryptography` library's Fernet symmetric encryption.

---

## Features

- **AES Encryption** — Passwords are encrypted using Fernet (AES-128-CBC) before being written to disk
- **Password Strength Checker** — Rates passwords as Weak, Moderate, or Strong with improvement suggestions
- **Key Management** — Generate or load encryption keys; only one key can be active at a time
- **Password File Management** — Create or load password files, with safeguards against accidental overwrites
- **Full CRUD** — Add, retrieve, list, and delete passwords
- **Secure Input** — Passwords are entered via hidden input (no echo to terminal)

---

## Requirements

- Python 3.7+
- [`cryptography`](https://pypi.org/project/cryptography/) library

Install the dependency with:

```bash
pip install cryptography
```

---

## Usage

Run the program:

```bash
python main.py
```

You will be presented with the interactive menu:

```
What do you want to do?
  (1) Create a new key
  (2) Load an existing key
  (3) Create new password file
  (4) Load existing password file
  (5) Add a new password
  (6) Get a password
  (7) List all passwords
  (8) Delete a password
  (9) Quit (q)
```

---

## Getting Started

Follow these steps in order on first use:

### Step 1 — Create or load a key
Choose **(1)** to generate a new encryption key and save it to a file:
```
Enter path: mykey.key
```
>  Keep this key file safe. Losing it means losing access to all your stored passwords.

### Step 2 — Create or load a password file
Choose **(3)** to create a new password file:
```
Enter path: passwords.txt
```

### Step 3 — Add passwords
Choose **(5)**, enter the site name, then type your password (input is hidden).  
The strength checker will rate your password and offer suggestions if it's weak.

### Step 4 — Retrieve passwords
Choose **(6)** and enter the site name to view the decrypted password.

---

## Password Strength Criteria

A password is scored on five criteria:

| Criterion              | Requirement                        |
|------------------------|------------------------------------|
| Length                 | At least 8 characters              |
| Uppercase letters      | At least one (A–Z)                 |
| Lowercase letters      | At least one (a–z)                 |
| Numbers                | At least one (0–9)                 |
| Special characters     | At least one (`!@#$%^&*` etc.)     |

| Score | Rating   |
|-------|----------|
| 5/5   | STRONG   |
| 3–4/5 | MODERATE |
| 0–2/5 | WEAK     |

Weak passwords trigger a confirmation prompt before being saved.

---

## File Format

Passwords are stored in a plain-text file, one entry per line, in the format:

```
site:encrypted_password
```

The password is encrypted using the loaded Fernet key before being written — the file is unreadable without the corresponding key.

---

##  Important Notes

- **One key at a time** — Creating a new key replaces the current key in memory. A password file encrypted with a different key cannot be decrypted.
- **Back up your key file** — There is no way to recover passwords if the key file is lost.
- **Overwrite protection** — When creating a password file that already exists, the program will warn you and ask for confirmation before overwriting or deleting existing data.

---

## Project Structure

```
.
├── main.py          # Main application file
├── mykey.key        # Generated encryption key (created at runtime)
└── passwords.txt    # Encrypted password storage (created at runtime)
```

---

## License

This project is for personal/educational use. No warranty is provided.
