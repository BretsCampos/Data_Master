import pandas as pd
import sqlalchemy
import pymysql
import os

enem = pd.read_csv("/raw-data/MICRODADOS_ENEM_2020.csv", sep=';', low_memory=False, nrows=2000, dtype=str,  encoding='latin-1')

# TP_SEXO = sexo
# TP_FAIXA_ETARIA = faixa etaria
# TP_COR_RACA = raca
# Q006 = renda familiar
# Q005 = numero de pessoas na residencia
# TP_ESCOLA = tipo de escola do Ensino Medio

enem = enem[['TP_SEXO', 'TP_FAIXA_ETARIA', 'TP_COR_RACA', 'Q006', 'Q005', 'TP_ESCOLA']]

enem["SEXO"] = enem.TP_SEXO.replace({
    "M": "Masculino",
    "F": "Feminino"
})

enem["FAIXA_ETARIA"] = enem.TP_FAIXA_ETARIA.replace({
    "1": "Menor de 17 anos",
    "2": "17 anos",
    "3": "18 anos",
    "4": "19 anos",
    "5": "20 anos",
    "6": "21 anos",
    "7": "22 anos",
    "8": "23 anos",
    "9": "24 anos",
    "10": "25 anos",
    "11": "Entre 26 e 30 anos",
    "12": "Entre 31 e 35 anos",
    "13": "Entre 36 e 40 anos",
    "14": "Entre 41 e 45 anos",
    "15": "Entre 46 e 50 anos",
    "16": "Entre 51 e 55 anos",
    "17": "Entre 56 e 60 anos",
    "18": "Entre 61 e 65 anos",
    "19": "Entre 66 e 70 anos",
    "20": "Maior de 70 anos"
})

enem["COR"] = enem.TP_COR_RACA.replace({
    "0": "Nao declarado",
    "1": "Branca",
    "2": "Preta",
    "3": "Parda",
    "4": "Amarela",
    "5": "Indigena"
})

enem["RENDA_FAMILIAR"] = enem.Q006.replace({
    "A": "Nenhuma Renda",
    "B": "Ate R$ 1.045,00",
    "C": "De R$ 1.045,01 ate R$ 1.567,50",
    "D": "De R$ 1.567,51 ate R$ 2.090,00",
    "E": "De R$ 2.090,01 ate R$ 2.612,50",
    "F": "De R$ 2.612,51 ate R$ 3.135,00",
    "G": "De R$ 3.135,01 ate R$ 4.180,00",
    "H": "De R$ 4.180,01 ate R$ 5.225,00",
    "I": "De R$ 5.225,01 ate R$ 6.270,00",
    "J": "De R$ 6.270,01 ate R$ 7.315,00",
    "K": "De R$ 7.315,01 ate R$ 8.360,00",
    "L": "De R$ 8.360,01 ate R$ 9.405,00",
    "M": "De R$ 9.405,01 ate R$ 10.450,00",
    "N": "De R$ 10.450,01 ate R$ 12.540,00",
    "O": "De R$ 12.540,01 ate R$ 15.675,00",
    "P": "De R$ 15.675,01 ate R$ 20.900,00",
    "Q": "Acima de R$ 20.900,00"
})

enem["N_PESSOAS_RESIDENCIA"] = enem.Q005.replace({
    "1": 1
})

enem["TIPO_ESCOLA"] = enem.TP_ESCOLA.replace({
    "1": "Nao Respondeu",
    "2": "Publica",
    "3": "Privada",
    "4": "Exterior"
})

enem = enem.drop(columns=['TP_SEXO', 'TP_FAIXA_ETARIA', 'TP_COR_RACA', 'Q006', 'Q005', 'TP_ESCOLA'])

connection_string = "mysql+pymysql://root:root@172.21.0.3:3306/enem"
engine = sqlalchemy.create_engine(
    connection_string
)


enem.to_sql("enem_tratado", con=engine, index=False, if_exists='append', chunksize=1000)

print(dict(enem.dtypes))
