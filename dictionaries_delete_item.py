firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 18
}

# Untuk menghapus item dari Dictionaries, kita bisa menggunakan method "pop"
# Kita wajib menyebutkan nama "key" jika menggunakan method "pop"
firstPerson.pop("age")
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika'}

# Untuk menghapus semua item, kita bisa menggunakan method "clear"
firstPerson.clear()
print(firstPerson) # {}