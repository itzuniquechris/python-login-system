# Simple Login System (Version 1.0)

A secure, terminal-based authentication system built with Python. This project focuses on input validation and security logic for a beginner-friendly user experience.

## 🚀 Features
- **Account Registration:** Validates 4-digit PIN setup with a persistent retry loop.
- **Credential Validation:** Checks for character types (letters/numbers) to prevent crashes.
- **Security Lockout:** Limits the user to exactly 3 failed attempts before a system lockdown.
- **Clean Interface:** Uses F-strings and text formatting for a professional terminal look.

## 🛠️ Python Skills Used
- Nested `while` loops for state management
- `if / elif / else` branching for error handling
- String methods (`.isalpha()`, `.isdigit()`, `.upper()`, `len()`)
- Type conversion and F-string formatting

## 📂 Installation & Usage
1. Clone the repository:
   git clone

2. Run the program:
   python-login_system-v1.py

## 🌱 The Evolution: Version 2.0 (Coming Soon!)
I am currently a Python beginner, but I plan to evolve this project as I learn more. Future upgrades will include:
- **Merging with ATM:** Connecting this login system to the Mini ATM Project.
- **Data Persistence:** Saving user credentials to a local text file.
- **Password Masking:** Hiding characters as the user types their PIN.
- **Reset Feature:** Allowing users to reset their PIN after a successful login.

---
*Created with focus on logical structure and error-free execution.*
