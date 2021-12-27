from watcher import Watcher


def main():
    watcher = Watcher()
    print("Buscando Partida . . .")
    while True:
        watcher.watch()


if __name__ == "__main__":
    main()
