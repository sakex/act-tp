import base64

# num est un nombre entier
def is_a_prime_number(num):
    # Partie à compléter


# p est un nombre premier et message est une chaine de caractères
def fingerprinting(p, message):
    # Partie à compléter
    

# password est une chaine de caractères et your_details est un tuple avec le 
# format suivant (nombre premier, hash du mot de passe)
def login(password, your_details):
    return your_details[1] % your_details[0] == fingerprinting(your_details[0], password)



# Début de votre programme
password = "ceciestmonmotdepasse"
your_details = (19, hash(password))
success = login(password, your_details)

print("Connexion réussie? " + str(success))
if success:
    message = '''SmUgc2VyYWlzIGNvbmZpbsOpIGNoZXogbWVzIHBhcmVudHMgw
                    6AgbGEgY2FtcGFnbmUgbGVzIGRldXggcHJvY2hhaW5lIHNlbWF
                    pbmVzLCBldCBqZSBuJ2F1cmFpcyBwYXMgYWNjw6hzIMOgIEludGV
                    ybmV0LiDDgCBiaWVudMO0dCE='''
    print(base64.b64decode(message).decode())
