def affiche_fichier(entree):
	f = open(entree, 'r')
	print(f.read())
	f.close()


def affiche_fichier_un_mot_par_ligne(entree):
	f = open(entree, 'r')
	text = f.read()
 
	for w in text.split(' '):
		print(w)
	f.close()

 
def affiche_derniere_lettre(entree):
	f = open(entree, 'r')
	text = f.read()
	print(f"Last symbol: {text[-1]}")
	f.close()

 
def affiche_derniere_ligne(entree):
	f = open(entree, 'r')
	lines = f.read().splitlines()
	print(f"Last line: {lines[-1]}")
	f.close()


def ajoute_etoiles_fin(sortie):
    f = open(sortie, 'a')
    f.write('\n*****')


def ajoute_etoiles_debut(sortie):
	f = open(sortie, 'r')
	text = f.read()
	f.close()
 
	f = open(sortie, 'w')
	f.write("*****\n" + text)


def retire_caracteres(entree, sortie, caracteres):
	f = open(entree, 'r')
	text = f.read()
	f.close()

	text = "".join([c for c in text if c not in caracteres])

	f = open(sortie, 'w')
	f.write(text)
	f.close()


# retire_mot utils

def my_trim(text):
	f_chars = (',', '.', '\n')
	return "".join([c for c in text if c not in f_chars]).strip().lower()

def write(n, t):
	f = open(n, 'w')
	f.write(t)
	f.close()

def retire_mot(entree, sortie, mot: str):
	f = open(entree, 'r')
	wds = f.read().replace('\n', ' [t] ').split(' ')
	f.close()
	
	f_wds = " ".join([w for w in wds if my_trim(w) != my_trim(mot)]) 
	text = f_wds.replace(' [t] ', '\n').replace('[t] ', '\n')
	write(sortie, text)

if __name__ == '__main__':
	filename = 'LMCO.txt'

	# affiche_fichier_un_mot_par_ligne(filename)
	# affiche_derniere_lettre(filename)
	# affiche_derniere_ligne(filename)
	# ajoute_etoiles_fin(filename)
	# ajoute_etoiles_debut(filename)
	# retire_caracteres(filename, 'test.txt', [',', 'l', 'O', '.'])
	retire_mot(filename, 'test.txt',  'ah')