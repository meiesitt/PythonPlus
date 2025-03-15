# Python+
# RUSSIAN VERSION OF Python+
# V0.0.2
# Библиотека которая немного облегчит жизнь новичкам
# Весь код ниже написан нормально, можете даже посмотреть исходный код если конечно хотите, может что-то новое узнаете ;D

# Модули
import time
import os
import tkinter
import tkinter.messagebox

# Переменные
yap = "Пожалуйста, сначала инициализируйте Python+!\nExplanation: Вы только-что хотели сослаться на функцию из Python+ С самого начала инициализируйте класс, а потом только попробуйте использовать его."

# Исходный код
class PythonPlus:

    _initialized = False
    _logging = False

    _logs = []

    def __init__(self, console_logs: bool = False):
        if not PythonPlus._initialized:
            print("Python+ (v0.0.2) Сделан: @just_dingus#0")
            PythonPlus._initialized = True
            PythonPlus._logging = console_logs

    # AlertsClass

    class Alerts:
        @staticmethod
        def Warning(title: str = "Python+ API Предупреждение", description: str = "Unspecified"):

            """
            Показывает окно предупреждения, метод ОС по умолчанию

            Args:
                title (str): Этот текст будет отображаться в заголовке окна.
                description (str): а вот этот текст будет отображаться внутри окна как содержимое

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showwarning(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Предупреждение - один из аргументов пуст")
        
        @staticmethod
        def Info(title: str = "Python+ API Info Alert", description: str = "Unspecified"):

            """
            Показывает окно оповещения, метод ОС по умолчанию

            Args:
                title (str): Этот текст будет отображаться в заголовке окна.
                description (str): а вот этот текст будет отображаться внутри окна как содержимое

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showinfo(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Предупреждение - один из аргументов пуст")
            
        @staticmethod
        def Error(title: str = "Python+ API Error Alert", description: str = "Unspecified"):

            """
            Показывает окно ошибки, метод ОС по умолчанию

            Args:
                title (str): Этот текст будет отображаться в заголовке окна.
                description (str): а вот этот текст будет отображаться внутри окна как содержимое

            Raises:
                RuntimeWarning: If `title` or `description` was nil
            """

            if title and description:
                tkinter.messagebox.showerror(title=title, message=description)
            else:
                raise RuntimeWarning("Python+ API Предупреждение - один из аргументов пуст")
            
    class AskAlert:

        def AskYesNo(title: str = "Python+ API Вопрос", description: str = "Unspecified"):

            """
            Спрашивает пользователя ОС с кнопками "Да" либо "Нет"

            Args:
                title (str): Этот текст будет отображаться в заголовке окна.
                description (str): а вот этот текст будет отображаться внутри окна как содержимое

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
                raise RuntimeError(f"Произошла ошибка при использывании Python+ AskAlert API\nException: {e}")
            else:
                return x
            
    ####################
    def wait(self, delay: int = 1):

        """
        Задержка на указанное количество секунд

        Args:
            delay (int): Число должно быть больше чем 0

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
            raise ValueError(f"Введенный аргумент \"delay\"не корректный, нужно число больше чем 0 {delay}")
        
    def clear(self):

        """
        Пробует очистить консоль от текста при помощью команд которые специфичные для ОС. 

        Raises:
            RuntimeError: if the operation to clear the screen failed.
        """
        try:
            os.system("cls" if os.name == "nt" else "clear")
        except Exception:
            raise RuntimeError("Не удалось очистить консоль, произошла ошибка.")
