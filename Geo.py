import pandas as pd
import geoip2.database

# Chemin vers le fichier CSV contenant les IP
csv_file = 'chemin/vers/votre/fichier.csv'

# Chemin vers la base de données GeoLite2
geolite2_db = 'chemin/vers/GeoLite2-Country.mmdb'

# Charger le fichier CSV
df = pd.read_csv(csv_file)

# Assurez-vous que le fichier CSV a une colonne nommée 'ip' pour les adresses IP
if 'ip' not in df.columns:
    raise ValueError("Le fichier CSV doit contenir une colonne nommée 'ip'.")

# Initialiser le lecteur GeoLite2
reader = geoip2.database.Reader(geolite2_db)

# Fonction pour obtenir le pays à partir d'une IP
def get_country(ip):
    try:
        response = reader.country(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return 'Non trouvé'
    except Exception as e:
        return str(e)

# Appliquer la fonction à la colonne 'ip'
df['country'] = df['ip'].apply(get_country)

# Sauvegarder le résultat dans un nouveau fichier CSV
output_csv_file = 'chemin/vers/le/fichier_de_sortie.csv'
df.to_csv(output_csv_file, index=False)

print(f"Les pays ont été ajoutés et sauvegardés dans {output_csv_file}")
