import os


def write_val(val):
    with open(".env", "a", encoding="utf-8") as f:
        print(val, file=f)


def main():
    if token := os.getenv("DISCORD_BOT_TOKEN"):
        write_val(f"TestBotPythonDevToken={token}")


if __name__ == "__main__":
    main()
