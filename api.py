# Python+
# Library designed to make life easier for beginners.
# All below code is unobfuscated. If you wish, you may review the source. Who knows? You might learn something :D

# Modules
import time
import os
import tkinter
import tkinter.messagebox

# Variables
yap = "Please initialize Python+ first!\nExplanation: You just tried to reference a function from Python+ library's class directly. First, initialize class and then try to use its methods."

# Source
class PythonPlus:

    _initialized = False
    _logging = False

    _logs = []

    def __init__(self, console_logs: bool = False):
        if not PythonPlus._initialized:
            print("Python+ (v0.0.2) by @just_dingus#0")
            PythonPlus._initialized = True
            PythonPlus._logging = console_logs

    # AlertsClass

    class Alerts:
        @staticmethod
        def Warning(title: str = "Python+ API Warning Alert", description: str = "Unspecified"):

            """
            Shows a warning alert window using the default OS method

            Args:
                title (str): Text that will be displayed on the title section of the window.
                description (str): Text that will be displayed on the content section of the window.

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showwarning(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Warning - one of args was empty")
        
        @staticmethod
        def Info(title: str = "Python+ API Info Alert", description: str = "Unspecified"):

            """
            Shows an info alert window using the default OS method

            Args:
                title (str): Text that will be displayed on the title section of the window.
                description (str): Text that will be displayed on the content section of the window.

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showinfo(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Warning - one of args was empty")
            
        @staticmethod
        def Error(title: str = "Python+ API Error Alert", description: str = "Unspecified"):

            """
            Shows an error alert window using the default OS method

            Args:
                title (str): Text that will be displayed on the title section of the window.
                description (str): Text that will be displayed on the content section of the window.

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showerror(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Warning - one of args was empty")
            
    class AskAlert:

        def AskYesNo(title: str = "Python+ API Question", description: str = "Unspecified"):

            """
            Asks a question to the OS user with an UI prompt, specifically with Yes/No options

            Args:
                title (str): Text that will be displayed on the title section of the window.
                description (str): Text that will be displayed on the content section of the window.

            Returns:
                True: If user clicks "Yes"
                False: If user clicks "No"
                None: If user manages to somehow cancel the question window

            Raises:
                RuntimeWarning: If `title` or `description` was nil or the question ask operation failed.
            """

            x = None
            try:
                x = tkinter.messagebox.askyesno(title=title, message=description)
            except Exception as e:
                raise RuntimeError(f"Ran into an error while using Python+ AskAlert API\nException: {e}")
            else:
                return x
            
    ####################
    def wait(self, delay: int = 1):

        """
        Delays the thread that executed this function for the specified amount of seconds.

        Args:
            delay (int): The number of seconds to delay the execution for. Must be greater than 0.

        Raises:
            ValueError: If `delay` is not a positi  ve integer.
        
        """

        # Check for initialization
        if not PythonPlus._initialized:
            raise RuntimeError(yap)
        
        # Simple code
        if isinstance(delay, int) and delay > 0:
            time.sleep(delay)
        else:
            raise ValueError(f"Entered argument \"delay\" is invalid. Expected an integer thats above zero, got {delay}")
        
    def clear(self):

        """
        Attempts to clear the console window of text using OS-specific commands.

        Raises:
            RuntimeError: if the operation to clear the screen failed.
        """
        try:
            os.system("cls" if os.name == "nt" else "clear")
        except Exception:
            raise RuntimeError("Failed at attempt of clearing console screen - an error occurred.")
