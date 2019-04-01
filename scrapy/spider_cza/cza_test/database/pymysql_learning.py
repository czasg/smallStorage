import pymysql
import logging

logging.basicConfig(level=logging.DEBUG)

class czaPymysql(object):
    dbSettings = {
        "host":"127.0.0.1",
        "user":"root",
        "password":"cza19950917",
        "database":"dbPymysql",
    }
    def __init__(self):
        self.conn = pymysql.connect(**self.dbSettings)
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        logging.debug("execute done!")
        if 'select' in sql.lower():
            logging.debug("the result is {}".format(self.cursor.fetchall()))
        self.conn.commit()
        logging.debug("data save succes!")
        self.conn.close()

if __name__ == "__main__":
    db = czaPymysql()

    # sql = """create table cza (id int(1), name varchar(10), sex varchar(10), age int(2))"""
    # sql = """insert into cza values (3, 'ang', 'female', 24)"""
    sql = """select * from cza"""
    # sql = """select name,age from cza where id=1"""
    # sql = """update cza set name='newName' where id=1"""
    # sql = """delete from cza where id=1"""

    db.execute(sql)