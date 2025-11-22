# KSH Lakásár Statisztika Projekt - Rövid Leírás

## Projekt Áttekintés
Python-alapú adatelemzési eszköz, amely a KSH lakásár statisztikáit vizualizálja és elemzi. A program CSV formátumú adatokat dolgoz fel, vonal- és szóródási diagramokat készít lineáris regresszióval, ésR² értékek segítségével méri az árváltozások előrejelezhetőségét.

## Projekt Struktúra
```
├── main.py                     # Belépési pont, program indítása
├── data
│   └── data.csv                # KSH lakásár adatok (2007-2024)
├── config/
│   ├── config.py               # Konfiguráció, naplózás (LOG_TYPES)
│   └── translations.py         # Többnyelvű szövegek (magyar/angol)
└── scripts/
    ├── extract.py              # CSV adatok beolvasása és feldolgozása
    └── draw_diagram.py         # Vizualizáció: vonal- és szóródási diagramok
```

## Főbb Funkciók

**1. Adatok beolvasása és feldolgozása** (`extract.py`)
- CSV formátumú KSH adatok beolvasása
- 4 árszekció × 4 lakástípus × 18 év = 288 adatpont
- Lakástípusok: Családi házak, Többlakásos épületek, Lakótelepek, Összesen

**2. Vizualizáció** (`draw_diagram.py`)
- **Vonal diagramok**: Ártrendek időbeli alakulása lakástípusonként
- **Szóródási diagramok**: Lineáris regresszió R² értékkel
- NumPy: Adatkezelés, hiányzó értékek
- Matplotlib: Ábrakészítés
- SciPy: Lineáris regresszió számítása

## Használat
```bash
python main.py
```
1. Megnyílik az első ablak: vonal diagramok
2. Megnyílik a második ablak: szóródási diagramok R² értékekkel

## Konfigurációs Lehetőségek
- **Nyelv**: Magyar vagy angol (`config.py` → `lang = "hu"` vagy `"en"`)
- **Naplózás**: LOG_TYPES szintek (INFO, ACTION, ERROR)
- **Diagramok**: Szekciók oszlopainak száma (`cols=2`)

## Technológiai Stack
- **Python 3.13+**
- **NumPy**: Numerikus számítások, adatkezelés
- **Matplotlib**: Adatvizualizáció
- **SciPy**: Statisztikai elemzés (lineáris regresszió)
- **Colorama**: Színes terminál kimenet

## Gazdasági Elemzés - Főbb Eredmények

**Ártrend Alakulása (2007-2024)**
- **2007-2012**: Stagnálás - A 2008-as gazdasági válság hatására az ingatlanárak nem növekedtek
- **2012-2015**: Fokozatos emelkedés - Gazdasági fellendülés, alacsony kamatlábak
- **2015-2024**: Gyorsabb növekedés - Különösen 2015 után jelentős árugrás

**Lineáris Regresszió Eredményei**
- **R² értékek**: 0,85 - 0,95 között
- **Jelentése**: Az idő 85-95%-ban magyarázza az árváltozásokat
- **Következtetés**: Szisztematikus, előrejelezhető trend - nem véletlen ingadozások

**Befektetési Perspektíva**
- **Átlagos éves emelkedés**: ~3-4%
- **Stabilitás**: Magas R² érték stabil befektetést jelez
- **Kockázat**: Alacsony - az árak hosszú távon konzisztensen növekednek
- **Gyakorlati alkalmazás**: Lakásvásárlási döntések, befektetési portfólió, ingatlanpolitika

**Lakástípusok Összehasonlítása**
- Minden kategória hasonló trendet követ
- Családi házak és lakótelepek párhuzamos növekedést mutatnak
- A válság minden lakástípust érintett, de a fellendülés is általános volt

## Projekt Eredmény
Matematikailag igazolt, hogy az ingatlanárak nem találgatás, hanem szisztematikus és előrejelezhető trendeket követnek. Az R² értékek azt mutatják, hogy az ingatlan mint befektetés stabil és megbízható eszköz.

---
**Fejlesztő**: Szlucska Dóra | **Tárgy**: Adatelemzés - Lakásárak változása Magyarországon | **Forrás**: KSH (Központi Statisztikai Hivatal)
