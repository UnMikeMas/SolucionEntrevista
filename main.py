# Miguel Angel Gaona Sanchez 24/03/2023

import pandas as pd

data = pd.read_csv("Recursos - Tabellenblatt1.csv")

# Reto 1
data['Nombre comercial'] = data['Nombre comercial'].str.lower()

# Reto 2
data['Fecha de Emisión'] = data['Fecha de Emisión'].str.replace('*','/')
data['Fecha Vencimiento'] = data['Fecha Vencimiento'].str.replace('-','/')

data["Fecha de Emisión"] = pd.to_datetime(data["Fecha de Emisión"])
data["Fecha Vencimiento"] = pd.to_datetime(data["Fecha Vencimiento"])

data["Fecha de Emisión"] = data['Fecha de Emisión'].dt.strftime('%d/%m/%Y')
data["Fecha Vencimiento"] = data['Fecha Vencimiento'].dt.strftime('%d/%m/%Y')

# Reto 3

data['Forma Farmacéutica'] = data['Forma Farmacéutica'].str.upper()

# Reto 4

data.rename(columns={"0":"Registro"}, inplace=True)

# Reto 5

data["Registro"] = data['Registro'].drop_duplicates(keep="last")
print(data)

# Reto 6

data['Laboratorio'] = data['Laboratorio'].str.replace(', S.A. de C.V.','')

# Reto 7

data['Tipo de Sociedad'] = data['Tipo de Sociedad'].str.split(', ').str[1]

data.to_csv("Excel_Resuelto.csv")