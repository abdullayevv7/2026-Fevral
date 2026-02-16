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




# #Polimorfizm
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

mashina.harakatlan()
velosiped.harakatlan()



# #Inkapsulyatsiya
class Mashina:
    def __init__(self, rang, model):
        self.__rang = rang
        self.__model = model
        self.__tezlik = 0

    def get_rang(self):
        return self.__rang

    def set_rang(self, yangi_rang):
        self.__rang = yangi_rang

    def get_model(self):
        return self.__model

    def set_model(self, yangi_model):
        self.__model = yangi_model

    def get_tezlik(self):
        return self.__tezlik

    def set_tezlik(self, yangi_tezlik):
        if yangi_tezlik >= 0:
            self.__tezlik = yangi_tezlik
        else:
            print("Tezlik manfiy bo‘lishi mumkin emas!")

mening_mashinam = Mashina("qizil", "Toyota")
print(mening_mashinam.get_rang())
mening_mashinam.set_rang("ko‘k")
print(mening_mashinam.get_rang())
mening_mashinam.set_tezlik(30)
print(mening_mashinam.get_tezlik())
mening_mashinam.set_tezlik(-10)
