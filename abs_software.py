import numpy as mat
import skfuzzy as mantik
from skfuzzy import control as kontrol
import pypyodbc
import random

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=pc_sql_server_name'
    'Database=database_name'
    'Trusted_Connection=True;'
)

imlec = db.cursor()

imlec.execute('SELECT * FROM sorular')

sorular = imlec.fetchall()
print(sorular)

mesafe = kontrol.Antecedent(mat.arange(0, 50, 1), 'mesafe')
hiz = kontrol.Antecedent(mat.arange(0, 100, 1), 'hiz')
frenBasinci = kontrol.Consequent(mat.arange(0, 100, 1), 'frenBasinci')

mesafe[sorular[1][1]] = mantik.trimf(mesafe.universe, [0, 0, 10])
mesafe[sorular[0][1]] = mantik.trimf(mesafe.universe, [5, 15, 25])
mesafe[sorular[2][1]] = mantik.trimf(mesafe.universe, [20, 30, 40])
mesafe[sorular[3][1]] = mantik.trimf(mesafe.universe, [35, 50, 50])

hiz['çok yavaş'] = mantik.trapmf(hiz.universe, [0, 0, 20, 30])
hiz['yavaş'] = mantik.trapmf(hiz.universe, [20, 30, 45, 55])
hiz['hızlı'] = mantik.trapmf(hiz.universe, [45, 55, 70, 80])
hiz['çok hızlı'] = mantik.trapmf(hiz.universe, [70, 80, 100, 100])

frenBasinci['çok düşük'] = mantik.trimf(frenBasinci.universe, [0, 20, 40])
frenBasinci['düşük'] = mantik.trimf(frenBasinci.universe, [20, 40, 60])
frenBasinci['yüksek'] = mantik.trimf(frenBasinci.universe, [40, 60, 80])
frenBasinci['çok yüksek'] = mantik.trimf(frenBasinci.universe, [60, 100, 100])


kural1 = kontrol.Rule(mesafe[sorular[1][1]] & hiz['çok yavaş'], frenBasinci['çok yüksek'])
kural2 = kontrol.Rule(mesafe[sorular[0][1]] & hiz['çok yavaş'], frenBasinci['çok düşük'])
kural3 = kontrol.Rule(mesafe[sorular[1][1]] & hiz['yavaş'], frenBasinci['çok yüksek'])
kural4 = kontrol.Rule(mesafe[sorular[0][1]] & hiz['yavaş'], frenBasinci['düşük'])
kural5 = kontrol.Rule(mesafe[sorular[2][1]] & hiz['yavaş'], frenBasinci['çok düşük'])
kural6 = kontrol.Rule(mesafe[sorular[1][1]] & hiz['hızlı'], frenBasinci['çok yüksek'])
kural7 = kontrol.Rule(mesafe[sorular[0][1]] & hiz['hızlı'], frenBasinci['düşük'])
kural8 = kontrol.Rule(mesafe[sorular[2][1]] & hiz['hızlı'], frenBasinci['çok düşük'])
kural9 = kontrol.Rule(mesafe[sorular[1][1]] & hiz['çok hızlı'], frenBasinci['çok yüksek'])
kural10 = kontrol.Rule(mesafe[sorular[0][1]] & hiz['çok hızlı'], frenBasinci['yüksek'])
kural11 = kontrol.Rule(mesafe[sorular[2][1]] & hiz['çok hızlı'], frenBasinci['düşük'])
kural12 = kontrol.Rule(mesafe[sorular[3][1]] & hiz['çok hızlı'], frenBasinci['çok düşük'])

frenKontrol = kontrol.ControlSystem([kural1, kural2, kural3, kural4, kural5,
                                    kural6, kural7, kural8, kural9, kural10,
                                    kural11, kural12])

frenleme = kontrol.ControlSystemSimulation(frenKontrol)

sayac = 0
 
v = int(input("Hızı gir(0-100 km/h) : "))
s = int(input("Mesafeyi gir (m) : "))
e = int(input("Eğimi Giriniz : "))
    # v = random.randint(1, 100)
    # s = random.randint(1, 50)
    # e = random.randint(1, 60)
        
if (v/2 <= s):
    print("frene basılmasına gerek yoktur.")
            
else:
    frenleme.input['hiz'] = v
    frenleme.input['mesafe'] = s
            
    frenleme.compute()
    print("Fren Basıncı (%) :" , frenleme.output['frenBasinci'])
    print("yeni hız değeri : ", v-(v*frenleme.output['frenBasinci']/100))
    komut = 'INSERT INTO islemsonuclari VALUES(?,?,?)'
    veriler = (v-(v*frenleme.output['frenBasinci']/100),frenleme.output['frenBasinci'],e)
    
    sonuc = imlec.execute(komut,veriler)
    db.commit()

    
hiz.view(sim=frenleme)
