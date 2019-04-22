import sqlite3

class czaSqlite3(object):
    def __init__(self):
        self.conn = sqlite3.connect("sqlite3.db")
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        print("execute done")
        if "select" in sql.lower():
            print("result is {}".format(self.cursor.fetchall()))

    def commit(self):
        self.conn.commit()
        print("data save success!")

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = czaSqlite3()

    # sql = """create table cza (id int(1), name varchar(20), sex varchar(10), age int(2))"""
    # sql = """insert into cza values (3, 'ang', 'female', 24)"""
    sql = """select * from cza"""
    # sql = """select id,name from cza where age=23"""
    # sql = """select distinct age from cza"""
    # sql = """update cza set age=18 where name='chen'"""
    # sql = """delete from cza where age=18"""
    # sql = """drop table source"""
    # sql = """truncate table source""""  -- clear the table
    db.execute(sql)
    db.commit()
    db.close()