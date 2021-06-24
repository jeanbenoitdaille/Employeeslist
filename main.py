import string
     
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]
     
alphabet = string.ascii_lowercase
employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]
     
print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))