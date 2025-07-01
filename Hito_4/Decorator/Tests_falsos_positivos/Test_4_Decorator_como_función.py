class Component:
    def execute(self):
        print("Component execute")

def Decorator(component):
    print("Decorator wrapper")
    component.execute()
