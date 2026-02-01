# 🚀 WORKFLOW SVILUPPO APP WEB CON CLAUDE + TEMPLATE DJANGO

**Template Base:** https://github.com/turiliffiu/demo_app  
**Versione Template:** v1.2.1  
**Metodo:** Passo-passo verificabile

---

## 📋 FASE 1: PIANIFICAZIONE

### Come Iniziare
```
Ciao Claude! Voglio creare [nome app].
Idea: [descrizione 2-3 righe]
Funzionalità: [elenco bullet]
```

### Claude Chiede
- Target utenti?
- Features principali?
- Integrazioni esterne?
- Scala prevista?

### Output Fase 1
- Schema entità
- Ruoli utente
- Roadmap MVP vs Future

---

## 📦 FASE 2: SETUP PROGETTO

### Server Sviluppo (Locale)
```bash
cd ~/Documenti
git clone https://github.com/turiliffiu/demo_app.git nome-progetto
cd nome-progetto
git remote remove origin
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Rinomina Progetto
```bash
mv myproject nome_progetto
# Aggiorna riferimenti in manage.py, wsgi.py, asgi.py
```

### Connetti GitHub
```bash
git remote add origin https://github.com/tuouser/repo.git
git push -u origin main
```

---

## 🏗️ FASE 3: SVILUPPO ITERATIVO

### Ciclo per Ogni Feature

1. **Claude fornisce codice:**
```bash
   cat << 'EOF' > app/models.py
   [codice]
   EOF
```

2. **Tu esegui e verifichi:**
```bash
   cat app/models.py | head -20
```

3. **Tu incolli output** → Claude verifica

4. **Ripeti per:** forms.py, views.py, urls.py, templates

5. **Migrations:**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

6. **Test locale:**
```bash
   python manage.py runserver 0.0.0.0:8000
```

7. **Feedback:** ✅ funziona o ⚠️ errore

8. **Commit:**
```bash
   git add .
   git commit -m "feat: [descrizione]"
   git push
```

---

## 🧪 FASE 4: TESTING
```bash
pytest app/tests/
```

Claude crea test per ogni feature.

---

## 🚀 FASE 5: DEPLOY

### Setup Iniziale (Una Volta)
```bash
git clone https://github.com/tuouser/repo.git /opt/progetto
cd /opt/progetto
sudo ./scripts/deploy.sh
```

### Aggiornamenti
```bash
cd /opt/progetto
git pull
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

---

## ✅ REGOLE WORKFLOW

1. **Ogni comando = output verificato**
2. **Nessun copia-incolla cieco**
3. **Debug immediato**
4. **Commit frequenti e descrittivi**
5. **Test prima di push**

---

## 📊 TEMPLATE SESSIONE TIPO

**Tu:**
```
Voglio creare [app] per [scopo].
Features: [lista]
```

**Claude:**
```
Pianificazione:
- Entità: [...]
- Ruoli: [...]
- MVP: [...]
Ok? Procediamo?
```

**Tu:** "Sì"

**Claude:** [Fornisce comandi step-by-step]

**Tu:** [Esegui, incolla output, feedback]

**Ciclo continua fino a feature completa**

---

## 🎯 TEMPLATE BASE INCLUDE

✅ Django 5.0 + Python 3.12+
✅ Auth + User Profiles + Roles
✅ REST API (DRF)
✅ Tailwind CSS + Alpine.js
✅ Rate limiting
✅ Security headers
✅ SQLite + PostgreSQL support
✅ Management commands
✅ pytest tests
✅ CI/CD GitHub Actions
✅ Deploy scripts

---

## 📁 STRUTTURA PROGETTO BASE
```
progetto/
├── apps/
│   ├── core/          # Auth, users, dashboard
│   └── api/           # REST API
├── myproject/         # Settings, URLs
├── templates/         # Global templates
├── static/            # CSS, JS, images
├── media/             # User uploads
├── scripts/
│   ├── setup.sh       # Dev setup
│   └── deploy.sh      # Production deploy
├── requirements.txt
├── .env.example
└── manage.py
```

---

## 🆕 AGGIUNGERE NUOVA APP
```bash
python manage.py startapp nome_app
```

Poi Claude fornisce:
- models.py
- forms.py
- views.py
- urls.py
- templates/
- tests/
- admin.py

---

## 💡 BEST PRACTICES

- Commenti in italiano
- Nomi variabili in inglese
- Un commit per feature
- Test per ogni view
- Rate limit su form critici
- Permessi per ogni view

---

**READY TO START!** 🚀
