class Transport:
    def __init__(self, model, yil):
        self.model = model
        self.yil = yil
    
    def malumot(self):
        return f"Model: {self.model}, Yil: {self.yil}"


class Avtomobil(Transport):
    def __init__(self, model, yil, yonilgi_turi):
        super().__init__(model, yil)
        self.yonilgi_turi = yonilgi_turi
    
    def malumot(self):
        asosiy_malumot = super().malumot()
        return f"{asosiy_malumot}, Yonilg'i: {self.yonilgi_turi}"


class Avtobus(Transport):
    def __init__(self, model, yil, o_rinlar_soni):
        super().__init__(model, yil)
        self.o_rinlar_soni = o_rinlar_soni
    
    def malumot(self):
        asosiy_malumot = super().malumot()
        return f"{asosiy_malumot}, O'rinlar: {self.o_rinlar_soni}"


a = Avtomobil("Cobalt", 2022, "benzin")
print(a.malumot())

b = Avtobus("Isuzu", 2018, 40)
print(b.malumot())


class Kitob:
    def __init__(self, nom, muallif, yil):
        self.nom = nom
        self.muallif = muallif
        self.yil = yil
    
    def taqdimot(self):
        return f'"{self.nom}" - {self.muallif} ({self.yil})'


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, yil, fayl_hajmi_mb):
        super().__init__(nom, muallif, yil)
        self.fayl_hajmi_mb = fayl_hajmi_mb
    
    def taqdimot(self):
        asosiy = super().taqdimot()
        return f"{asosiy} [Elektron, {self.fayl_hajmi_mb}MB]"


class AudioKitob(Kitob):
    def __init__(self, nom, muallif, yil, davomiylik_soat):
        super().__init__(nom, muallif, yil)
        self.davomiylik_soat = davomiylik_soat
    
    def taqdimot(self):
        asosiy = super().taqdimot()
        return f"{asosiy} [Audio, {self.davomiylik_soat} soat]"


e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)

print(e.taqdimot())
print(a.taqdimot())


class Xodim:
    def __init__(self, ism, asosiy_maosh):
        self.ism = ism
        self.asosiy_maosh = asosiy_maosh
    
    def oylik(self):
        return self.asosiy_maosh
    
    def malumot(self):
        return f"Ism: {self.ism}, Oylik: {self.oylik()}"


class Oqsoch(Xodim):
    def __init__(self, ism, asosiy_maosh, bonus_foiz):
        super().__init__(ism, asosiy_maosh)
        self.bonus_foiz = bonus_foiz
    
    def oylik(self):
        bonus = self.asosiy_maosh * (self.bonus_foiz / 100)
        return self.asosiy_maosh + bonus


class SoatbayXodim(Xodim):
    def __init__(self, ism, soat, soatlik_stavka):
        asosiy_maosh = soat * soatlik_stavka
        super().__init__(ism, asosiy_maosh)
        self.soat = soat
        self.soatlik_stavka = soatlik_stavka


o = Oqsoch("Dilshod", 5_000_000, 20)
s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)

print(o.malumot())
print(s.malumot())


class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx
    
    def chegirmali_narx(self, foiz):
        chegirma = self.narx * (foiz / 100)
        return self.narx - chegirma


class Elektronika(Mahsulot):
    def __init__(self, nom, narx, kafolat_oy):
        super().__init__(nom, narx)
        self.kafolat_oy = kafolat_oy
    
    def malumot(self):
        return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"


class OziqOvqat(Mahsulot):
    def __init__(self, nom, narx, yaroqlilik_kuni):
        super().__init__(nom, narx)
        self.yaroqlilik_kuni = yaroqlilik_kuni
    
    def malumot(self):
        return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"


telefon = Elektronika("iPhone 15", 12_000_000, 12)
sut = OziqOvqat("Sut", 9000, "2026-12-31")

print(telefon.malumot())
print(sut.malumot())

print(telefon.chegirmali_narx(10))


class Shaxs:
    def __init__(self, ism):
        self.ism = ism


class Talaba(Shaxs):
    def __init__(self, ism, id_raqam):
        super().__init__(ism)
        self.id_raqam = id_raqam


