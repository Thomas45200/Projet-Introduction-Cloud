# Projet-Introduction-Cloud

Plateforme de diffusion de contenu statique via une API REST et une interface web.
Le contenu est stocké dans Azure Blob Storage et consommé par une application Flask.
Le projet est stocké avec Docker, déployé sur AKS et automatisé via GitHub Actions.

## Objectifs
- Exposer une API REST :
  - `GET /api/events`
  - `GET /api/news`
  - `GET /api/faq`
- Fournir des endpoints de santé :
  - `GET /healthz`
  - `GET /readyz`
- Mettre en cache les données pour limiter les appels au stockage.
- Stocker l’application.
- Déployer sur Kubernetes avec :
  - Namespace, Deployment, Service, Ingress, ConfigMap, Secret
  - Probes, resources, rolling update
- Automatiser CI/CD.

## Stack technique
- **Backend** : Python / Flask
- **Stockage contenu** : Azure Blob Storage
- **Container** : Docker
- **Registry** : GitHub Container Registry
- **Orchestration** : AKS
- **CI/CD** : GitHub Actions

## Structure du dépôt


## Lancement local
Les commandes exactes seront complétées une fois l’application implémentée.
- Installation des dépendances : `pip install -r requirements.txt`
- Lancement : `python -m app.main` (ou équivalent)
- Test : `pytest`

## Auteur
- Thomas BEAUBOIS IR4
