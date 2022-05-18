#!/bin/bash

echo "Buscando dados do Enem 2020..."
bash -x /scripts/sh/busca_enem.sh

if [ $? -eq 0 ]; then
    echo "Dados carregados com sucesso"
    echo "Carregando os dados no MySQL..."

    python3 /scripts/python/enem_pd.py

    if [ $? -eq 0 ]; then
        echo "Dados carregados com sucesso no MySQL"
        echo "Criando database enem no Hive..."
        hive -e "CREATE DATABASE enem;"

        if [ $? -eq 0 ]; then
          echo "Database enem criado com sucesso no Hive"
          echo "Importando dados do Enem do MySQL para o Hive..."

          sqoop import --connect jdbc:mysql://172.21.0.3:3306/enem \
          --driver com.mysql.cj.jdbc.Driver \
          --username root \
          --password ${MYSQL_ROOT_PASSWORD} \
          --split-by id \
          --columns id,SEXO,FAIXA_ETARIA,COR,RENDA_FAMILIAR,N_PESSOAS_RESIDENCIA,TIPO_ESCOLA \
          --table enem_tratado \
          --bindir /tmp/sqoop-root/compile \
          --target-dir /user/root/enem_tratado  \
          --fields-terminated-by ";"  \
          --hive-import \
          --create-hive-table \
          --hive-table enem.enem_tratado

          if [ $? -eq 0 ]; then
            echo "Dados importados com sucesso no MySQL"

          else
              echo "Problema para importar dados do MySQL"
              exit 1
          fi

        else
            echo "Problema para criar o database enem no Hive"
            exit 1
        fi
    else
        echo "Problema para carregar dados no MySQL"
        exit 1
    fi
else
    echo "Problema para buscar os dados do Enem"
    exit 1
fi



