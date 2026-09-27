# Pydantic Order Validator

## Projektbeskrivning

Detta projekt skapades som en fördjupningsuppgift inom kursen Fördjupning i Pythonprogrammering.

Syftet med projektet är att undersöka hur biblioteket Pydantic kan användas för datavalidering i Python. Programmet läser in orderdata från en CSV-fil, validerar varje rad mot en definierad modell och rapporterar vilka ordrar som är giltiga respektive ogiltiga.

Projektet demonstrerar hur Pydantic kan användas för att säkerställa datakvalitet innan data används vidare i ett system eller en analys.

---

## Funktioner

- Läser orderdata från CSV-fil
- Validerar data med Pydantic
- Kontrollerar datatyper
- Kontrollerar affärsregler
- Rapporterar valideringsfel
- Hanterar giltiga och ogiltiga ordrar separat

---

## Tekniker

- Python
- Pandas
- Pydantic
- Pytest

---

## Projektstruktur

```text
pydantic_orders_projekt/
│
├── data/
│   └── orders.csv
│
├── src/
│   └── pydantic_orders/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── models.py
│       └── validator.py
│
├── tests/
│   └── test_validator.py
│
├── README.md
├── Rapport.md
├── requirements.txt
└── pyproject.toml
```

---

## Datamodell

Projektet använder följande Pydantic-modell:

```python
class Order(BaseModel):
    order_id: int
    customer_id: int
    
    product_category: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    discount: float = Field(ge=0, le=1)
```

### Valideringsregler

| Fält | Regel |
|-------|--------|
| product_category | Måste vara minst 1 i längd |
| quantity | Måste vara större än 0 |
| unit_price | Måste vara större än 0 |
| discount | Måste vara mellan 0 och 1 |

---

## Exempel på data

### Giltig order

```csv
1,101,Electronics,2,499.99,0.10
```

### Ogiltig order

```csv
2,102,Books,-2,149.99,0.05
```

Denna order är ogiltig eftersom `quantity` är mindre än 0.

---

## Installation

### Klona repot

```bash
git clone <repository-url>
cd pydantic_orders_projekt
```

### Skapa och aktivera virtuell miljö

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Installera beroenden

```bash
pip install -r requirements.txt
```

---

## Kör programmet

```bash
python -m pydantic_orders
```

---

## Exempel på resultat

```text
Giltiga ordrar: 2
Ogiltiga ordrar: 3

Valideringsfel:

Rad 3:
quantity
Input should be greater than 0

Rad 4:
unit_price
Input should be greater than 0

Rad 5:
discount
Input should be less than or equal to 1
```

---

## Tester

Projektet innehåller automatiserade tester med Pytest.

Kör testerna med:

```bash
pytest
```

Om alla tester går igenom visas ett resultat liknande:

```text
=================== test session starts ===================
collected 3 items

tests/test_validator.py ...                      [100%]

=================== 3 passed ===================
```

---

## När passar Pydantic?

Pydantic passar bra när data behöver valideras innan den används vidare i ett system.

Vanliga användningsområden:

- API:er (t.ex. FastAPI)
- CSV-importer
- JSON-data
- Konfigurationsfiler
- Datakvalitetskontroller
- Integrationer mellan olika system

---

## Begränsningar

Pydantic är främst byggt för att validera objekt och modeller.

För mycket stora tabulära dataset kan det bli ineffektivt att skapa och validera ett objekt för varje rad. I sådana situationer är Pandas eller Pandera ofta bättre alternativ för tabulär datavalidering.

Pydantic bör därför ses som ett komplement till Pandas snarare än en ersättare.

---

## Lärdomar

Genom projektet har jag lärt mig:

- Hur Pydantic använder type hints för datavalidering
- Hur BaseModel används för att skapa modeller
- Hur Field används för att definiera valideringsregler
- Hur ValidationError kan användas för felhantering
- Hur Pandas och Pydantic kan kombineras för att förbättra datakvalitet

Projektet har också gett en bättre förståelse för när Pydantic är ett lämpligt verktyg och vilka begränsningar som finns vid arbete med större dataset.

---

## Författare

Daniel Rangmyr

Fördjupning i Pythonprogrammering  
EC Utbildning