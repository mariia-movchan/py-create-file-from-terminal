import sys
import os
from datetime import datetime


def create_directory(path: list) -> None:
    os.mkdir("/".join(path))


def create_file(file_name: str) -> None:
    content = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content.append(content_line)

    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%y-%m-%d %H:%M:%S')}\n")

        for idx, line in enumerate(content):
            file.write(f"{idx + 1} {line}\n")


def create_file_from_terminal() -> None:
    command = sys.argv[1:]
    directory_name = command[1:command.index("-f")]
    file_name = command[-1]

    if "-d" in command and "-f" not in command:
        create_directory(directory_name)
    elif "-d" not in command and "-f" in command:
        create_file(file_name)
    elif "-d" in command and "-f" in command:
        create_directory(directory_name)
        create_file(file_name)


create_file_from_terminal()
