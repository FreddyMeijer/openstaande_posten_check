# Materialized view voor openstaande posten controleren
's nachts wordt een tijdelijk rapport gemaakt van openstaande posten. Als iemand in de front-end het rapport opvraagt, wordt op de achtergrond dit tijdelijke rapport geraadpleegd. Het gedraagt zich als een materialized view. 

Soms wordt de materialized view niet goed aangemaakt en kan je het rapport niet draaien. Met onderstaand script kan je achterhalen op welke dagen de materialized view wel is gemaakt. 

## Installatie
- Een installatie van Python en GIT is noodzakelijk alvorens de volgende stappen te zetten.
- Open een terminal (of gebruik die van Visual Studio Code), navigeer naar de gewenste installatielocatie en gebruik `git clone https://github.com/FreddyMeijer/openstaande_posten_check.git`
- Open in de terminal de map waarin de repository gekloond is.
- Geef het commando `pip install -r openstaande_posten_check/requirements.txt`
- Draai `opvragen_files.py`

## Resultaten
Als het script gedraaid is, zal een bestand <i>allFiles.csv</i> opgeslagen worden in de root van het project. In deze CSV vind je de laatste 200 regels die aangemaakt zijn met als peildatum vandaag.