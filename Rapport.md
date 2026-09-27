# Pydantic för datavalidering i Python

## Syfte

Syftet med denna fördjupning var att undersöka hur biblioteket Pydantic kan användas för datavalidering i Python. Jag ville förstå hur Pydantic använder type hints och modeller för att kontrollera att data har rätt struktur och innehåll.

För att praktiskt demonstrera tekniken utvecklade jag ett mindre projekt som läser orderdata från en CSV-fil och validerar varje rad mot fördefinierade regler. Målet var inte enbart att bygga ett fungerande program utan också att förstå när Pydantic är ett lämpligt verktyg och vilka begränsningar som finns.

---

## Området och dess relevans

Datavalidering handlar om att kontrollera att data är korrekt innan den används vidare i ett system eller en analys. Felaktiga värden kan leda till problem i programvara, databaser och analyser. Därför är datakvalitet en viktig del av både mjukvaruutveckling och data science.

För en Data Scientist är detta särskilt relevant eftersom analyser ofta bygger på data från externa källor, exempelvis CSV-filer, databaser eller API:er. Om datan innehåller felaktiga värden riskerar resultaten att bli missvisande.

Pydantic är ett bibliotek som används för att säkerställa datakvalitet genom att validera data mot definierade regler. Biblioteket används bland annat tillsammans med FastAPI och är därför vanligt förekommande i moderna Pythonprojekt.

---

## Viktiga begrepp

### Pydantic

Pydantic är ett Pythonbibliotek för datavalidering som bygger på Python type hints. Biblioteket används för att definiera modeller som beskriver hur giltig data ska se ut.

### BaseModel

BaseModel är basklassen som används för att skapa modeller i Pydantic. När en klass ärver från BaseModel får den automatiskt stöd för validering.

Exempel:

```python
class Order(BaseModel):
    order_id: int
```

### Type hints

Type hints används för att beskriva vilka datatyper som förväntas.

Exempel:

```python
quantity: int
```

Detta innebär att värdet förväntas vara ett heltal.

### Field

Field används för att definiera ytterligare regler för ett fält.

Exempel:

```python
quantity: int = Field(gt=0)
```

Här måste värdet vara större än noll.

### ValidationError

När data inte uppfyller reglerna genererar Pydantic ett ValidationError som beskriver vad som är fel.

---

## Genomförande

För att undersöka Pydantics funktionalitet utvecklade jag ett program som läser in orderdata från en CSV-fil och validerar innehållet.

Jag använde följande bibliotek:

- Pandas för att läsa CSV-filen
- Pydantic för datavalidering
- Pytest för tester

Projektets arbetsflöde kan beskrivas enligt följande:

```text
CSV-fil
   ↓
Pandas
   ↓
Pydantic-modell
   ↓
Validering
   ↓
Resultat
```

Ordermodellen definierades enligt följande:

```python
class Order(BaseModel):
    order_id: int
    customer_id: int
    
    product_category: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    discount: float = Field(ge=0, le=1)
```

Modellen definierar både datatyper och valideringsregler. Quantity och unit_price måste vara större än noll medan discount måste ligga mellan 0 och 1.

Varje rad från CSV-filen omvandlas till en dictionary och skickas till modellen:

```python
order = Order(**row.to_dict())
```

När objektet skapas utför Pydantic automatiskt valideringen.

En utmaning under arbetet var att förstå hur Pandas och Pydantic kunde användas tillsammans. Efter att ha arbetat med `row.to_dict()` och uppackning med `**` blev det tydligare hur data från en DataFrame kan omvandlas till Pydantic-objekt för validering.

---

## Resultat

Programmet kunde identifiera både giltiga och ogiltiga ordrar i testdatasetet.

Resultatet från körningen blev:

```text
Giltiga ordrar: 2
Ogiltiga ordrar: 3
```

De fel som upptäcktes var:

- Negativ kvantitet
- Negativt pris
- Rabatt större än 100 %

Exempel på felmeddelande:

```text
quantity
Input should be greater than 0
```

Resultatet visar att Pydantic effektivt kan användas för att upptäcka felaktiga värden innan data används vidare i ett system.

Genom arbetet blev det också tydligt att Pydantic inte bara handlar om datatyper utan om att definiera regler för hur giltig data ska se ut.

---

## Begränsningar och möjliga förbättringar

En begränsning är att Pydantic främst är utvecklat för objektbaserad validering. I detta projekt skapades ett Pydantic-objekt för varje rad i datasetet.

För mindre dataset fungerar detta bra, men för mycket stora tabulära dataset kan det bli mindre effektivt eftersom varje rad måste behandlas separat.

För sådana situationer kan bibliotek som Pandera vara mer lämpliga eftersom de är utvecklade för att validera hela DataFrames.

Om projektet skulle vidareutvecklas skulle jag vilja:

- lägga till egna validerare
- generera mer detaljerade felrapporter
- validera fler typer av affärsregler
- undersöka integration med FastAPI

