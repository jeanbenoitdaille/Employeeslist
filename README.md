# Employeeslist
Trier une liste d'employés 
Ici, nous faisons tout en une seule ligne grâce aux compréhensions de liste qui nous permettent de réaliser une boucle for avec une structure conditionnelle.

J'ai également enlevé l'étape qui consistait à calculer la moitié de l'alphabet. Comme je vous le disais dans la vidéo, on peut être sûr que la taille de l'alphabet ne changera pas demain, on utilise donc directement la valeur 13 dans notre slice, ce qui permet d'alléger un peu le code.

Vous pourriez vous demander pourquoi nous n'utilisons pas directement la constante ascii_uppercase du module string, ce qui nous éviterait d'avoir à convertir la première lettre en minuscule avec la méthode 'lower' ?

Eh bien tout simplement parce que si jamais un des prénom dans la liste ne commence pas par une majuscule, il ne sera pas pris en compte.
Je préfère donc forcer la conversion en lettre minuscule pour être absolument sur que l'on compare deux lettres en minuscule.

Pour commencer, je vous conseille toujours d'écrire un script de la façon la plus logique qui vous vient à l'esprit, sans forcément vous soucier de la longueur et / ou l'efficacité de votre script. Une fois que la logique de votre script est là, vous pouvez ensuite facilement passer par une petite étape d'optimisation pour essayer de réduire la longueur de votre script au maximum (tant que cela reste lisible bien sûr).
