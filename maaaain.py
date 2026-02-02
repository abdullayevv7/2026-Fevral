# # =========================
# # 1. Supermarket savatchasi
# # =========================
# class CartItem:
#     def __init__(self, name, price, quantity, discount):
#         self.name, self.price, self.quantity, self.discount = name, price, quantity, discount
#     def total_cost(self):
#         return self.price * self.quantity * (1 - self.discount / 100)
#
# class FoodItem(CartItem):
#     def total_cost(self): return f"{self.name}: ${super().total_cost():.2f}"
#
# class NonFoodItem(CartItem):
#     def total_cost(self): return f"{self.name}: ${super().total_cost():.2f}"
#
# print("\n1.")
# for i in [FoodItem("Olma",1.5,3,10), FoodItem("Non",2,2,5)]:
#     print(i.total_cost())
#
#
# # ======================
# # 2. Transport xarajatlari
# # ======================
# class Vehicle:
#     def __init__(self,n,d,f,p): self.name,self.distance,self.fuel_efficiency,self.fuel_price=n,d,f,p
#     def trip_cost(self): return self.distance*self.fuel_efficiency*self.fuel_price
#
# class Car(Vehicle):
#     def trip_cost(self): return f"{self.name}: ${super().trip_cost():.2f}"
#
# class Motorcycle(Vehicle):
#     def trip_cost(self): return f"{self.name}: ${super().trip_cost():.2f}"
#
# print("\n2.")
# for v in [Car("Avto",100,0.1,1.5), Motorcycle("Motosikl",50,0.05,1.5)]:
#     print(v.trip_cost())
#
#
# # ======================
# # 3. Uy hayvonlari
# # ======================
# class Pet:
#     def __init__(self,n,f): self.name,self.daily_food=n,f
#     def feeding_plan(self): return self.daily_food
#
# class Dog(Pet):
#     def feeding_plan(self): return f"It: {self.daily_food} g"
#
# class Cat(Pet):
#     def feeding_plan(self): return f"Mushuk: {self.daily_food} g"
#
# print("\n3.")
# for p in [Dog("It",500), Cat("Mushuk",200)]:
#     print(p.feeding_plan())
#
#
# # ======================
# # 4. Restoran
# # ======================
# class Order:
#     def __init__(self,n,p,s): self.name,self.price,self.service_fee=n,p,s
#     def total_cost(self): return self.price*(1+self.service_fee/100)
#
# class MainDish(Order):
#     def total_cost(self): return f"{self.name}: ${super().total_cost():.2f}"
#
# class SideDish(Order):
#     def total_cost(self): return f"{self.name}: ${super().total_cost():.2f}"
#
# print("\n4.")
# for o in [MainDish("Pizza",15,10), SideDish("Salat",5,10)]:
#     print(o.total_cost())
#
#
# # ======================
# # 5. Baholar
# # ======================
# class Student:
#     def __init__(self,n,g): self.name,self.grades=n,g
#     def average_grade(self): return sum(self.grades)/len(self.grades)
#
# class HighSchoolStudent(Student):
#     def average_grade(self): return f"{self.name}: {super().average_grade():.2f}"
#
# class CollegeStudent(Student):
#     def average_grade(self): return f"{self.name}: {super().average_grade():.2f}"
#
# print("\n5.")
# for s in [HighSchoolStudent("Ali",[5,4,5]), CollegeStudent("Vali",[3,4,5])]:
#     print(s.average_grade())
#
#
# # ======================
# # 6–50 QISQA SHABLON
# # (barchasi bir xil mantiq)
# # ======================
#
# class SimpleBase:
#     def __init__(self,a,b=None,c=None,d=None): self.a,self.b,self.c,self.d=a,b,c,d
#     def calc(self): return self.b if self.b is not None else self.a
#
# class A(SimpleBase):
#     def calc(self): return f"{self.a}: {super().calc()}"
#
# class B(SimpleBase):
#     def calc(self): return f"{self.a}: {super().calc()}"
#
# print("\n6–50.")
# examples = [
#     A("Elektr",100*0.2), B("Suv",5000*0.01),
#     A("Yugurish",30*10), B("Velosiped",20*8),
#     A("Transport",200), B("Yashash",300),
#     A("Standart",100*0.1+50*0.05), B("Premium",200*0.08+100*0.04),
#     A("Gul",2), B("Daraxt",5),
#     A("Ali",20*45+5*20*0.5), B("Vali",15*40),
#     A("WiFi",(50+20)/2), B("4G",(30+15)/2),
#     A("Pizza",20+5*0.5), B("Sushi",15+3*0.5),
#     A("Kecha",(7+8)/2), B("Kunduz",(1+2)/2),
#     A("Oila",1000-500), B("Shaxsiy",500-150),
#     A("Ali",85), B("Vali",90),
#     A("Yotoqxona",(22.5+23)/2), B("Oshxona",(21+22)/2),
#     A("Kofe",5), B("Choy",3),
#     A("Yugurish",60), B("Yoga",45),
#     A("Tesla",50*0.15), B("Nissan",40*0.15),
#     A("Matematika",3), B("Fizika",2),
#     A("Ko‘cha",5*3), B("Garaj",7*2),
#     A("Go‘sht",15), B("Sut",3),
#     A("Shaharda",(60+70)/2), B("Tashqarida",(80+90)/2),
#     A("Osh",60), B("Salat",15),
#     A("Shtanga",50), B("Gantel",20),
#     A("A yo‘li",100), B("B yo‘li",80),
#     A("Supurish","Bajarilmagan"), B("Yuvish","Bajarilgan"),
#     A("Python",300), B("AI",200),
#     A("Dasturlash",40), B("Dizayn",30),
#     A("Olma",100), B("Sovun",50),
#     A("Ali","Tahlil"), B("Vali","Tashxis"),
#     A("Kiyim",50*0.8), B("Elektronika",100*0.9),
#     A("Avtobus",15), B("Metro",10),
#     A("Telefon",500*2), B("Ko‘ylak",30*3),
#     A("Yugurish",30*10), B("Suzish",20*12),
#     A("Kattalar",10), B("Bolalar",5),
#     A("It",50), B("Mushuk",30),
#     A("Transport",200), B("Ovqat",100),
#     A("Oddiy",30), B("Premium",50),
#     A("Gaz",100*0.05), B("Elektr",200*0.1),
#     A("Kitob",20), B("Video",15),
#     A("Sho‘rva",8), B("Salat",5),
#     A("Krossovka",60), B("Sport kiyim",40),
#     A("Oylik",10), B("Yillik",100),
#     A("Gul",20), B("Daraxt",50),
#     A("Individual",100), B("Jamoaviy",150),
#     A("Meva",200), B("Telefon",50),
#     A("Samolyot",2), B("Poezd",5)
# ]
#
# for e in examples:
#     print(e.calc())


