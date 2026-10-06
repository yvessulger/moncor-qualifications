# Dashboard « Suivi des inbox »

Fichier à utiliser : `dashboard-dossiers.html` (à la racine). L'ouvrir dans Edge/Chrome/Firefox par double-clic, en local.

- Aucune connexion réseau : la librairie de lecture Excel (SheetJS 0.18.5) est intégrée dans la page, et une politique CSP bloque tout envoi.
- Seules les colonnes En retard, Statut d'utilisateur, Date inbox, Type de transaction, Date de début, Personne responsable et ID de l'objet sont extraites. Description et Bénéficiaire ne sont jamais lues dans le modèle de données.
- Nom de fichier conseillé : `<COLLABORATEUR>_<prestation>.xlsx` (ex. `MJA_IC droit.xlsx`) : la partie après le premier `_` sert de filtre « Prestation ».
- L'export « instantané » produit un CSV agrégé (par collaborateur, sans donnée d'assuré) à recharger les jours suivants pour la tendance.

Modifier la page : éditer `tools/dashboard-dossiers.src.html`, puis `python3 tools/build-dashboard.py`.
