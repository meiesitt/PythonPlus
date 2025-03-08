# Python+
Python+ is an amazing library to put into your project for beginners. It contains multiple functions like `wait()` or `clear()`.
Why do extra work if you can let Python+ do the heavylifting? Download the latest release and simply add the Python file to your project directory. Import it and enjoy!

## 🎯 Our aim
Python+ contains multiple useful functions, with newer additions being added frequently. Our aim is to help keep your code clean while also ensuring reliability. With good error handling, we can guarantee that you will not run into problems with our library.
Additionally, Python+ is completely open-source, meaning you can happily view the source of `api.py` and discover how Python+ works.
We like to keep our code open so we can guarantee the safety of our library.

## 📃 Prerequisites
As for the possible version of Python needed, each release has the version of Python used noted in the description of each release.
The way Python works is slightly changed almost every version of Python, so to ensure your projects don't suddenly stop working when using Python+, we will try our best to use the newest versions of Python.

## 🔒 Safe Code
I, as of writing this as the sole developer of Python+, will promise to you to use the best of my abilities when updating Python+. I will never include possibly malicious code, which can be checked by anyone. I apologize if the code is not readable, I rarely remember to include comments while working on code.

## 📕 Documented with docstrings
All functions of Python+ are well documented with docstrings. Depending on the IDE you use, it should show when referencing a function.

## ⬇ Get Python+
You can get latest release of Python+ <a href="https://github.com/meiesitt/PythonPlus/releases">by clicking here.</a> You can choose release of your choice, noted with Python version.

## ⚙ Source of Python+
Alternatively, if you want to learn more about Python+ and its inner workings, you can <a href="https://github.com/meiesitt/PythonPlus/blob/main/api.py">click here to visit the api.py source.</a>

# ✅ How to use Python+
## Step 1. Download Python+ API
You can <a href="https://github.com/meiesitt/PythonPlus/blob/main/api.py">the latest release by clicking here.</a> This is automatically updated to include the latest version of Python+

## Step 2. Put the Python+ API file into your project directory
Move the file into your project directory. You may name it as whatever you want.

## Step 3. Reference it in your project
```py
from api import PythonPlus
```
⚠ Warning: If you have changed the name of the API file, also change the `api` bit in the above code. In Python, you can import any module or file by just referencing its actual file name. You can think of it as just putting the file name there but excluding the .py part of it.

## Step 4. Make a Python+ Variable
If you want to use the functions or methods inside Python+ API, you must first initialize the API. Here's how:
```py
from api import PythonPlus

PyPlus = PythonPlus()
```
If you have done everything correctly, you should see a `Python+ (v0.0.2) by @just_dingus#0` line in the console. If so, PythonPlus has been initialized and is ready to be used in your project.

# Example usage
The below code asks the user if they think today is, for example, Monday.
```py
from api import PythonPlus
PyPlus = PythonPlus()

answer = PyPlus.AskAlert.AskYesNo("Question for you", "Is today Monday?")

if answer:
  print("User agrees that it may be Monday")
else:
  print("User does not think that it's Monday.")
```
Very simple, right?
And ofcourse there are many more functions, being added frequently. Make sure to frequently check for updates.
