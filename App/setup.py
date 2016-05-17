application_title = "TCM"
main_python_file = "Main.py"

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re", "PyQt4", "sip", "PyQt4.QtCore", "src/TCM/TCM.py"]

setup(
        name = application_title,
        version = "0.1",
        description = "TCM",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)])
