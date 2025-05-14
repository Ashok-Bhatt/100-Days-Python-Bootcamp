from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Squirtle","Bulbasaur","Charmander"])
table.add_column("Pokemon Type",["Water","Grass","Fire"])

table.align = "l"
print(table)