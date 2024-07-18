# Fliper Igra - Space Pinball



Dobrodošli u Space Pinball! Ova igra je razvijena u Pythonu koristeći popularni modul Pygame. Pre nego što započnete, uverite se da imate instaliran Python i Pygame, i da su parametri prilagođeni vašoj rezoluciji.

## Preduslovi
1. Instalirajte Python (preporučena verzija: 3.11 ili novija)
2. Instalirajte Pygame: `pip install pygame`
3. Podesite parametre igre prema svojoj rezoluciji

## Opis igre
Space Pinball pruža mehaničko iskustvo 2D flipera s dodatkom svemirskih elemenata. Koristite leve i desne strelice za pomeranje krilaca, a Space taster za ispaljivanje kuglice. Osvojite poene tako što ćete pogoditi različite oblike:
- **30 poena** za planete
- **10 poena** za trapezoide
- **60 poena** za sestouglove

Cilj je sakupiti što više poena i sprečiti kuglicu da padne dole.

## Mehanika igre
### Pomeranje Kuglice
Ojlerove jednačine koriste se za modeliranje rotacije i translacije kuglice. Ovaj matematički pristup omogućava nam precizno praćenje kretanja kuglice u dvodimenzionalnom prostoru.

### Rotacija
Rotacija loptice zavisi od trenutne translacione brzine i pravca odbijanja od prepreka. Ovo se postiže primenom trigonometrijskih funkcija i vektorskih operacija. Dinamička rotacija doprinosi realističnosti i dinamici igre.

### Gravitacija
Gravitaciono ubrzanje zavisi od nagiba table, dok sila gravitacije zavisi od gravitacionog ubrzanja i mase loptice. Ovakav pristup omogućava da gravitacija postane faktor koji utiče na kretanje loptice u igri, stvarajući dodatni izazov.

### Pomeranje Loptice
Na početku igre, korisnik zadaje početnu silu koja ispaljuje lopticu uvis. Podešavanje ove sile postavlja ton za čitavu igru, gde precizno doziranje snage utiče na trajanje i visinu kretanja loptice.

### Kolizije
#### Separating Axis Theorem (SAT)
Separating Axis Theorem je algoritam za detekciju kolizija između poligona. Korišćenjem SAT-a, možemo precizno odrediti da li se dva objekta presecaju. Ovaj algoritam koristi se za detekciju kolizija sa poligonima u igri.

#### Kolizija sa linijom
Određuje se na osnovu razdaljine pozicije centra loptice od linije. Vektor odbijanja dobija se na osnovu vektora upada, koristeći refleksiju kako bi se simuliralo odbijanje od prepreke.

#### Kolizija sa krugom
Implementirana je koristeći geometrijske metode poput udaljenosti između tačaka. Ovo osigurava precizno detektovanje sudara sa krugovima u igri.

## Inspiracija Estetike
Igra je inspirisana svemirom, koristeći Space elemente za stvaranje jedinstvenog vizuelnog iskustva. Planete, zvezde i kosmički pejzaž dodaju šarm i originalnost fliperu.

🌌 **Spremite se za kosmičko putovanje kroz vasionu flipera!** 🚀


Uživajte u igri i osvojite najviše poena u svemirskom fliperu! 🌠

Autori - Studenti sa smera računarstvo i automatika:
1) Teodora Bečejac RA37/2021
2) Nataša Radmilović RA20/2021
