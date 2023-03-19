from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokeymon", "Types"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmender", "Fire"])
table.add_row(["Squirtle", "Water"])

table.align = "c"
print(table)
