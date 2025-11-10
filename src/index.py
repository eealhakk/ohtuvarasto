from varasto import Varasto


def nayta_varasto(varasto, nimi):
    print(f"{nimi}: {varasto}")


def testaa_lisays(varasto, maara):
    print(f"Lisätään {maara}")
    varasto.lisaa_varastoon(maara)
    nayta_varasto(varasto, "Varasto")


def testaa_otto(varasto, maara):
    print(f"Otetaan {maara}")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    nayta_varasto(varasto, "Varasto")

def nayta_getterit(varasto, nimi):
    print(f"{nimi} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def virhetilanteet():
    print("Virhetilanteita:")
    huono1 = Varasto(-100.0)
    nayta_varasto(huono1, "Huono1")

    huono2 = Varasto(100.0, -50.7)
    nayta_varasto(huono2, "Huono2")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    nayta_varasto(mehua, "Mehuvarasto")
    nayta_varasto(olutta, "Olutvarasto")

    nayta_getterit(olutta, "Olut")

    print("Mehu setterit:")
    testaa_lisays(mehua, 50.7)
    testaa_otto(mehua, 3.14)

    virhetilanteet()

    testaa_lisays(olutta, 1000.0)
    testaa_lisays(mehua, -666.0)
    testaa_otto(olutta, 1000.0)
    testaa_otto(mehua, -32.9)


if __name__ == "__main__":
    main()
