class car:
    def __init__(self,model,variant,color):
        self.model=model
        self.variant=variant
        self.color=color
    def print_info(self):
        print('car information=',self.model,self.variant,self.color)
obj=car("glanza","petrol","red")
obj.print_info()
class model(car):
    pass
obj=model("hycross","diesel","blue")
obj.print_info()
