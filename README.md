# Case - Engenheiro de Dados
## Certificação Data Master

### Bruno Campos

### Download do Projeto

```
git clone https://github.com/detonih/data_master.git
```

## Build da Imagem

```
docker build -t hadoop-cluster .
```

## Subida dos serviços

```
docker-compose up -d
```

## Entrar no serviço principal - Hadoop

```
docker exec -it hadoop-env /bin/bash
```

## Entrar no serviço do MySQL
```
docker exec -it data_master_db /bin/bash
```

## Entrar no serviço do MongoDB
```
docker exec -it data_master_mongo_db /bin/bash
```


## Execução dos scripts de fluxo de trabalho

Realizar no terminal do serviço principal (Hadoop)
```
bash /scripts/sh/cria_enem.sh
```

## Exclusão dos serviços

Realizar após todo o processo ser concluído e validações realizadas
```
docker stop hadoop-env 
docker stop data_master_db
docker stop data_master_mongo_db
docker container prune
```
