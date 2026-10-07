# Dashboard « Suivi des inbox »

Fichier à utiliser : `dashboard-dossiers.html` (à la racine). L'ouvrir dans Edge/Chrome/Firefox par double-clic, en local.

- Aucune connexion réseau : la librairie de lecture Excel (SheetJS 0.18.5) est intégrée dans la page, et une politique CSP bloque tout envoi.
- Les données chargées (colonnes utiles uniquement) sont mémorisées dans le navigateur du poste (localStorage) : le détail des dossiers est effacé automatiquement après 30 jours, l'historique agrégé est conservé jusqu'à « Effacer les données mémorisées ». Case « Mémoriser » décochée = rien n'est conservé.
- Seules les colonnes En retard, Statut d'utilisateur, Date inbox, Type de transaction, Date de début, Personne responsable et ID de l'objet sont extraites. Description et Bénéficiaire ne sont jamais lues dans le modèle de données.
- Nom de fichier conseillé : `<COLLABORATEUR>_<prestation>.xlsx` (ex. `MJA_IC Droit.xlsx`, `MJA_IC PC.xlsx`, `MJA_VA.xlsx`). La date d'extraction de chaque fichier est la date présente dans le nom (`MJA_IC Droit_2026-10-06.xlsx`), sinon sa date de modification ; elle se corrige dans « (détails) ».
- L'historique est tenu par date × prestation × collaborateur ; la comparaison affiche les écarts par prestation puis par collaborateur (par défaut : dernière date vs date précédente).
- Routine hebdomadaire : déposer les extractions Excel, « Importer l'historique » (dernier CSV), consulter, puis « Terminer » : télécharge `historique_inbox_<date>.csv` (toutes les dates, chiffres agrégés par collaborateur, aucune donnée d'assuré) et efface tout du poste.

Modifier la page : éditer `tools/dashboard-dossiers.src.html`, puis `python3 tools/build-dashboard.py`.