class ImtihonNatijasi(Talaba):
    def __init__(self, ism, id_raqam, baholar):
        super().__init__(ism, id_raqam)
        self.baholar = baholar
    
    def ortalama(self):
        return sum(self.baholar) / len(self.baholar)
    
    def status(self):
        ort = self.ortalama()
        if ort >= 86:
            return "A'lo"
        elif ort >= 71:
            return "Yaxshi"
        elif ort >= 56:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"


natija = ImtihonNatijasi("Ali", "T001", [90, 80, 100])
print(natija.ism)
print(natija.id_raqam)
print(natija.ortalama())
print(natija.status())


# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
    
#     def kirim(self, summa):
#         self.balans += summa
    
#     def chiqim(self, summa):
#         if self.balans >= summa:
#             self.balans -= summa
#         else:
#             return "Balans yetarli emas"


# class JamgArmaMixin:
#     def __init__(self, *args, foiz_stavka, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.foiz_stavka = foiz_stavka
    
#     def foiz_qosh(self):
#         foiz = self.balans * (self.foiz_stavka / 100)
#         self.balans += foiz


# class KreditMixin:
#     def __init__(self, *args, limit, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.limit = limit
    
#     def chiqim(self, summa):
#         if self.balans + self.limit >= summa:
#             self.balans -= summa
#         else:
#             return "Balans va limit ham yetarli emas"


# class VIPHisob(Hisob, JamgArmaMixin, KreditMixin):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans, foiz_stavka=foiz_stavka, limit=limit)


# vip = VIPHisob("001", "Karim", 2_000_000, foiz_stavka=12, limit=500_000)
# vip.foiz_qosh()
# print(vip.balans)

# vip.chiqim(2_400_000)
# print(vip.balans)


class Kurs:
    def __init__(self, nom, davomiylik_hafta, narx):
        self.nom = nom
        self.davomiylik_hafta = davomiylik_hafta
        self.narx = narx
    
    def malumot(self):
        return f"Kurs: {self.nom}, Davomiylik: {self.davomiylik_hafta} hafta, Narx: {self.narx}"


class OnlaynKurs(Kurs):
    def __init__(self, nom, davomiylik_hafta, narx, platforma):
        super().__init__(nom, davomiylik_hafta, narx)
        self.platforma = platforma
    
    def malumot(self):
        asosiy = super().malumot()
        return f"{asosiy}, Platforma: {self.platforma}"


class OfflineKurs(Kurs):
    def __init__(self, nom, davomiylik_hafta, narx, manzil):
        super().__init__(nom, davomiylik_hafta, narx)
        self.manzil = manzil
    
    def malumot(self):
        asosiy = super().malumot()
        return f"{asosiy}, Manzil: {self.manzil}"


kurslar = [
    OnlaynKurs("Python Asoslari", 8, 500_000, "Udemy"),
    OfflineKurs("Java Bootcamp", 12, 2_000_000, "Toshkent, Chilonzor"),
    OnlaynKurs("Web Development", 10, 800_000, "Coursera")
]

for kurs in kurslar:
    print(kurs.malumot())


class Taom:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx
    
    def tavsif(self):
        return f"Taom: {self.nom}, Narx: {self.narx}"


class IssiqTaom(Taom):
    def __init__(self, nom, narx, kaloriya):
        super().__init__(nom, narx)
        self.kaloriya = kaloriya
    
    def tavsif(self):
        asosiy = super().tavsif()
        return f"{asosiy}, Kaloriya: {self.kaloriya}"


class Ichimlik(Taom):
    def __init__(self, nom, narx, hajm_ml):
        super().__init__(nom, narx)
        self.hajm_ml = hajm_ml
    
    def tavsif(self):
        asosiy = super().tavsif()
        return f"{asosiy}, Hajm: {self.hajm_ml}ml"


def chegirma_qollash(taomlar, foiz):
    for taom in taomlar:
        chegirma = taom.narx * (foiz / 100)
        taom.narx -= chegirma


menu = [
    IssiqTaom("Osh", 25_000, 650),
    IssiqTaom("Lag'mon", 22_000, 580),
    Ichimlik("Coca Cola", 8_000, 500),
    Ichimlik("Choy", 3_000, 200)
]

