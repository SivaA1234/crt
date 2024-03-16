#create a class of palcements which has function info which displays no of placements this year.create another class name departement with function display
#which will display the name of the departements present in college.create a class pragati.with fun()"welcome"which dispalys message.pragati class should also display
#details about departments and placemets
class placements:
    def info(self):
        print("the no of placements this year is 650 and still counting")
class departments(placements):
    def display(self,cse,IT,ECE,CIVIL,MECH,EEE):
        self.cse=cse
        self.IT=IT
        self.ECE=ECE
        self.CIVIL=CIVIL
        self.MECH=MECH
        self.EEE=EEE
        print('the departements=',self.cse,self.IT,self.ECE,self.CIVIL,self.MECH,self.EEE)
class pragati(departments):
    def welcome(self):
        print("welcome to pragati college")
obj1=pragati()
obj1.welcome()
obj1.info()
obj1.display("cse","IT","ECE","CIVIL","MECH","EEE")


        
