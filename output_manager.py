from pathlib import Path


class OutputManager:
    def __init__(self):
        self.__file_path = "output_dirs.txt"
        doc = Path(self.__file_path)
        if not doc.is_file():
            try:
                open(self.__file_path, 'x')
            except IOError:
                print("Unhandled IO Error")

    def add_path(self, path, name):
        doc = open(self.__file_path, 'a')
        doc.write("Name:{} | Path:{}".format(name, path) + "\n")
        doc.close()
        print("-- Name : {} | Path : {}".format(name, path))

    def remove_path(self, path):
        doc = open(self.__file_path, 'r')
        paths = doc.readlines()
        doc.close()

        removed = False
        for p in paths:
            if p[p.index('| Path:') + 7:] == path:
                removed = True
                path = p
                break

        if not removed:
            print("> Could not find path <")
            return

        paths.remove(path)
        doc = open(self.__file_path, 'w')
        for p in paths:
            doc.write(p + "\n")
        doc.close()

    def clear(self):
        doc = open(self.__file_path, 'w')
        doc.close()

    def list(self):
        doc = open(self.__file_path, 'r')
        paths = doc.readlines()
        print()
        for path in paths:
            print(path)
        doc.close()

    def get_paths(self):
        doc = open(self.__file_path, 'r')
        doc_paths = doc.readlines()
        doc.close()
        paths = []
        for path in doc_paths:
            if len(path) > 3:
                paths.append(path[path.index('| Path:' + 7)])
        return paths