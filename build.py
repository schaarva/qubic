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
    
    PyInstaller.__main__.run([  
        "--onefile",
        "--windowed",
        "--noconsole",
        "--clean",
        "--name", "Qubic",
        os.path.join(os.getcwd(), r".\src\main.py")
    ])

    shutil.copytree(r".\src\assets", r".\dist\assets", dirs_exist_ok=True)