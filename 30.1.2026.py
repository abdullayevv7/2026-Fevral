##1
class Transport:
    def __init__(self, model: str, yil: int) -> None:
        self.model = model
        self.yil = yil
        
    def malumot(self) -> str:
        return f"Model: {self.model}, Yil: {self.yil}"

class Avtomobil(Transport):
    def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
        super().__init__(model, yil)
        self.yonilgi_turi = yonilgi_turi
    
    def malumot(self) -> str:
        baza = super().malumot()
        return f"{baza}, Yonilg'i: {self.yonilgi_turi}"

class Avtobus(Transport):
    def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
        super().__init__(model, yil)
        self.orinlar_soni = orinlar_soni
    
    def malumot(self) -> str:
        baza = super().malumot()
        return f"{baza}, O'rinlar: {self.orinlar_soni}"


a = Avtomobil("Cobalt", 2022, "benzin")
print(a.malumot())

b = Avtobus("Isuzu", 2018, 40)
print(b.malumot())

##2
class Kitob:
    def __init__(self, nom: str, muallif: str, yil: int) -> None:
        self.nom = nom
        self.muallif = muallif
        self.yil = yil
    
    def taqdimot(self) -> str:
        return f'"{self.nom}" - {self.muallif} ({self.yil})'


class ElektronKitob(Kitob):
    def __init__(self, nom: str, muallif: str, yil: int, fayl_hajmi_mb: float) -> None:
        super().__init__(nom, muallif, yil)
        self.fayl_hajmi_mb = fayl_hajmi_mb
    
    def taqdimot(self) -> str:
        return super().taqdimot() + f" [Elektron, {self.fayl_hajmi_mb}MB]"


class AudioKitob(Kitob):
    def __init__(self, nom: str, muallif: str, yil: int, davomiylik_soat: float) -> None:
        super().__init__(nom, muallif, yil)
        self.davomiylik_soat = davomiylik_soat
    
    def taqdimot(self) -> str:
        return super().taqdimot() + f" [Audio, {self.davomiylik_soat} soat]"