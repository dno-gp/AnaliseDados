import pymysql.cursors

connection = pymysql.connect(host='localhost',
                            user = 'root',
                            password = '123456',
                            db = 'sis1_db')


def consulta(sql): 
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()

    return result

def mklist(tupla):
    eixo_x = []
    eixo_y = []
    for i, j in tupla:
        eixo_x.append(str(i))
        eixo_y.append(j)