# # # #print("Hello World")

# class Obuna:
#     def __init__(self, foydalanuvchi, asosiy_narx):
#         self.foydalanuvchi = foydalanuvchi
#         self.asosiy_narx = asosiy_narx
        
#     def oylik_tolov(self):
#         return self.asosiy_narx
    
#     def tavsif(self):
#            return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Oddiy, Oylik to'lov: {self.oylik_tolov()}"
    
    
# class TalabaObunasi(Obuna):
#     def __init__(self, foydalanuvchi, asosiy_narx, talaba_id):
#         super().__init__(foydalanuvchi, asosiy_narx)
#         self.talaba_id = talaba_id
        
#     def oylik_tolov(self):
#         return self.asosiy_narx * 0.7
    
#     def tavsif(self):
#            return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Talaba, Talaba ID: {self.talaba_id}, Oylik to'lov: {self.oylik_tolov()}"
    
    
# class OilaviyObuna(Obuna):
#     def __init__(self, foydalanuvchi, asosiy_narx, ekranlar_soni):
#         super().__init__(foydalanuvchi, asosiy_narx)
#         self.ekranlar_soni = ekranlar_soni
        
        
        
        # # #print("Hello World")

class Obuna:
    def __init__(self, foydalanuvchi, asosiy_narx):
        self.foydalanuvchi = foydalanuvchi
        self.asosiy_narx = asosiy_narx
        
    def oylik_tolov(self):
        return self.asosiy_narx
    
    def tavsif(self):
           return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Oddiy, Oylik to'lov: {self.oylik_tolov()}"
    
    
class TalabaObunasi(Obuna):
    def __init__(self, foydalanuvchi, asosiy_narx, talaba_id):
        super().__init__(foydalanuvchi, asosiy_narx)
        self.talaba_id = talaba_id
        
    def oylik_tolov(self):
        return self.asosiy_narx * 0.7
    
    def tavsif(self):
           return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Talaba, Talaba ID: {self.talaba_id}, Oylik to'lov: {self.oylik_tolov()}"
    
    
class OilaviyObuna(Obuna):
    def __init__(self, foydalanuvchi, asosiy_narx, ekranlar_soni):
            super().__init__(foydalanuvchi, asosiy_narx)
            self.ekranlar_soni = max(1, int(ekranlar_soni))

    def oylik_tolov(self):

            if self.ekranlar_soni <= 1:
                return self.asosiy_narx
            else:
                ekstra = (self.ekranlar_soni - 1) * (0.3 * self.asosiy_narx)
                return round(self.asosiy_narx + ekstra, 2)

    def tavsif(self):
            return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Oilaviy, Ekranlar: {self.ekranlar_soni}, Oylik to'lov: {self.oylik_tolov()}"
if __name__ == "__main__":

    o1 = Obuna("Ali", 100_000)
    t1 = TalabaObunasi("Vali", 100_000, "T-123")
    oila = OilaviyObuna("Ibrohim", 100_000, 3)

    print(o1.tavsif())
    print(f"{o1.foydalanuvchi} oylik: {o1.oylik_tolov()}")
    print(t1.tavsif())
    print(f"{t1.foydalanuvchi} oylik: {t1.oylik_tolov()}")
    print(oila.tavsif())
    print(f"{oila.foydalanuvchi} oylik: {oila.oylik_tolov()}")
