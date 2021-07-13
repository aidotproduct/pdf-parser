import tabula
# import pandas as pd
# import camelot

file = "/home/milind/Python/Documents/CapitaGainStatement_3374554_PY_NOPASS.pdf"

tables = tabula.read_pdf(file, pages = "all", multiple_tables = True, stream=True)

# tabula.convert_into(file, "/home/milind/Python/to/iris_all.csv", all = True, password="AAYPC8552D")
print(tables[1])

#print(tables[2])


