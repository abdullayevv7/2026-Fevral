class Salomlashish:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam
    def salom(self, ism, fam):
        return f"Assalomu alaykum hurmatli {self.ism} {self.fam}!"
    
ism = input("Ismingizni kiriting: ").title()
fam = input("Familiyangizni kiriting: ").title()

salom1 = Salomlashish()
print(salom1.salom(ism, fam))