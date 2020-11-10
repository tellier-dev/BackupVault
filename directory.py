class Directory:

    def __init__(self, path=None, name=None, size=None, dictionary=None):
        if dictionary is not None and isinstance(dictionary, dict):
            self.path = dictionary['path']

            dir_name = ''
            if 'name' in dictionary:
                dir_name = dictionary['name']
            self.name = dir_name

            dir_size = -1
            if 'size' in dictionary:
                dir_size = dictionary['size']
            self.size = dir_size
        else:
            dir_path = ''
            dir_name = ''
            dir_size = -1

            if path is not None:
                dir_path = path
            if name is not None:
                dir_name = name
            if size is not None:
                dir_size = size
            self.path = dir_path
            self.name = dir_name
            self.size = dir_size
    
    def asJson(self):
        obj = {'path': self.path}
        obj['name'] = self.name
        obj['size'] = self.size
        return obj
    
    def asList(self):
        dirAsList = []
        dirAsList.append(self.path)
        dirAsList.append(self.name)
        dirAsList.append(self.size)
        return dirAsList
    
    def hasName(self):
        return self.name != ''
    
    def hasSize(self):
        return self.size > -1