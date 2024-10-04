Quelques informations supplémentaires à destination d’un développeur qui souhaiterait reprendre 
/ transposer le développement de l’application : 
 L’application est développée en Python et comporte 5 fichiers :
o Extraction.py quise connecte au workspace et qui réalise l’extraction
o Gerer_workspace.pyqui s’occupe de l’affichage graphique et teste la connexion pour 
afficher Connecté ou Connexion impossible
o getColumn.py qui récupère le nom des colonnes du workspace et met à jour le JSON 
qui est utilisé pour télécharger la sauvegarde d'un certain workspace. Cela permet que 
si des champs changent dans un certain workspace, les nouveaux champs soient 
quand même mis à jour (ie. ce n’est plus en dur dans un JSON comme dans la méthode 
3)
o Save.py qui permet de sauvegarder le fichier et d’appeler la fonction de suppression 
o Clean.py qui supprime tous les fichiers du dossier workspace_name dont la date de 
modification est supérieure à DELAI_SUPPRESSION. DELAI_SUPPRESSION est 
paramétré à 30 jours en début de fichier.
 Les fichiers JSON au format export_options_NOM_WORKSPACE correspondent, pour chaque 
workspace, aux champs à extraire. Ces fichiers sont définis par get_column.py ET par le JSON 
default_attributes qui liste tous les champs communs à tous les workspaces (ex : id, card ref, 
parent id, title, is archived, state, …). En effet, lors de l’appel à l’API pour déterminer les 
colonnes à exporter (via getColum.py), l’API ne revoie que les champs créés dans ce 
workspace, et non pas les champs par défaut / commun. 
 Le fichier JSON workspace_to_save liste les workspaces pour lesquels l’export est réalisé. Il 
est compléter automatiquement lors de sa mise à jour via l’interface graphique vue en début 
de cette partie Méthode 4. Il pourrait aussi être complété manuellement à ce niveau en 
respectant bien les indentations.
 Le code est commenté dans chaque fichier 
