# class Salomlashish:
#     def __init__(self, ism, fam):
#         self.ism = ism
#         self.fam = fam
#     def salom(self, ism, fam):
#         return f"Assalomu alaykum hurmatli {self.ism} {self.fam}!"
    
# ism = input("Ismingizni kiriting: ").title()
# fam = input("Familiyangizni kiriting: ").title()

# salom1 = Salomlashish()
# print(salom1.salom(ism, fam))




class Transport:
    def __init__(self, rang):
        self.rang = rang

    def harakatlan(self):
        print("Harakatlanmoqda")

class Mashina(Transport):
    def harakatlan(self):
        print(f"{self.rang} mashina yo‘lda g‘ildirab ketyapti!")

class Velosiped(Transport):
    def harakatlan(self):
        print(f"{self.rang} velosiped pedalsiz ham yuradi!")


mashina = Mashina("qizil")
velosiped = Velosiped("yashil")

mashina.harakatlan()    # "qizil mashina yo‘lda g‘ildirab ketyapti!"
velosiped.harakatlan()  # "yashil velosiped pedalsiz ham yuradi!"
