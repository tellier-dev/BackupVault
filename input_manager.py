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

    def add_path(self, path, name):
        doc = open(self.__file_path, 'a')
        doc.write("Name:{} | Path:{}\n".format(name, path))
        doc.close()
        print("-- Name: {} | Path: {}".format(name, path))
        

    def remove_path(self, path):
        doc = open(self.__file_path, 'r')
        paths = doc.readlines()
        doc.close()

        removed = False
        for p in paths:
            if p[p.index('| Path:') + 7:] == path:
                removed = True
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
        print("Input dirs have been removed.")
        doc.close()

    def list(self):
        doc = open(self.__file_path, 'r')
        paths = doc.readlines()
        print()
        for path in paths:
            print("Path: {}".format(path))
        doc.close()

    def get_paths(self):
        doc = open(self.__file_path, 'r')
        doc_paths = doc.readlines()
        doc.close()
        paths = []
        for path in doc_paths:
            path = path.replace('\n', '')
            index = path.index('| Path:') + 7
            paths.append(path[index:])
        return paths
    
    def get_name_from_root_path(self, root_path):
        doc = open(self.__file_path, 'r')
        doc_paths = doc.readlines()
        doc.close()
        for path in doc_paths:
            path = path.replace('\n', '')
            index = path.index('| Path:') + 7
            if root_path == path[index:]:
                index = path.index(' | Path:')
                return path[len("Name:"):index]
        return None
    
    def has_paths(self):
        paths = self.get_paths()
        return paths is not None and len(paths) > 0