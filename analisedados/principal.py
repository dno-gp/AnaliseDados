import cnxmysql
from cnxmysql import consulta

#Define a consulta no banco de dados
sql = "select municipio, q1 from s1_pes_22ago20"

#Executa a consulta
tupla = consulta(sql)

#Faz as listas que serão usadas nos eixos x e y.
mklist(tupla)

#Constrói o gráfico
