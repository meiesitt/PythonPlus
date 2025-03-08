# Python+  
Python+ is a beginner-friendly library designed to simplify coding. It includes useful functions like `wait()` and `clear()` to reduce repetitive tasks.  
Why do extra work when Python+ can handle it for you? Simply download the latest release, add the Python file to your project directory, import it, and start coding!

## 🎯 Our Goal  
Python+ provides multiple useful functions, with frequent updates introducing new ones. Our goal is to help keep your code clean, efficient, and reliable. With built-in error handling, we ensure that you won't run into unexpected issues.  

Additionally, Python+ is **completely open-source**, meaning anyone can review the `api.py` file and understand how it works. Transparency is key to maintaining trust and security.  

## 📃 Prerequisites  
Each release specifies the Python version it was tested with. Since Python evolves with each update, we strive to use the **latest stable version** to ensure compatibility with modern Python projects.  

## 🔒 Safe & Transparent Code  
As the sole developer of Python+ (for now), I promise to do my best when updating this library. **Python+ will never contain malicious code**—you are free to inspect the source yourself.  

I apologize if parts of the code lack comments; I sometimes forget to add them while coding. However, I will improve documentation over time.  

## 📕 Fully Documented with Docstrings  
Every function in Python+ includes **docstrings**, so your IDE will provide helpful information when you reference them.

## ⬇ Get Python+  
You can download the latest release of Python+ **[here](https://github.com/meiesitt/PythonPlus/releases)**. Each release includes the Python version it was tested with.

## ⚙ View the Source Code  
Want to explore Python+'s inner workings? You can **[view the `api.py` source code here](https://github.com/meiesitt/PythonPlus/blob/main/api.py).**

---

# ✅ How to Use Python+  
## Step 1: Download Python+  
**[Click here](https://github.com/meiesitt/PythonPlus/releases)** to download the latest release. The file will always be updated to the latest version of Python+.

## Step 2: Add Python+ to Your Project  
Move the downloaded file into your project directory. You can rename it if needed.

## Step 3: Import Python+  
```py
from api import PythonPlus
```
⚠ **Note:** If you renamed the file, update `api` in the import statement to match the new filename (excluding `.py`).  

## Step 4: Initialize Python+  
To use Python+ functions, you need to **initialize** the library first:  
```py
from api import PythonPlus

PyPlus = PythonPlus()
```
If everything is set up correctly, you should see:  
```
Python+ (v0.0.2) by @just_dingus#0
```
This confirms that Python+ has been successfully initialized.

---

# 📝 Example Usage  
The following example asks the user if today is Monday:  
```py
from api import PythonPlus
PyPlus = PythonPlus()

answer = PyPlus.AskAlert.AskYesNo("Question for you", "Is today Monday?")

if answer:
    print("User agrees that it may be Monday")
else:
    print("User does not think it's Monday.")
```
Pretty simple, right?  

More functions are being added frequently, so be sure to **check for updates regularly**!
