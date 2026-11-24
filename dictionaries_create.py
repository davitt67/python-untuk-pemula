# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 18
}

# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name']) # Hana
# Cara kedua dengan method "get"
print(firstPerson.get("age")) # 18

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['first_name', 'last_name', 'age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values()) # dict_values(['Hana', 'Malika', 18])