import pandas as pd

"""
Tohle slouží jako studijní materiáli 

"""


#------------------------------------------------
# Příklad DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Skupinování a agregace dat
grouped = df.groupby('A').sum()
print(grouped)

#------------------------------------------------

# Příklad DataFrame
data = {"jméno": ["adel", "kiki", "mama"],
        "věk" : [16, 18, 45],
        "oblíbené zvíře" : ["lorninka", "lorninka", "Julie"],
        "pohlaví": ["žena", "žena", "žena"],
        "vzděláni": ["student", "student","pracuje"],
        "ob. číslo":[34, 653, 357]}

# Výběr sloupce 'věk' můžeš si zvolit jakýkoliv sloupec zezhora, který sis stanovila
df = pd.DataFrame(data)
vek_sloupec = df["věk"]


print(vek_sloupec)                

#------------------------------------------------

# Příklad DataFrame
data = {"jméno": ["adel", "kiki", "mama"],
        "věk" : [16, 18, 45],
        "oblíbené zvíře" : ["lorninka", "lorninka", "Julie"],
        "pohlaví": ["žena", "žena", "žena"],
        "vzděláni": ["student", "student","pracuje"],
        "ob. číslo":[34, 653, 357]}

# Výběr sloupce 'věk' můžeš si zvolit jakýkoliv sloupec zezhora, který sis stanovila
df = pd.DataFrame(data)
vek_sloupec_filtr = df[df["věk"] > 19]

"""
Můžeš samozřejmě použít i string
jmeno1_sloupec_filtr = df[df["jméno"] == "kiki"]

jmeno2_sloupec_filtr = df[df["jméno"] > "adel"]

"""

print(vek_sloupec_filtr)


#------------------------------------------------

# Příklad DataFrame
data = {'name': ['John', 'Emily', 'Kate'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Výběr řádků, ve kterých je hodnota v sloupci 'age' větší než 30
first_row_loc = df.loc[2]
print(first_row_loc)


#------------------------------------------------

# Příklad DataFrame
data = pd.read_csv("studenti1.csv")
df = pd.DataFrame(data)
# Zde se filtruje obor a prospěch
filtr_obor = df[(df["obor"] == "softwarové inženýrství") & (df["prospěch"] > 1.4)]
# Počítání nalezených objektů
pocet_objektu = len(filtr_obor)
#následné vypsání
print(filtr_obor,"\n","Počet vyhledaných objektů:", pocet_objektu)
#------------------------------------------------

# Příklad DataFrame
data = pd.read_csv("studenti1.csv")
df = pd.DataFrame(data)

cistení_dat = df.dropna()

print(cistení_dat)


#------------------------------------------------

# Příklad DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Výpočet popisných statistik
print(df.mean())  # Průměr
print(df.median())  # Medián
print(df.std())  # Směrodatná odchylka
print(df.min())  # Minimální hodnota
print(df.max())  # Maximální hodnota
print(df.describe())  # Výpis rozšířeného popisu

#------------------------------------------------


# Skupinování a agregace dat
grouped = df.groupby('A').sum()
print(grouped)

# Křížová tabulka
cross_tab = pd.crosstab(df['A'], df['B'])
print(cross_tab)

# Výběr a extrakce dat
subset = df[df['A'] > 2]
print(subset)

#------------------------------------------------

# Příklad DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Aplikace aritmetické operace na sloupci
df['C'] = df['A'] + df['B']

# Aplikace matematické funkce na sloupec
df['D'] = df['B'].apply(lambda x: x ** 2)

# Aplikace vlastní uživatelské funkce na sloupec
def my_function(x):
    return x * 2

df['E'] = df['A'].apply(my_function)

print(df)


