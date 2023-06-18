"""
Qubic
~~~~~

Author: Valentin
Description: Executable compiler
"""
import PyInstaller.__main__
import os
import shutil


if __name__ == "__main__":

    shutil.rmtree(r".\build", ignore_errors=True)
    shutil.rmtree(r".\dist", ignore_errors=True)
    
    PyInstaller.__main__.run([  
        "--onefile",
        "--windowed",
        "--noconsole",
        "--clean",
        "--name", "Qubic",
        "--icon", r".\src\assets\icon.ico",
        os.path.join(os.getcwd(), r".\src\main.py")
    ])

    shutil.copytree(r".\src\assets", r".\dist\assets", dirs_exist_ok=True)