---

## Koppling till yrkesrollen

Datavalidering är relevant för flera dataroller, bland annat Data Scientist, Data Analyst och Data Engineer.

Inom data science är datakvalitet avgörande eftersom analyser och modeller endast är så bra som den data de bygger på. Genom att validera data innan analys kan många problem upptäckas tidigt.

Pydantic kan användas för att kontrollera data som kommer från API:er, CSV-filer eller andra externa system innan den lagras eller analyseras. Detta kan bidra till mer tillförlitliga analyser och minska risken för felaktiga resultat.

För mig som studerar till Data Scientist var det därför relevant att undersöka hur datavalidering fungerar och hur verktyg som Pydantic kan användas för att förbättra datakvalitet i praktiska projekt.

---

## Källor

1. Pydantic Documentation  
   https://docs.pydantic.dev/

2. Pydantic Concepts – Models and Validation  
   https://docs.pydantic.dev/latest/concepts/models/

3. Pandas Documentation  
   https://pandas.pydata.org/docs/



---


# Självreflektion

## 1. Vad lärde du dig som du inte kunde innan?

Innan detta arbete hade jag begränsad erfarenhet av Pydantic och datavalidering i Python. Genom projektet har jag lärt mig hur Pydantic använder type hints tillsammans med BaseModel för att validera data automatiskt. Jag har också fått en bättre förståelse för hur valideringsregler kan definieras med hjälp av Field och hur ValidationError används för att hantera felaktig data.

Jag har dessutom lärt mig hur Pydantic kan kombineras med Pandas för att validera data som läses in från CSV-filer. Tidigare hade jag främst använt Pandas för att läsa och bearbeta data, men nu förstår jag hur Pydantic kan användas för att förbättra datakvaliteten innan analysen påbörjas.

---

## 2. Vad var svårast att förstå eller genomföra?

Det svåraste var att förstå hur Pandas och Pydantic kunde användas tillsammans. Jag förstod relativt snabbt hur en Pydantic-modell definieras, men det tog längre tid att förstå hur varje rad i en DataFrame kunde omvandlas till ett Pydantic-objekt genom:

```python
order = Order(**row.to_dict())
```

Jag behövde också sätta mig in i hur uppackning med `**` fungerar och hur Pydantic använder informationen för att validera datan.

---

## 3. Vilket tekniskt val är du mest nöjd med och varför?

Det tekniska val jag är mest nöjd med är att använda en separat Pydantic-modell för orderdata. Genom att samla alla regler på ett ställe blev lösningen tydligare och lättare att underhålla.

Istället för att skriva flera manuella kontroller i olika delar av programmet kunde valideringsreglerna definieras direkt i modellen. Detta gjorde koden mer lättläst och gav dessutom tydliga felmeddelanden när data inte uppfyllde kraven.

---

## 4. Vad hade du gjort annorlunda om du började om?

Om jag började om hade jag sannolikt undersökt Pydantics dokumentation mer ingående redan från början. Jag hade då snabbare förstått vissa centrala begrepp och kunnat planera projektet mer effektivt.

Jag hade också velat jämföra Pydantic med andra lösningar för datavalidering, exempelvis Pandera, för att få en djupare förståelse för när olika verktyg är mest lämpliga.

---

## 5. Vad skulle vara ett naturligt nästa steg om du fortsatte arbetet?

Ett naturligt nästa steg skulle vara att utforska mer avancerade funktioner i Pydantic, exempelvis egna validerare, nästlade modeller och generering av JSON-scheman.

Jag skulle även vilja undersöka hur Pydantic används tillsammans med FastAPI eftersom detta är ett vanligt användningsområde i verkliga Pythonprojekt. Det hade gett en bättre förståelse för hur datavalidering används i större system.

---

## 6. Vilket betyg tycker du själv att arbetet motsvarar – G eller VG?

Jag bedömer att arbetet motsvarar betyget **G**.

---

## 7. Motivera din bedömning genom att koppla till kraven för G och VG

Jag anser att arbetet uppfyller kraven för G eftersom jag har undersökt ett relevant tekniskt område, utvecklat ett fungerande projekt och visat förståelse för de centrala begreppen inom Pydantic. Jag kan förklara hur biblioteket fungerar, vilka problem det löser och hur det användes i min lösning.

Jag har också diskuterat både användningsområden och begränsningar samt kopplat tekniken till Data Science-yrkesrollen.

Däremot anser jag inte att arbetet fullt ut motsvarar VG. För att nå den nivån hade jag behövt genomföra en djupare teknisk analys, jämföra flera alternativa lösningar och utforska mer avancerade funktioner inom Pydantic. Projektet fokuserar främst på grundläggande datavalidering och syftet har varit att skapa en stabil förståelse för bibliotekets kärnfunktioner.

Sammantaget tycker jag att arbetet visar god förståelse för ämnet och uppfyller målen för ett godkänt arbete.


