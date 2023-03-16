import os


def get_token() -> str:
    if token := os.getenv("TestBotPythonDevToken"):
        return token
    with open("token", "r", encoding="utf-8") as f:
        return f.read().strip()