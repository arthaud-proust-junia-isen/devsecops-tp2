# Résultats SonarQube — analyse initiale

SonarQube Community Build 26.11.0.134175, profil Python « Sonar way core » (défaut, 232 règles).
Projet `tiwap`, 1 084 lignes de code analysées (Python + Dockerfile).

| Mesure | Valeur |
|---|---|
| Problèmes au total | 32 |
| Sécurité | 24 (note E) |
| Fiabilité | 8 (note C) |
| Maintenabilité | 6 (note A) |
| Sévérités | 2 Blocker, 16 High, 12 Medium, 8 Low |
| Security Hotspots | 0 |
| Quality Gate | OK (pas de « new code » sur une première analyse) |

## Problèmes de sécurité relevés

| Clé | Règle | Emplacement | Sévérité | Message |
|---|---|---|---|---|
| 9d8ccf55 | python:S6779 | app.py:29 | BLOCKER | Don't disclose "Flask" secret keys. |
| 87c393f1 | python:S8392 | app.py:913 | BLOCKER | Avoid binding the application to all network interfaces. |
| 69a740b0 | python:S4502 | app.py:28 | HIGH | Make sure disabling CSRF protection is safe here. |
| cdec085d | python:S4830 | app.py:723 | HIGH | Enable server certificate validation on this SSL/TLS connection. |
| edab0950 | python:S4830 | app.py:728 | HIGH | idem |
| ebc9f233 | python:S4830 | app.py:731 | HIGH | idem |
| 292e04cb | python:S5659 | helper/auth.py:39 | HIGH | Don't use a JWT token without verifying its signature. |
| 77e49768 | python:S4790 | helper/db_manager.py:47 | HIGH | Make sure that hashing data is safe here. |
| 34723869 | python:S4790 | helper/db_manager.py:55 | HIGH | idem |
| 40760006 | python:S4790 | helper/mongodb_manager.py:45 | HIGH | idem |
| b588232b | python:S4790 | vulnerabilities/SQLi.py:151 | HIGH | idem |
| e66e6fba | docker:S6470 | Dockerfile:4 | HIGH | Copying recursively might inadvertently add sensitive data to the container. |
| 2004b7b6 | python:S5247 | app.py:40 | MEDIUM | Make sure disabling auto-escaping feature is safe here. |
| 4e4af928 | python:S2245 | app.py:760 | MEDIUM | Make sure that using this pseudorandom number generator is safe here. |
| bc069b55 | python:S2068 | helper/mongodb_manager.py:68 | MEDIUM | "password" detected here, review this potentially hard-coded credential. |
| 8688e2ec | python:S2068 | helper/mongodb_manager.py:69 | MEDIUM | idem |
| 5ce3a354 | python:S2092 | app.py:848 | LOW | Cookie sans flag "secure". |
| 74cab957 | python:S3330 | app.py:848 | LOW | Cookie sans flag "HttpOnly". |
| 54bfc539 | python:S3330 | app.py:880 | LOW | idem |
| c5b2c241 | python:S2092 | app.py:880 | LOW | idem |
| 09f5ba21 | python:S3330 | app.py:898 | LOW | idem |
| 590bcb70 | python:S2092 | app.py:898 | LOW | idem |
| ff2da581 | python:S4507 | app.py:913 | LOW | Debug feature activée. |
| 1d5d8d27 | docker:S6471 | Dockerfile:1 | LOW | L'image "python" tourne en root. |

## Injection SQL

Aucun problème signalé dans `vulnerabilities/SQLi.py` en dehors du MD5 ligne 151.

- `python:S2077` (« SQL queries should not be dynamically formatted ») est active dans le profil par défaut, mais ne s'est pas déclenchée.
- `python:S3649` (injection SQL par analyse de propagation / taint analysis) n'existe pas dans l'édition Community (`Rule not found`).
