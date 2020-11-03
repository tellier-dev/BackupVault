from pathlib import Path


class InputManager:
    def __init__(self):
        self.__file_path = "input_dirs.txt"
        doc = Path(self.__file_path)
        if not doc.is_file():
            try:
                open(self.__file_path, 'x')
            except IOError:
                print("Unhandled IO Error")

    def add_path(self, path):
        doc = open(self.__file_path, 'a')
        doc.write(path + "\n")
        doc.close()
        print("-- Path : {}".format(path))

    def remove_path(self, path):
        doc = open(self.__file_path, 'r')
        paths = doc.readlines()
        doc.close()

        removed = False
        for p in paths:
            if p == path:
                removed = True

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
                paths.append(path.strip())
        return paths
    
    def has_paths(self):
        paths = self.get_paths()
        return paths is not None and len(paths) > 0