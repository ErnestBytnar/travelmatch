# 🌍 TravelMatch – inteligentna platforma do łączenia podróżników

**TravelMatch** to innowacyjna aplikacja webowa (i w przyszłości mobilna), która umożliwia znajdowanie towarzyszy podróży na podstawie kierunku, terminu, stylu podróżowania, preferencji i wspólnych zainteresowań. Dzięki algorytmom dopasowującym i inteligentnym filtrom, użytkownicy mogą bezpiecznie i świadomie zaplanować wspólne podróże z odpowiednimi osobami.

---

## 🎯 Misja projektu

> **Stworzyć bezpieczną, dopasowaną i przyjazną przestrzeń dla podróżników szukających towarzystwa – niezależnie od miejsca, stylu czy budżetu.**

---

## 💡 Co wyróżnia TravelMatch?

✅ **Dopasowanie przez algorytm** – znajdź osoby, które naprawdę pasują do Twojego stylu podróżowania  
✅ **Zautomatyzowany AI matching** (planowany) – wykorzystanie uczenia maszynowego lub embeddingów do trafniejszych propozycji  
✅ **Zaawansowane filtry i tryby prywatności** – np. widoczność tylko dla znajomych lub tryb anonimowy  
✅ **Wbudowany kalendarz wspólnych planów** – widzisz, kto gdzie i kiedy chce jechać  
✅ **Czat i zarządzanie planami** – komunikacja + ustalanie szczegółów podróży w jednym miejscu  
✅ **Bezpieczna weryfikacja profilu i opinii** – system ocen, weryfikacja tożsamości (planowane)

---

## 🧱 Stack technologiczny (v1 MVP)

| Warstwa         | Technologia               |
|------------------|---------------------------|
| Backend          | Django, Django REST Framework |
| Baza danych      | PostgreSQL                |
| Taski async      | Celery + Redis            |
| Konteneryzacja   | Docker + docker-compose   |
| Frontend         | React (planowany)         |
| Autoryzacja      | JWT + `dj-rest-auth`      |
| Testy            | Pytest + Faker + FactoryBoy |
| DevOps           | GitHub Actions, .env, pre-commit |
| AI Matching (v2) | OpenAI API / SentenceTransformers (planowane) |

---

## 🧠 Plan rozwoju (etapy)

### MVP (v1)
- Rejestracja/logowanie użytkownika
- Tworzenie profilu podróżnika (styl, język, budżet, preferencje)
- Przeglądanie i filtrowanie osób
- Prosty silnik dopasowania
- Czat + zaproszenia do podróży
- Zarządzanie planami i kalendarz

### Wersja PRO (v2+)
- AI matching (z embeddings, OpenAI, ML)
- System reputacji i opinii
- Powiadomienia push / e-mail
- Marketplace (np. wspólne koszty, noclegi, transport)
- Wersja mobilna (React Native)

---

## 📐 Architektura (skrót)

- `apps/users` – autoryzacja, profile, ustawienia prywatności  
- `apps/matching` – logika dopasowywania + system scoringowy  
- `apps/trips` – plany podróży, kalendarze, dostępność  
- `apps/chat` – prosty system wiadomości  
- `apps/common` – narzędzia wspólne, np. enums, utils

---

## 🔐 Bezpieczeństwo

- Weryfikacja e-mail i tożsamości
- Rate-limity, CSRF, CORS
- Tryb prywatny profilu (widoczność tylko dla znajomych)
- Moderacja treści i raportowanie

---

## 💸 Model biznesowy (planowany)

- Subskrypcja premium (dodatkowe filtry, AI match, widoczność)
- Promowane profile (Top miejsca w wynikach)
- Partnerstwa z hostelami, przewoźnikami, firmami outdoorowymi
- Płatne ogłoszenia wspólnych podróży (np. wyprawy zorganizowane)

---

## 🤝 Dla kogo to jest?

- Dla **solopodróżników**, którzy szukają ludzi do wspólnego odkrywania świata  
- Dla **cyfrowych nomadów**, którzy zmieniają lokalizację i chcą społeczności  
- Dla osób, które **nie chcą podróżować same**, ale też nie szukają typowego Tindera  
- Dla tych, którzy chcą **dzielić koszty podróży** lub organizować wyprawy grupowe  

---

## 🛠️ Jak uruchomić (dev)

```bash
# 1. Skopiuj repo
git clone https://github.com/yourname/travelmatch.git
cd travelmatch

# 2. Uruchom kontenery
docker-compose up --build

# 3. Wykonaj migracje
docker-compose exec web python manage.py migrate

# 4. Stwórz użytkownika admin
docker-compose exec web python manage.py createsuperuser
