import json
import logging
import datetime
import pymysql
import models as M

# log file

log_file = '/data/'+__file__.split('/')[-1]+'_'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.log'
logging.basicConfig(filename=log_file, filemode='a', format='%(levelname)s:%(asctime)s:%(message)s' , level=logging.DEBUG)

#reading table list
try :
    tablelist = {}
    with open('ingestion_config.json','r') as j :
        tablelist = json.load(j)

except Exception as e :
    logging.error("Error at opening config file " + e)

#mysql connection
conn = pymysql.Connect(host='database',user='codetest',password='swordfish')
cur = conn.cursor()


#loading tables
saperator = ','
try :
    for _table in tablelist :
        cur.execute("use codetest;")
        sql = f"truncate table {_table};"
        cur.execute(sql)
        logging.info(f"table {_table} truncated successfully !!")

        data = []
        with open(tablelist[_table],'r',encoding="utf8") as f :
            next(f)
            for line in f.readlines() :
                data.append(tuple(line.strip('\n').split(saperator)))
        logging.info(f"loading file {tablelist[_table]}")
        cols = getattr(M, _table)()
        cols = ','.join(cols)
        data = ','.join(map(lambda x : str(x) , data))
        sql = f" insert into {_table}({cols}) values {str(data)};"
        cur.execute(sql)
        cur.execute('commit;')
        logging.info(f"data inserted successfully into {_table} !!")
except Exception as e:
    logging.error(f"!!!!! error : {e} !!!!!!!!")
