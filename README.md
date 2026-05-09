# Projekti 1: Model SEIR me vaksinim dhe kontakt të varur nga sjellja kolektive

Ky repozitor përmban implementimin e një modeli epidemik SEIRV ku dinamika e infektimit ndikohet nga sjellja kolektive e popullatës dhe programet e vaksinimit. Ky projekt është zhvilluar si pjesë e kursit **"Modelim në Fizikë"**.

## 1. Qëllimi Shkencor
Qëllimi i këtij modeli është të studiohet se si reagimi njerëzor ndaj rrezikut (ulja e kontakteve) ndikon në parametrat kyç të një pandemie. Pyetja qendrore është: si ndryshon kulmi epidemik dhe koha e arritjes së tij kur popullata reagon duke ulur kontaktet bazuar në fraksionin e individëve infektivë?

## 2. Modeli Matematikor
Sistemi bazohet në ekuacionet diferenciale të zakonshme (ODE) për pesë grupe:
- **S (Susceptible):** Të ndjeshmit
- **E (Exposed):** Të ekspozuarit
- **I (Infectious):** Të infektuarit
- **R (Recovered):** Të shëruarit
- **V (Vaccinated):** Të vaksinuarit

### Ekuacionet kryesore:
$$\frac{dS}{dt} = -\beta_{eff}(t)SI - \nu S$$
$$\frac{dE}{dt} = \beta_{eff}(t)SI - \sigma E$$
$$\frac{dI}{dt} = \sigma E - \gamma I$$
$$\frac{dR}{dt} = \gamma I$$
$$\frac{dV}{dt} = \nu S$$

**Sjellja kolektive:** Norma efektive e kontaktit nuk është konstante, por funksion i infeksioneve aktuale:
$$\beta_{eff}(t) = \beta_0 [1 - \eta I(t)/N]$$
Ku $\eta$ është koeficienti i reagimit kolektiv.

## 3. Struktura e Projektit
```text
seirv_behavior_model/
├── src/
│   ├── models/seirv.py           # Logjika e ekuacioneve ODE
│   ├── analysis/metrics.py       # Llogaritja e pikut dhe kohës së pikut
│   └── visualization/plots.py    # Gjenerimi i figurave
├── scripts/
│   ├── run_default.py            # Simulim bazë pa/me vaksinim
│   └── scan_behavior.py          # Skanimi i parametrit eta (η)
├── results/
│   ├── figures/                  # Grafikët e gjeneruar
│   └── tables/                   # Metrikat numerike
├── report/
│   └── project_report.tex        # Raporti teknik
└── requirements.txt              # Varësitë (numpy, scipy, matplotlib)
