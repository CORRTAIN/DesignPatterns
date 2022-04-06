import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

if __name__ == '__main__':
    class A:
        pass

    a = A()
    property = Prototype()
    property.register_object('a', a)
    b = property.clone('a', a=1, b=2, c=3)

    print(a)
    print(b)
    print(b.a, b.b, b.c)