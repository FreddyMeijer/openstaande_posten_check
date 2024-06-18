# Materialized view voor openstaande posten controleren
's nachts wordt een tijdelijk rapport gemaakt van openstaande posten. Als iemand in de front-end het rapport opvraagt, wordt op de achtergrond dit tijdelijke rapport geraadpleegd. Het gedraagt zich als een materialized view. 

Soms wordt de materialized view niet goed aangemaakt en kan je het rapport niet draaien. Met onderstaand script kan je achterhalen op welke dagen de materialized view wel is gemaakt. 

## Installatie
- Een installatie van Python en GIT is noodzakelijk alvorens de volgende stappen te zetten.
- Open een terminal (of gebruik die van Visual Studio Code), navigeer naar de gewenste installatielocatie en gebruik `git clone https://github.com/FreddyMeijer/openstaande_posten_check.git`
- Open in de terminal de map waarin de repository gekloond is.
- Geef het commando `pip install -r openstaande_posten_check/requirements.txt`
- Draai `opvragen_files.py`

## config.py
Om de code goed uit te voeren is het noodzakelijk dat een bestand wordt opgenomen met de naam config.py. Hierin vind je de volgende informatie:

```python
url = xxxxxx
authProfileUuid = yyyyyyy
username = zzzzzzz
password = wwwwwww
```

Hierbij geldt dat de url gevuld wordt met de endpoint van de GraphQL playground van de betreffende omgeving. `authProfileUuid` is de unieke ID van de rol die probeert in te loggen. `username` en `password` spreken voor zichzelf. Als `config.py` mist, krijg je een error:

```python
Traceback (most recent call last):
  File "...\opvragen_files.py", line 12, in <module>   
    header = token()
             ^^^^^^^
  File "...\function_token_PAL21.py", line 24, in token
    bearer = 'Bearer ' + responseParsed['data']['login']['jwtToken']
                         ~~~~~~~~~~~~~~^^^^^^^^
KeyError: 'data'
```
<b>config.py is niet opgenomen in de respository in verband met beveiliging</b>

## Resultaten
Als het script gedraaid is, zal een bestand <i>allFiles.csv</i> opgeslagen worden in de root van het project. In deze CSV vind je de laatste 200 regels die aangemaakt zijn met als peildatum vandaag.