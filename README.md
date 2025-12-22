# ML Deployment Pipeline 

Dieses Repository enthält den **Quellcode und die Konfigurationsdateien** für eine Machine-Learning-Deployment-Pipeline.

---

## Überblick

Die Pipeline stellt ein vortrainiertes Machine-Learning-Modell über eine REST-API bereit.
Sie umfasst:

- Laden eines ML-Modells
- Bereitstellung als Webservice (FastAPI)
- Containerisierung mit Docker
- Automatisierte Tests
- CI-Pipeline mit GitHub Actions

---

## Projektstruktur

```text
.
├── src/
│   └── app/
│       ├── main.py
│       └── model/
│           └── housing_pipeline.pkl
│
├── tests/
│   └── test_api.py
│
├── docker/
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Datei- und Ordnerbeschreibung

### `src/app/main.py`
- Einstiegspunkt der FastAPI-Anwendung
- Initialisiert die API
- Lädt das trainierte Machine-Learning-Modell
- Definiert API-Endpunkte (z. B. `/health`, `/predict`)
- Führt Vorverarbeitung und Inferenz durch

---

### `src/app/model/housing_pipeline.pkl`
- Serialisiertes Scikit-Learn-Pipeline-Objekt
- Enthält Feature-Engineering, Vorverarbeitung und Modell
- Wird beim Start der Anwendung geladen

---

### `tests/test_api.py`
- Automatisierte Tests mit Pytest
- Überprüft:
  - Erreichbarkeit der API
  - Korrekte Antwortformate
  - Fehlerbehandlung

---

### `docker/Dockerfile`
- Definiert das Docker-Image der Anwendung
- Installiert Abhängigkeiten
- Kopiert Quellcode und Modell
- Startet die API mit Uvicorn

---

### `.github/workflows/ci.yml`
- CI-Workflow für GitHub Actions
- Führt Tests bei jedem Push aus
- Dient der automatisierten Qualitätssicherung

---

### `requirements.txt`
- Liste aller Python-Abhängigkeiten
- Wird lokal, im CI und im Docker-Build verwendet

---

## Lokale Ausführung

### Voraussetzungen
- Python ≥ 3.10
- Optional: Docker

### Installation
```bash
pip install -r requirements.txt
```

### Start der API
```bash
uvicorn src.app.main:app --reload
```