print("Chegirmadan oldin:")
for taom in menu:
    print(taom.tavsif())

chegirma_qollash(menu, 10)

print("\n10% chegirmadan keyin:")
for taom in menu:
    print(taom.tavsif())


from abc import ABC, abstractmethod


class JamoaAzo(ABC):
    def __init__(self, ism):
        self.ism = ism
    
    @abstractmethod
    def vazifa(self):
        pass


class BackendDasturchi(JamoaAzo):
    def vazifa(self):
        return "API va ma'lumotlar bazasi bilan ishlaydi"


class FrontendDasturchi(JamoaAzo):
    def vazifa(self):
        return "UI va foydalanuvchi tajribasini yaratadi"


class Tester(JamoaAzo):
    def vazifa(self):
        return "Tizimni test qiladi"


def hisobot(azolar):
    for azo in azolar:
        print(f"Ism: {azo.ism}, Vazifa: {azo.vazifa()}")


jamoa = [
    BackendDasturchi("Ali"),
    FrontendDasturchi("Vali"),
    Tester("Hasan"),
    BackendDasturchi("Husan")
]

hisobot(jamoa)


class QadamSanagich:
    def __init__(self, kunlik_maqsad, qadamlar):
        self.kunlik_maqsad = kunlik_maqsad
        self.qadamlar = qadamlar
    
    def bajarilgan_kunlar(self):
        count = 0
        for qadam in self.qadamlar:
            if qadam >= self.kunlik_maqsad:
                count += 1
        return count
    
    def ortalama_qadam(self):
        return sum(self.qadamlar) / len(self.qadamlar)


class MotivatsionQadamSanagich(QadamSanagich):
    def motivatsiya_xabari(self):
        if self.bajarilgan_kunlar() >= 5:
            return "Barakalla! Siz juda faol ekansiz!"
        else:
            return "Harakatni ko'proq oshiring!"


hafta = [10000, 7500, 8200, 9000, 5000, 12000, 8000]
q = MotivatsionQadamSanagich(8000, hafta)

print(f"Bajarilgan kunlar: {q.bajarilgan_kunlar()}")
print(f"O'rtacha qadam: {q.ortalama_qadam():.1f}")
print(q.motivatsiya_xabari())






def qaytim_hisobla(narx, tolangan):
    if tolangan < narx:
        return "Pul yetarli emas"
    return tolangan - narx


print(qaytim_hisobla(12000, 20000))
print(qaytim_hisobla(15000, 10000))
print(qaytim_hisobla(50000, 50000)) 


def borsh_orinlar(jami, yolovchilar):
    if yolovchilar > jami:
        return "Joy yetmaydi"
    return jami - yolovchilar


print(borsh_orinlar(40, 32))
print(borsh_orinlar(50, 55))
print(borsh_orinlar(30, 30))


def jarima_hisobla(kechikkan_kun):
    jarima = 0
    
    if kechikkan_kun <= 5:
        jarima = kechikkan_kun * 1000
    elif kechikkan_kun <= 10:
        jarima = 5 * 1000
        jarima += (kechikkan_kun - 5) * 2000
    else:
        jarima = 5 * 1000
        jarima += 5 * 2000
        jarima += (kechikkan_kun - 10) * 3000
    
    return jarima


print(jarima_hisobla(3))
print(jarima_hisobla(7))
print(jarima_hisobla(12))
print(jarima_hisobla(15))


def jarima_hisobla(kechikkan_kun):
    jarima = 0
    
    if kechikkan_kun <= 5:
        jarima = kechikkan_kun * 1000
    elif kechikkan_kun <= 10:
        jarima = 5 * 1000
        jarima += (kechikkan_kun - 5) * 2000
    else:
        jarima = 5 * 1000
        jarima += 5 * 2000
        jarima += (kechikkan_kun - 10) * 3000
    
    return jarima


print(jarima_hisobla(3))
print(jarima_hisobla(7))
print(jarima_hisobla(12))
print(jarima_hisobla(15))


def reyting_tahlil(baholar):
    ortalama = sum(baholar) / len(baholar)
    eng_yuqori = max(baholar)
    eng_past = min(baholar)
    
    a_soni = 0
    for baho in baholar:
        if 86 <= baho <= 100:
            a_soni += 1
    
    return {
        "ortalama": round(ortalama, 2),
        "eng_yuqori": eng_yuqori,
        "eng_past": eng_past,
        "a_soni": a_soni
    }


