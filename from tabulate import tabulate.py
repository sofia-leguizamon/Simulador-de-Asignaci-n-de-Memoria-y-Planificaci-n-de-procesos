from tabulate import tabulate

d = [ ["Mark", 12, 95, 3],
     ["Jay", 11, 88, 5],
     ["Jack", 14, 90, 7]]

print(tabulate(d, headers=["ID", "Tamaño", "TA", "TI"]))