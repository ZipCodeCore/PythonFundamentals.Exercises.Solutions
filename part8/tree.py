import os


def walk(dirname, file_handler):
    items = os.listdir(dirname)
    for item in items:
        path = os.path.join(dirname, item)

        if os.path.isfile(path):
            file_handler.write(path+"\n")
        else:
            walk(path, file_handler)


if __name__ == '__main__':
    with open("log.txt", "w") as file_handler:
        walk(".", file_handler)
