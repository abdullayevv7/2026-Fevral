class Talaba:
    def __init__(self, ism, fan):
        self.__ism = ism
        self.__fan = fan
        self.__baholar = []

    def get_ism(self):
        return self.__ism
    def get_fan(self):
        return self.__fan
    
    def baho_qosh(self, baho):
        if not (0 <= baho <= 100):
            print("Baho 0 dan 100 gacha bo'lishi kerak.")
            return
        else:
            self.__baholar.append(baho)

    def get_baholar(self):
        return self.__baholar.copy()
    
    def ortacha_baho(self):
        if not self.__baholar:
            print("Hali baholar yo'q!")
            return
        else:
            return round(sum(self.__baholar) / len(self.__baholar), 2)
        

talaba = Talaba("Behruz", "Matematika")
talaba.baho_qosh(100)
talaba.baho_qosh(99)
talaba.baho_qosh(77)
print(f"Talaba baholari: {talaba.get_baholar()}")
print(f"Talaba o'rtacha bahosi: {talaba.ortacha_baho()}")

talaba.baho_qosh(1000)
print(f"Talaba baholari: {talaba.get_baholar()}")