## 28.01.2026
# class Hayvon:
#     def __init__(self, nom):
#         self.nom = nom
#
#     def ovoz_chiqar(self):
#         return f"Hayvon ovoz chiqarmoqda"
#
#
# class It(Hayvon):
#     def ovoz_chiqar(self):
#         return f"Vov-vov"
#
# it = It("Bobik")
# print(it.nom)
# print(it.ovoz_chiqar())


# class Tirik:
#     def __init__(self, name, turi, qanday_boqiladi, ovozi):
#         self.name = name
#         self.turi = turi
#         self.qanday_boqiladi = qanday_boqiladi
#         self.ovozi = ovozi

# class Ayiq(Tirik):
#     def malumot(self):
#         return f"{self.name} - {self.turi}, {self.qanday_boqiladi}, ovozi: {self.ovozi}"
    

# m = Ayiq("Qor ayiqlari", "Mammal", "Go'sht va baliq", "Grrr")
# print(m.name)
# print(m.turi)
# print(m.qanday_boqiladi)
# print(m.ovozi)


# class Ish_boshqaruvchi:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Menejer(Ish_boshqaruvchi):
#     def malumot(self):
#         return f"Menejer: {self.name}, Maosh: ${self.salary}"
# class Direktor(Ish_boshqaruvchi):
#     def malumot(self):
#         return f"Direktor: {self.name}, Maosh: ${self.salary}"
# m = Menejer("Ali", 5000)
# d = Direktor("Vali", 10000)
# print(m.malumot())
# print(d.malumot())


