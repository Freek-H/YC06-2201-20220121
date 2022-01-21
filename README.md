# De les voor groep YC06-2201 op 21 januari 2022

## Gebruikte commands
### Windows only: welke Python versies staan geïnstalleerd
```powershell
py -0
```

### Nieuwe virtual environment installeren:
```powershell
py -m venv venv               # Windows optie 1
python -m venv venv           # Windows optie 2
py -3.10 -m venv venv         # Windows optie 3 (specifiek voor Python 3.10)
python3 -m venv venv          # MacOS en Linux
```

### Activeren van virtual environment
```powershell
.\venv\Scripts\activate       # Windows
```
```bash
source venv/bin/activate      # MacOS en Linux
```

### Installeren Jupyter Notebook
```powershell
pip install notebook
python -m pip install notebook  # Alternatief Windows
python3 -m pip install notebook # Alternatief MacOS en Linux
```

### Starten Jupyter Notebook
```powershell
jupyter notebook
python -m notebook            # Alternatief Windows
python3 -m notebook           # Alternatief MacOS en Linux
```

### Installeren andere packages, voor alternatieven zie het installeren van Jupyter notebook
```powershell
pip install pandas
pip install matplotlib
pip install flask
```

### Environment variabelen instellen windows
```powershell
$env:FLASK_APP = "app_naam"     # app naam
$env:FLASK_ENV = "development"  # development mode (automatisch herstarten bij het aanpassen van bestanden)
$env:FLASK_RUN_PORT = 5002      # Poort, handig als er conflicten zijn
```

### Environment variabelen instellen MacOS en Linux
```bash
export FLASK_APP=app_naam       # app naam
export FLASK_ENV=development    # development mode (automatisch herstarten bij het aanpassen van bestanden)
export FLASK_RUN_PORT=5002      # Poort, handig als er conflicten zijn
```
