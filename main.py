import requests  

def get_all_models():
    # Această funcție returnează toate modelele de mașini din fișierul JSON de la server.
    response = requests.get('http://127.0.0.1:5000/api/title/')  # Trimite o cerere GET la API pentru a obține toate titlurile
    models = response.json()  # Convertim răspunsul primit 
    print("Toate modelele:")  
    for model in models:  # Parcurgem fiecare model din lista
        print(model)  # Afișăm modelul curent pe ecran

def search_by_name(keyword):  # Definim o funcție care permite căutarea după nume

    url = f'http://127.0.0.1:5000/api/cauta/title/{keyword}'  # Construim URL-ul pentru cerere folosind cuvântul cheie primit
    response = requests.get(url)  # Trimitem cererea GET la URL-ul format
    filtered_data = response.json()  # Convertim răspunsul JSON într-un obiect Python
    if filtered_data:  # Dacă lista nu este goală
        print(f"Modele găsite care conțin '{keyword}':\n")  # Afișăm un mesaj cu cuvântul cheie căutat

        for i, item in enumerate(filtered_data):
            # Afișăm fiecare proprietate a obiectului
            print(f"Name: {item['Name']}")
            print(f"Miles per Gallon: {item.get('Miles_per_Gallon', 'N/A')}")
            print(f"Cylinders: {item.get('Cylinders', 'N/A')}")
            print(f"Displacement: {item.get('Displacement', 'N/A')}")
            print(f"Horsepower: {item.get('Horsepower', 'N/A')}")
            print(f"Weight in lbs: {item.get('Weight_in_lbs', 'N/A')}")
            print(f"Acceleration: {item.get('Acceleration', 'N/A')}")
            print(f"Year: {item.get('Year', 'N/A')}")
            print(f"Origin: {item.get('Origin', 'N/A')}")
            if i < len(filtered_data) - 1:  # Dacă nu suntem la ultimul element, afișăm o linie separatoare, pentru a se citi mai ușor
                print("------------")

    else:  # Dacă nu s-au găsit modele
            print(f"Niciun model nu conține '{keyword}'.")
       

def main():
    while True:
        print("\nOpțiuni:")  # Afișăm un meniu basic
        print("1. Afișează toate modelele")
        print("2. Caută un model după nume")
        print("3. Ieși")
        choice = input("Alege o opțiune: ")  

        if choice == '1':
            get_all_models()  # Afișăm toate modelele
        elif choice == '2':
            keyword = input("Introdu cuvântul cheie pentru căutare: ")  
            search_by_name(keyword)  
        elif choice == '3':
            print("La revedere!")  
            break 
        else:
            print("Opțiune invalidă, încearcă din nou.") 

if __name__ == '__main__':
    main() 