baholar = [56, 89, 100, 75, 90, 86]
natija = reyting_tahlil(baholar)
print(natija)


def umumiy_summa(savat):
    jami = 0
    for mahsulot in savat:
        nom, narx, soni = mahsulot
        jami += narx * soni
    return jami


savat = [
    ("Non", 4000, 2),
    ("Sut", 9000, 1),
    ("Olma", 6000, 3)
]
print(umumiy_summa(savat))


def chipta_narxi(baza_narx, yosh, bagaj_kg):
    narx = baza_narx
    
    if yosh < 12:
        narx = narx * 0.5
    elif yosh > 60:
        narx = narx * 0.7
    
    if bagaj_kg > 20:
        qoshimcha_kg = bagaj_kg - 20
        qoshimcha_tolov = qoshimcha_kg * 10_000
        narx += qoshimcha_tolov
    
    return int(narx)


print(chipta_narxi(500000, 10, 15))
print(chipta_narxi(500000, 65, 25))
print(chipta_narxi(500000, 35, 18))
print(chipta_narxi(500000, 8, 30))


def qadam_tahlil(qadamlar):
    maqsad = 8000
    bajarilgan = 0
    bajarilmagan = 0
    
    for qadam in qadamlar:
        if qadam >= maqsad:
            bajarilgan += 1
        else:
            bajarilmagan += 1
    
    ortalama = sum(qadamlar) / len(qadamlar)
    
    return {
        "bajarilgan": bajarilgan,
        "bajarilmagan": bajarilmagan,
        "ortalama": round(ortalama, 2)
    }


hafta = [10000, 7500, 8200, 9000, 5000, 12000, 8000]
print(qadam_tahlil(hafta))


def kartalarni_filtrlash(kartalar, tur, min_balans):
    natija = []
    
    for karta in kartalar:
        egasi, balans, karta_turi = karta
        
        if karta_turi == tur and balans >= min_balans:
            natija.append(karta)
    
    return natija


kartalar = [
    ("Ali", 1_000_000, "debet"),
    ("Vali", 500_000, "kredit"),
    ("Hasan", 3_000_000, "debet"),
    ("Husan", 200_000, "kredit")
]

print(kartalarni_filtrlash(kartalar, "debet", 2_000_000))

print(kartalarni_filtrlash(kartalar, "kredit", 300_000))


def vazifa_statistikasi(vazifalar):
    bajarildi = 0
    jarayonda = 0
    kutilmoqda = 0
    umumiy_soat = 0
    
    for vazifa in vazifalar:
        status = vazifa["status"]
        soatlar = vazifa["soatlar"]
        
        if status == "bajarildi":
            bajarildi += 1
        elif status == "jarayonda":
            jarayonda += 1
        elif status == "kutilmoqda":
            kutilmoqda += 1
        
        umumiy_soat += soatlar
    
    return {
        "bajarildi": bajarildi,
        "jarayonda": jarayonda,
        "kutilmoqda": kutilmoqda,
        "umumiy_soat": umumiy_soat
    }


vazifalar = [
    {"nom": "Backend API", "soatlar": 10, "status": "bajarildi"},
    {"nom": "Frontend UI", "soatlar": 8, "status": "jarayonda"},
    {"nom": "Testing", "soatlar": 6, "status": "kutilmoqda"},
    {"nom": "Database", "soatlar": 12, "status": "bajarildi"},
]

print(vazifa_statistikasi(vazifalar))


def navbatni_tartibla(buyurtmalar):
    return sorted(buyurtmalar, key=lambda x: x["vaqt"])


buyurtmalar = [
    {"id": 1, "mijoz": "Ali", "vaqt": 15},
    {"id": 2, "mijoz": "Vali", "vaqt": 10},
    {"id": 3, "mijoz": "Hasan", "vaqt": 15},
    {"id": 4, "mijoz": "Aziza", "vaqt": 8},
]

natija = navbatni_tartibla(buyurtmalar)
for buyurtma in natija:
    print(buyurtma)
