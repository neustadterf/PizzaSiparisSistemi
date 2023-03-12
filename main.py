
#Gerekli kitaplıklar içeriye aktarıldı.

import csv
import datetime
#Pizza üst sınıfı oluşturuldu.

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

#Pizza çeşitleri alt sınıflar olarak oluşturuldu.

class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza ", 150)

class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita ", 170)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza ", 150)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza ", 130)

#Decorator üst sınıfı oluşturuldu.Pizza sınıfından kalıtım alındı.

class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

#Sos çeşitleri Decorator sınıfının alt sınıfları olarak oluşturuldu.

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2
        self.description = "zeytin"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 5
        self.description = "mantarlar"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class KeçiPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 7
        self.description = "keçi peyniri"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 15
        self.description = "et"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Soğan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2
        self.description = "soğan"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mısır(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2
        self.description = "mısır"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

#Main fonksiyonu oluşturuldu.

def main():
    #menu.txt dosyası oluşturuldu ve menü içerisine yazılıp ekrana gösterildi.

    menu = open("menu.txt", "w")
    menu.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: SadePizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")
    menu = open("menu.txt", "r")
    oku = menu.read()
    print(oku)

    #Kullanıcıdan input ile pizza ve sos seçimi alındı.

    pizza_secim = input("Pizzanızı şeçiniz (1-4): ")
    sos_secim = input("Pizzanızın yanındaki sosunuzu seçin (11-16): ")

    #Pizza seçimine göre sınıflara yönlendirmek için if yapısı kullanıldı.

    if pizza_secim == "1":
        pizza = Klasik()
    elif pizza_secim == "2":
        pizza = Margarita()
    elif pizza_secim == "3":
        pizza = TurkPizza()
    elif pizza_secim == "4":
        pizza = SadePizza()
    else:
        print("geçerli bir rakam giriniz (1-4)")
        return

    #Sos seçimine göre sınıflara yönlendirmek için if yapısı kullanıldı.

    if sos_secim == "11":
        pizza = Zeytin(pizza)
    elif sos_secim == "12":
        pizza = Mantarlar(pizza)
    elif sos_secim == "13":
        pizza = KeçiPeyniri(pizza)
    elif sos_secim == "14":
        pizza = Et(pizza)
    elif sos_secim == "15":
        pizza = Soğan(pizza)
    elif sos_secim == "16":
        pizza = Mısır(pizza)

    #Toplam fiyat hesaplanıp ekrana basıldı.

    toplam_fiyat = pizza.get_cost()
    print("Seçtikleriniz: " + pizza.get_description() + ", Toplam fiyat: " + str(toplam_fiyat)+" TL")

    #Kullanıcı bigileri kullanıcıdan input ile alındı.

    isim = input("İsminizi giriniz: ")
    tc_kimlik = input("TC kimlik numaranızı giriniz: ")
    kredi_kart_no = input("Kart numaranızı giriniz: ")
    kredi_kart_sifre = input("Kart şifrenizi giriniz: ")
    siparis_zamanı = datetime.datetime.now()

    #Kullanıcı bilgileri sipariş zamanı Orders_Database.csv dosyasına kaydedildi.

    order = [isim, tc_kimlik, kredi_kart_no, pizza.get_description(), siparis_zamanı, kredi_kart_sifre]

    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(order)

    print("Siparişiniz başarıyla oluşturuldu!")


#Main fonksiyonu çağırıldı.
main()



