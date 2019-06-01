import typing
# metraze [m2]
pokoj_dzienny = 4*5
sypialnia = 3.8*4
kuchnia = 3.3*3.5
lazienka = 2.2*1.7
korytarz = (1*2.7)+(0.8*0.8)
# dict pomiesczen
pomieszczenia = {
    "pokoj_dzienny": pokoj_dzienny,
    "sypialnia": sypialnia,
    "kuchnia": kuchnia,
    "lazienka": lazienka,
    "korytarz": korytarz
}

# bezpieczne zalozenie wymganej do ogrzania pomieszczen energii w domu [W/m2]
zaptorzebowanie_na_energie = 150


def oblicz_zapotrzebowanie_cieplne(pomieszczenia: typing.Dict) -> typing.Dict:
    zapotrzebowanie_pomieszczen = {}
    for pomieszczenie in pomieszczenia.items():
        print(f'{pomieszczenie[0]}: {pomieszczenie[1]}')
        zapotrzebowanie_pomieszczen[pomieszczenie[0]] = (
            pomieszczenie[1] * zaptorzebowanie_na_energie
        )
    return zapotrzebowanie_pomieszczen

zapotrzebowanie_pomieszczen = (
    oblicz_zapotrzebowanie_cieplne(pomieszczenia=pomieszczenia)
)
print(
    f'Zapotrzebowanie cieplne pomieszczen [W]: ' +
    f'\n{zapotrzebowanie_pomieszczen}'
)

powierzchnie = list(pomieszczenia.values())
calkowita_powierzchnia = 0
for powierzchnia in powierzchnie:
    calkowita_powierzchnia = calkowita_powierzchnia + powierzchnia
print(f'Calkowita powierzchnia: {calkowita_powierzchnia} m2')
print(f'Całokowiete zapotrzebowanie: {calkowita_powierzchnia*150/1000} [kW]')
