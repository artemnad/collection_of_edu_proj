# классы
class TestClass:
    field1 = 0
    field2 = 0

    def __init__(self, f1=8, f2=78):
        self.field1 = f1
        self.field2 = f2

    def method1(self):
        print(self.field1)

    def sum(self, a, b):
        print(a + b, self.field1)


tmp = TestClass()
print(tmp.field1, tmp.field2)
tmp.field1 = "spam"
tmp.field2 = [0, 0]
print(tmp.field1, tmp.field2)
tmp.method1()
tmp.sum("spam", "!")
print(dir(tmp))
tmp2 = TestClass(3, 4)
print(tmp2.field1, tmp2.field2)


# двоичное дерево поиска

class BinaryTree:
    root = None  # {'left':, 'right':, 'key':, 'value':}

    def __init__(self, key, value):
        self.root = {'left': None, 'right': None, 'key': key, 'value': value}

    def InsertLeft(self, key, value):
        left = BinaryTree(key, value)
        self.root["left"] = left

    def InsertRight(self, key, value):
        right = BinaryTree(key, value)
        self.root["right"] = right

    def Insert(self, key, value):
        if (self.root['key'] == None):
            self.root['key'] = key
            self.root['value'] = value
        else:
            if (key < self.root['key']):
                if (self.root['left'] == None):
                    self.InsertLeft(key, value)
                else:
                    self.root['left'].Insert(key, value)
            elif (key > self.root['key']):
                if (self.root['right'] == None):
                    self.InsertRight(key, value)
                else:
                    self.root['right'].Insert(key, value)
            else:
                self.root['value'] = value

    def FindByKey(self, key):
        if (key < self.root['key']):
            if self.root['left'] == None:
                return None
            else:
                return self.root['left'].FindByKey(key)
        elif (key > self.root['key']):
            if (self.root['right'] == None):
                return None
            else:
                return self.root['right'].FindByKey(key)
        else:
            return self.root['value']

    def FindAllByValue(self, value):
        return []

    def GetDict(self):
        return {}  # {'key': value}

    def GetDeep(self):
        return 0


tree = BinaryTree(None, None)
tree.Insert(5, "str5")
tree.Insert(8, "str8")
tree.Insert(1, "str1")
tree.Insert(4, "str4")
tree.Insert(7, "str7")
print(tree.FindByKey(0))
