eded1 = int(input("Birinci ededi daxil et: "))
eded2 = int(input("Ikinci ededi daxil et: "))
cem = eded1 + eded2
ferq = eded1 - eded2
hasil = eded1 * eded2
qismet = eded1 / eded2
print(f"Cem: {cem}")
print(f"Ferq: {ferq}")
print(f"Hasil: {hasil}")
print(f"Qismet: {qismet}")

##2
dogum_ili = int(input("Dogum ilini daxil et: "))
yas = 2026 - dogum_ili
print(f"Senin yasin: {yas}")

##3
en = float(input("Duzbucaqlinin enini daxil et: "))
uzunluq = float(input("Duzbucaqlinin uzunlugunu daxil et: "))
sahe = en * uzunluq
perimetr = 2*(en + uzunluq)
print(f"Sahə: {sahe}")
print(f"Perimetr: {perimetr}")

##4
toplam_deqiqe = int(input("Deqiq sayini daxil et: "))
saat = toplam_deqiqe // 60
qaliq_deqiqe = toplam_deqiqe % 60
print(f"{toplam_deqiqe} dəqiqə = {saat} saat {qaliq_deqiqe} dəqiqə")

##5
toplam_saniye = int(input("Saniyə sayini daxil et: "))
saat = toplam_saniye // 3600
qaliq_saniye = toplam_saniye % 3600
deqiqe = qaliq_saniye // 60
saniye = qaliq_saniye % 60
print(f"{toplam_saniye} saniyə = {saat} saat {deqiqe} dəqiqə {saniye} saniyə")

##6
toplam_qepik = int(input("Umumi qepik sayini daxil et: "))
manat = toplam_qepik // 100
qaliq_qepik = toplam_qepik % 100
print(f"{toplam_qepik} qəpik = {manat} manat {qaliq_qepik} qəpik")

##7
sagird_sayi = int(input("Sinifdeki şagirdlerin sayini daxil et: "))
qelem_sayi = int(input("Qelemlerin umumi sayini daxil et: "))
her_sagirde = qelem_sayi // sagird_sayi
artiq_qaldi = qelem_sayi % sagird_sayi
print(f"Hər şagirdə dusen qelem sayi: {her_sagirde}")
print(f"Artiq qalan qelem sayi: {artiq_qaldi}")

##8
eded = int(input("İkireqemli eded daxil edin: "))
onluq = eded // 10
tekliyi = eded % 10

print("Onluq:", onluq)
print("Təklik:", tekliyi)

##9
eded = int(input("Ucreqemli eded daxil et: "))
yuzluk = eded // 100
onluq = (eded // 10) % 10
teklik = eded % 10
cem = yuzluk + onluq + teklik

print(f"Yuzluk: {yuzluk}")
print(f"Onluq: {onluq}")
print(f"Teklik: {teklik}")
print(f"Reqemlerin cemi: {cem}")

##10
gun_sayi = int(input("Gunlerin umumi sayini daxil et: "))
hefte = gun_sayi // 7
elave_gun = gun_sayi % 7

print(f"Hefte sayi: {hefte}")
print(f"Elave gun sayi: {elave_gun}")
