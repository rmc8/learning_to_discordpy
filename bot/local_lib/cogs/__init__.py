import os
from os.path import join, dirname

from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path: str = join(dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print("Set values")
