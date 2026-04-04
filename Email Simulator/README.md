# 📧 Email Simulator

A lightweight Python program that simulates a basic email system — send, receive, read, and delete emails between users.

**Created by:** C.K Baloyi  
**Date:** 2026-03-24

---

## Features

- Send emails between users
- Receive and store emails in a personal inbox
- List all emails with read/unread status
- Read individual emails (auto-marked as read)
- Delete emails from the inbox

---

## Project Structure

```
email-simulator.py
```

The project is contained in a single file with three core classes:

| Class   | Description                                              |
|---------|----------------------------------------------------------|
| `Email` | Represents a single email with sender, receiver, subject, body, timestamp, and read status |
| `Inbox` | Manages a collection of emails — list, read, and delete  |
| `User`  | Represents a user who can send emails and owns an inbox  |

---

## Getting Started

### Prerequisites

- Python 3.x (no external dependencies required)

### Running the Program

```bash
python email-simulator.py
```

This runs the built-in `main()` demo, which simulates two users exchanging emails and performing inbox operations.

---

## Usage Example

```python
from email_simulator import User

# Create users
alice = User('Alice')
bob = User('Bob')

# Send an email
alice.send_email(bob, 'Hello!', 'Hi Bob, just checking in.')

# Check inbox
bob.check_inbox()

# Read the first email
bob.read_email(1)

# Delete the first email
bob.delete_email(1)
```

### Sample Output

```
Email sent from Alice to Bob!

Bob's Inbox:
Your Emails:
1. [Unread] From: Alice | Subject: Hello! | Time: 2026-03-24 10:00

--- Email ---
From: Alice
To: Bob
Subject: Hello!
Received: 2026-03-24 10:00
Body: Hi Bob, just checking in.
------------

Email deleted.

Bob's Inbox:
Your inbox is empty.
```

---

## Class Reference

### `Email(sender, receiver, subject, body)`
| Method                | Description                            |
|-----------------------|----------------------------------------|
| `mark_as_read()`      | Marks the email as read                |
| `display_full_email()`| Prints the full email and marks as read|
| `__str__()`           | Returns a summary line for inbox listing|

### `Inbox()`
| Method                  | Description                                      |
|-------------------------|--------------------------------------------------|
| `receive_email(email)`  | Adds an email to the inbox                       |
| `list_emails()`         | Displays a summary of all emails                 |
| `read_email(index)`     | Reads and displays the email at the given position (1-based) |
| `delete_email(index)`   | Deletes the email at the given position (1-based)|

### `User(name)`
| Method                              | Description                            |
|-------------------------------------|----------------------------------------|
| `send_email(receiver, subject, body)`| Sends an email to another user        |
| `check_inbox()`                     | Displays inbox summary                 |
| `read_email(index)`                 | Reads an email from the inbox          |
| `delete_email(index)`               | Deletes an email from the inbox        |

---

## Notes

- Emails are stored in memory only — they are not persisted between runs.
- Email indices in `read_email()` and `delete_email()` are **1-based** (as displayed in the inbox list).
- Timestamps are recorded at the moment of sending using `datetime.datetime.now()`.

---

## License

This project is for educational purposes.
