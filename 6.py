def kilometrdan_metrga(km):
    return km * 1000


def metr_dan_santimetrga(metr):
    return metr * 100


def kilogrammdan_grammga(kg):
    return kg * 1000


if __name__ == "main":
    print(kilometrdan_metrga(5))
    print(metr_dan_santimetrga(3))
    print(kilogrammdan_grammga(2))