#!/bin/bash

curl https://download.inep.gov.br/microdados/microdados_enem_2020.zip  -o /raw-data/MICRODADOS_ENEM_2020.zip

FILE=/raw-data/MICRODADOS_ENEM_2020.zip
if [ -f "$FILE" ]; then

    echo "Fazendo unziping do arquivo..."
    unzip /raw-data/MICRODADOS_ENEM_2020.zip -d  /raw-data/
    if [ $? -eq 0 ]; then
        echo "Sucesso no unzip do arquivo"
        EXTRACTED_FILE=/raw-data/DADOS/MICRODADOS_ENEM_2020.csv
        rm /raw-data/MICRODADOS_ENEM_2020.zip
    else
        echo "Problema no unzip"
    fi

    if [ -f "$EXTRACTED_FILE" ]; then
        echo "Colocando o arquivo $EXTRACTED_FILE no HDFS..."
        hdfs dfs -put -f /raw-data/DADOS/MICRODADOS_ENEM_2020.csv /stage/MICRODADOS_ENEM_2020.csv
        mv /raw-data/DADOS/MICRODADOS_ENEM_2020.csv /raw-data/MICRODADOS_ENEM_2020.csv
        if [ $? -eq 0 ]; then
            echo "Arquivo importado com sucesso no HDFS"
            echo "Deletando os diretorios gerados pelo unzip"
            rm -rf /raw-data/D*
            rm -rf /raw-data/I*
            rm -rf /raw-data/L*
            rm -rf /raw-data/P*
            echo "Diretorios apagados"
        else
            echo "Problema para colocar o arquivo $EXTRACTED_FILE no HDFS"
        fi
    else
        echo "O arquivo $EXTRACTED_FILE nao existe"
    fi

else
    echo "O arquivo $FILE nao existe"
fi
