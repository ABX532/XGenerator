<p align="center">
  <img src="xgenerator.png" width="600">
</p>

# 🔐 XGenerator

![Python](https://img.shields.io/badge/python-3-blue)
![License](https://img.shields.io/badge/license-GPLv3-blue)

A simple, fast, and secure password generator written in Python.

XGenerator allows you to generate strong random passwords using Python's built-in `secrets` module, which is designed for generating cryptographically secure random values.

## ✨ Features

* 🔒 Cryptographically secure password generation
* 🎨 Colored terminal interface
* 📏 Custom password length
* ⚙️ Multiple password generation modes:

  * Uppercase + Lowercase + Numbers + Special Characters *(Recommended)*
  * Uppercase + Lowercase + Numbers
  * Uppercase + Lowercase
  * Uppercase Only
  * Lowercase Only
* 🚀 Lightweight and easy to use
* 📦 No external libraries required

---

## 📷 Preview

```text
██╗  ██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
╚██╗██╔╝██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 ╚███╔╝ ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
 ██╔██╗ ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██╔╝ ██╗╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ 
```

Then simply choose your desired password length and generation mode.

---

## 📥 Requirements

* Python 3 or newer

No additional packages are required.

---

## ▶️ Usage

Clone the repository:

```bash
git clone https://github.com/YourUsername/XGenerator.git
cd XGenerator
```

Run the program:

```bash
python3 xgenerator.py
```

---

## 🔢 Password Modes

| Option | Description                                            |
| ------ | ------------------------------------------------------ |
| 1      | Uppercase + Lowercase + Numbers + Special Characters ⭐ |
| 2      | Uppercase + Lowercase + Numbers                        |
| 3      | Uppercase + Lowercase                                  |
| 4      | Uppercase Only                                         |
| 5      | Lowercase Only                                         |

---

## 🔐 Why `secrets`?

Unlike Python's `random` module, the `secrets` module is specifically designed for generating passwords, authentication tokens, and other security-sensitive data.

---

## 📁 Project Structure

```text
XGenerator/
│
├── xgenerator.py
├── LICENSE
└── README.md
```

---

## 💡 Future Improvements

* [ ] Password strength indicator
* [ ] Copy password directly to clipboard
* [ ] Save generated passwords to a file
* [ ] Custom character exclusions
* [ ] Prevent ambiguous characters (O, 0, l, I)
* [ ] Loop until the user exits
* [ ] Input validation for invalid lengths

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the GPL-3.0 License.

---

## 👤 Author

**ABX**

If you like this project, consider giving it a ⭐ on GitHub!
