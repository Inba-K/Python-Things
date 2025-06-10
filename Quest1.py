class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __del__(self):
        print("An employee has been fired.")
Jim=employee("Jim",25)
Jim.__del__()
