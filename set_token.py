import os


def main():
    with open("token", "w", encoding="utf-8") as f:
        print(os.getenv("DISCORD_BOT_TOKEN"), file=f)


if __name__ == "__main__":
    main()
