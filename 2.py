class hello:
    def __init__(self,name):
        self.name=name
    def func(self):
        return (self.name)
class child(hello):
    def __init__(self,name):
        self.name=name
a=child("hello")
print(a.func())