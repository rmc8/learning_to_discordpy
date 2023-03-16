import os


class DockerFile:
    path: str = "./Dockerfile"
    encoding: str = "utf-8"

    def read(self) -> str:
        with open(self.path, mode="r", encoding=self.encoding) as f:
            return f.read()

    def write(self, query: str):
        with open(self.path, mode="w", encoding=self.encoding) as f:
            print(query, file=f)


def main():
    df = DockerFile()
    query: str = df.read()
    new_query: str = query.replace(
        "<<TOKEN>>",
        os.getenv("DISCORD_BOT_TOKEN"),
    )
    df.write(new_query)


if __name__ == "__main__":
    main()
