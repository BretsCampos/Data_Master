USE enem;
CREATE TABLE IF NOT EXISTS enem_tratado (
  id int(10) NOT NULL AUTO_INCREMENT,
  FAIXA_ETARIA varchar(100),
  SEXO varchar(100),
  COR varchar(100),
  RENDA_FAMILIAR varchar(100),
  N_PESSOAS_RESIDENCIA int(10),
  TIPO_ESCOLA varchar(100),
  KEY(id)
);