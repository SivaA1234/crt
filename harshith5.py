#create a class ticket which will be abstract class inside that create the function book ticket which will be a abstract method and have nothing in it
#create a class make my trip which will use the book ticket function from ticket class to take the details  such as name,phone number,emailid,journey date displays
#message thank you for booking make my trip. create a class irctc which uses of book ticket of ticket class takes the same details of make my trip but in the
#and it will give a option to user to select wheather it is oneway or rountrip .if the user option is round trip it again asks the user to enter the return date as well
#and then prints the msg thank you for choosing irctc else it prints msg thank for choosing irctc.create a class indigo which takes all details as irctc and
#just asks which mode of transport do you want to go train ,bus ,flight,thanks for choosing indigo
from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class make_my_trip(Ticket):
    def book_ticket(self):
        input("enter the name:")
        input("enter the phone number:")
        input("enter the email id:")
        input("enter journey date:")
        print("thank you for booking make my trip")
class irctc(Ticket):
    def book_ticket(self):
        input("enter the name:")
        input("enter the phone number:")
        input("enter the email id:")
        input("enter journey date:")
        select=input("enter wheater its roundtrip or oneway")
        
        if select in ["roundtrip"]:
            input("enter the return date:")
            print("thank you for choosing irctc")
        else:
            print("thanks you for choosing irctc")
class indigo(Ticket):
    def book_ticket(self):
        input("enter the name:")
        input("enter the phone number:")
        input("enter the email id:")
        input("enter journey date:")
        select=input("enter wheater its roundtrip or oneway")
        if select in ["roundtrip"]:
            input("enter the return date:")
            print("thank you for choosing irctc")
        else:
            print("thanks you for choosing irctc")
        input("which mode of transport do you want to go train ,bus ,flight,thanks for choosing indigo:")
        print("thank you for choosing indigo")

k=make_my_trip()
k.book_ticket()
j=irctc()
j.book_ticket()
i=indigo()
i.book_ticket()

        
