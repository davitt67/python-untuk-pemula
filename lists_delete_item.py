animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu dengan method "remove"
animals.remove("Bebek")
print(animals) # ['Ayam', 'Cicak']

# Menghapus item terakhir dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals) # ['Ayam', 'Bebek']

# Menghapus item berdasarkan posisinya (indexing) dengan "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals) # ['Bebek', 'Cicak']

# Menghapus semua item dengan method "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals) # []