from psycopg2 import sql
from pandas import DataFrame

from config import DB_SCHEMA

def getData(cursor, table, mode='year', year=1961):
    cursor.execute(
        sql.SQL("SELECT * FROM {} WHERE date_part('year', date) = %s AND date_part('month', date) IN (4, 5, 6) ORDER BY date;").format(sql.Identifier(DB_SCHEMA, table)), (str(year),))
    
    array = cursor.fetchall()
    
    dataDict = {'date': [], 'common': [], 'spillway': [], 'diff': []}
    index = []
    
    for i in array:
        index.append(i[0])
        dataDict['date'].append(i[1])
        dataDict['common'].append(i[2])
        dataDict['spillway'].append(i[3])
        dataDict['diff'].append(i[2] - i[3])
    # print(dataDict)
    return DataFrame(data=dataDict, index=index)
