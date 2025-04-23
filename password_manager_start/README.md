# 🔐 Password Manager – Python Tkinter Project

This is a simple yet functional **Password Manager Desktop App** built using Python's `tkinter` GUI library. It includes the following features:
- Password generation
- Secure storage (locally in a JSON file)
- Password retrieval via search
- Clipboard copy of generated passwords

---

### 🚀 Features

- Generate strong, random passwords
- Save passwords with associated websites and emails/usernames
- Search and retrieve saved credentials
- Automatically copy generated password to clipboard
- Error handling and data validation
- All data stored locally in `data.json`

---

### 💠 Technologies Used

- **Python 3**
- `tkinter` for GUI
- `json` for structured data storage
- `random` for password generation
- `pyperclip` to copy password to clipboard

---

## 📂 File Structure

```
password_manager/
|
|├— main.py             # Main application script
|├— logo.png            # Logo image for the GUI
|├— data.json           # JSON file to store credentials (auto-created)
└— README.md           # Project documentation
```

---

## 📜 How It Works

### 1. **UI Layout**
The GUI is built using `tkinter`:
- A logo image on top.
- Input fields for Website, Email/Username, and Password.
- Buttons to **Generate Password**, **Add**, and **Search**.

### 2. **Password Generator Function**

```python
def generate_password():
```
- Uses random `letters`, `numbers`, and `symbols`.
- Creates a strong password of length 12–16.
- Shuffles the characters.
- Inserts the password into the Password field.
- Copies it to clipboard using `pyperclip.copy()`.

---

### 3. **Saving Data to File**

```python
def save():
```

- Retrieves input from Website, Email, and Password fields.
- Validates that Website and Password fields are not empty.
- Loads existing data from `data.json` if it exists.
- Adds the new entry without deleting old data.
- Saves the updated dictionary back to `data.json`.
- Clears the Website and Password fields after saving.

Handles:
- `FileNotFoundError`: if file does not exist
- `JSONDecodeError`: if the file is empty or corrupted

---

### 4. **Searching for a Saved Password**

```python
def find_password():
```

- Gets the website name from the entry.
- Looks it up in `data.json`.
- If found, displays the stored email and password in a popup.
- If not found, shows an appropriate error.

Handles:
- `FileNotFoundError`: if `data.json` doesn’t exist

---

## 🧪 Sample Data Structure (`data.json`)

```json
{
  "amazon.com": {
    "email": "user@amazon.com",
    "password": "Ab1@xyz123"
  },
  "google.com": {
    "email": "me@gmail.com",
    "password": "StrongPass#456"
  }
}
```

---

## 🖼️ GUI Preview

> 💡 _Make sure `logo.png` is present in the same directory to load the image correctly._

---

## ✅ To Run the App

1. Install Python and required packages:

```bash
pip install pyperclip
```

2. Run the Python script:

```bash
python main.py
```

---

## 🔒 Security Notes

- All credentials are stored **locally** in `data.json` in plain text.
- For real-world applications, consider encrypting the file or integrating with a secure vault.

---

## 📌 Future Improvements (Ideas)

- Add encryption for stored passwords
- Integrate with cloud storage (e.g., Firebase or SQLite DB)
- Add a master password for accessing the app
- Support export/import of saved data

---

## 👩‍💼 Author

Created by **[Your Name Here]**  
A beginner-friendly project to practice GUI development and file handling in Python.

---

