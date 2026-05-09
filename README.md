# SEIRV Epidemic Model with Collective Behavior

[cite_start]Ky repozitor përmban implementimin e një modeli epidemik SEIRV ku dinamika e infektimit ndikohet nga sjellja kolektive e popullatës dhe programet e vaksinimit[cite: 33, 35]. [cite_start]Ky projekt është zhvilluar si pjesë e kursit **"Modelim në Fizikë"**[cite: 1].

## 1. Qëllimi Shkencor
[cite_start]Qëllimi i këtij modeli është të studiohet se si reagimi njerëzor ndaj rrezikut (ulja e kontakteve) ndikon në parametrat kyç të një pandemie[cite: 35, 36]. [cite_start]Pyetja qendrore është: si ndryshon kulmi epidemik dhe koha e arritjes së tij kur popullata reagon duke ulur kontaktet bazuar në fraksionin e individëve infektivë? [cite: 36]

## 2. Modeli Matematikor
[cite_start]Sistemi bazohet në ekuacionet diferenciale të zakonshme (ODE) për pesë grupe[cite: 38]:
- **S (Susceptible):** Të ndjeshmit
- **E (Exposed):** Të ekspozuarit
- **I (Infectious):** Të infektuarit
- **R (Recovered):** Të shëruarit
- **V (Vaccinated):** Të vaksinuarit

### [cite_start]Ekuacionet kryesore [cite: 39-43]:
$$\frac{dS}{dt} = -\beta_{eff}(t)SI - \nu S$$
$$\frac{dE}{dt} = \beta_{eff}(t)SI - \sigma E$$
$$\frac{dI}{dt} = \sigma E - \gamma I$$
$$\frac{dR}{dt} = \gamma I$$
$$\frac{dV}{dt} = \nu S$$

[cite_start]**Sjellja kolektive:** Norma efektive e kontaktit nuk është konstante, por funksion i infeksioneve aktuale[cite: 44]:
$$\beta_{eff}(t) = \beta_0 [1 - \eta I(t)/N]$$
[cite_start]Ku $\eta$ është koeficienti i reagimit kolektiv.

## [cite_start]3. Struktura e Projektit [cite: 12-29, 58-66]
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
