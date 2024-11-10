
from ast import main
from typing import Any


class Container:
    def __init__(self, name, min_temp, max_temp, temp) -> None:
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.temp = temp

    
class ContainerManager:
    def __init__(self) -> None:
        self.containers = []
    
    def add(self, name, min_temp, max_temp, temp):
        self.containers.append(Container(name,min_temp, max_temp, temp))
    
    def __getitem__(self, name: str):
        return [i for i in self.containers if i.name == name][0]

    def __contains__(self, name):
        return name in [c.name for c in self.containers]

    def verify(self, data): # name:instruction
        name, instruction, *data = data.split(":")
        if name not in self:
            self.add(name, 12, 32, 0.0)
        match instruction:
            case "SET":
                self[name].temp = float(data[0])
                self[name].min_temp = min(self[name].temp, self[name].min_temp)
                self[name].max_temp = max(self[name].temp, self[name].max_temp)
    
    def __iter__(self):
        return iter(self.containers)


    def get(self, name):
        return self[name].temp
        

if __name__ == '__main__':
    manager = ContainerManager()
    manager.add("test1", 12, 32, 20)
    manager.add("test2", 12, 32, 20)
    manager.add("test3", 12, 32, 20)

    manager.verify("test7:SET:10")
    print(manager["test7"].temp)