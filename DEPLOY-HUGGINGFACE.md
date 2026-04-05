# Déploiement sur Hugging Face Spaces

## Étapes

1. Créer un compte sur [huggingface.co](https://huggingface.co) si pas déjà fait
2. Aller sur **New Space** → choisir **Docker** comme SDK
3. Connecter ce repo GitHub (`tolmod/dataline`)
4. Dans les **Settings > Variables and Secrets** du Space, ajouter :
   - `ALLOWED_ORIGINS` = `https://TON_USERNAME-TON_SPACE_NAME.hf.space`
   - (optionnel) `AUTH_USERNAME` = ton login
   - (optionnel) `AUTH_PASSWORD` = ton mot de passe
5. HF va builder et déployer automatiquement — attendre ~5 min
6. L'app est accessible à `https://TON_USERNAME-TON_SPACE_NAME.hf.space`

## Notes

- Les données (connexions, historique) sont conservées tant que le Space n'est pas rebuild
- L'app reste active 24/7 sur le plan gratuit (pas de mise en veille)
- Pour une utilisation privée, activer `AUTH_USERNAME` et `AUTH_PASSWORD`
