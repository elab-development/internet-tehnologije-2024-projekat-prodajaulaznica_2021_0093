# 🏀 Aplikacija za prodaju ulaznica – Partizan Evroliga

Full-stack web aplikacija za online prodaju ulaznica za utakmice košarkaškog kluba Partizan u okviru Evrolige. Implementirana korišćenjem **Django (REST API)** na backend strani i **React** na frontend strani.

---

## ⚙️ Kako pokrenuti projekat lokalno


1. Kloniraj repozitorijum

```bash
git clone https://github.com/korisnicko-ime/ime-repozitorijuma.git
cd ime-repozitorijuma

python -m venv env
source env/bin/activate        # Za Linux/macOS
env\Scripts\activate           # Za Windows

2. Pokretanje Django backend-a

-->Aktiviraj virtuelno okruzenje<--
python -m venv env
source env/bin/activate        # Za Linux/macOS
env\Scripts\activate           # Za Windows

-->Instalirati requirements<--

pip install Django djangorestframework djangorestframework-simplejwt reportlab pytz

-->Pokreni migracije<--
python manage.py migrate

-->Pokreni backend server<--
python manage.py runserver

Backend će biti dostupan na http://127.0.0.1:8000/

3. Pokretanje React frontend-a

cd frontend
npm install
npm start

Frontend aplikacija će se pokrenuti na http://localhost:3000/

🚀 Funkcionalnosti
✅ Prikaz liste narednih utakmica Partizana

✅ Registracija i login korisnika (JWT autentifikacija)

✅ Kupovina karata po kategorijama (tribine, loža, parter)

✅ PDF generisanje kupljenih karata

✅ Pregled svih prethodnih kupovina za ulogovanog korisnika

✅ Zaštićeni pristup funkcionalnostima na osnovu tokena

🧱 Tehnologije
Backend: Python, Django, Django REST Framework, JWT

Frontend: React, React Router, Axios

Baza: SQLite (lokalni razvoj)

PDF generacija: ReportLab (Python)

Autentifikacija: JWT (rest_framework_simplejwt)







