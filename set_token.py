import os
from os.path import join, dirname


def write_val(val):
    dotenv_path: str = join(dirname(__file__), ".env")
    with open(dotenv_path, "a", encoding="utf-8") as f:
        print(val, file=f)


def main():
    if token := os.getenv("DISCORD_BOT_TOKEN"):
        write_val(f"TestBotPythonDevToken={token}")
    print("[set_token.py] Done")


if __name__ == "__main__":
    main()
