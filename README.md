# TP2 : injection SQL dans TIWAP, détection avec SonarQube et correction

Le rendu du TP (analyse SonarQube, correction de l'injection SQL, tests, CI) est dans [RAPPORT.md](RAPPORT.md).

L'application analysée est [TIWAP](https://github.com/tombstoneghost/TIWAP), copiée dans `TIWAP/`. C'est un lab volontairement vulnérable.

## Lancer le projet

Créer le fichier `.env` à partir du modèle, puis changer le mot de passe :

```bash
cp .env.example .env
```

Démarrer PostgreSQL et SonarQube :

```bash
podman compose up -d
```

SonarQube répond sur http://127.0.0.1:9000 (premier login `admin` / `admin`, le mot de passe est à changer). Générer un jeton d'analyse dans My Account > Security, puis lancer le scan de `TIWAP/` :

```bash
SONAR_TOKEN=<jeton> podman compose --profile scan run --rm scanner
```
