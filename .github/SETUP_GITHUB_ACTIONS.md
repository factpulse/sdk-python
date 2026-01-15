# Configuration GitHub Actions

## Secret PyPI requis

Pour que le déploiement automatique sur PyPI fonctionne, vous devez configurer le secret suivant dans les paramètres du repository :

1. Allez sur https://github.com/factpulse/sdk-python/settings/secrets/actions
2. Cliquez sur "New repository secret"
3. Nom : `PYPI_API_TOKEN`
4. Valeur : Votre token API PyPI (commence par `pypi-`)

### Comment obtenir un token PyPI ?

1. Créez un compte sur https://pypi.org/
2. Allez dans Account Settings > API tokens
3. Créez un nouveau token avec scope "Entire account" ou limitez-le au package "factpulse"
4. Copiez le token (il commence par `pypi-`)

## Workflow de déploiement

Le workflow `.github/workflows/publish-pypi.yml` se déclenche automatiquement quand vous créez un tag Git qui commence par `v` (exemple : `v1.0.0`).

### Processus automatique :
1. Build du package Python
2. Vérification avec twine
3. Publication sur PyPI
4. Création d'une GitHub Release avec les artefacts
