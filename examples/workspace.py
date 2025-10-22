import os
from settings import ROOT_DIR

print(f"ROOT_DIR from settings.py. {ROOT_DIR}")

dir = os.getenv('VSCODE_WORKSPACE_FOLDER', os.getcwd())
print(f"VSCODE_WORKSPACE_FOLDER: {dir}")

dir = os.getcwd()
print(f"os.getcwd: {dir}")

dir = os.path.dirname(os.path.abspath(__file__))
print(f"os.path.dirname(os.path.abspath): {dir}")

dir = os.path.dirname(__file__)
print(f"os.path.dirname: {dir}")

dir = os.path.abspath(__file__)
print(f"os.path.abspath: {dir}")

