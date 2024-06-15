import sqlite3
import time

def get_all_tasks(sort_by_newest=False)->list:
    with sqlite3.connect("static/database.db") as conn:
        cursor = conn.cursor()
        keys = "rowid content created_at".split()
        q = f"""select {','.join(keys)} from tasks """
        if sort_by_newest:
            q += "order by created_at desc"
        res = conn.cursor().execute(q)
        ret = []
        for task in res.fetchall():
            d = {}
            for i,key in enumerate(keys):
                d[key] = task[i] 
            ret.append(d)
        return ret
    
def add_one_task(content:str)->int:
    with sqlite3.connect("static/database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute(f"insert into tasks(content, created_at) values (?,?)", (str(content), int(time.time())))
        print(res.fetchone())
        return 0

if __name__=="__main__":
    with sqlite3.connect("static/database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""create table if not exists tasks 
                        (created_at integer,
                        content text)""")
        # tasks =  [(f'{i}',int(time.time()), f"task {i}") for i in range(10)]
        tasks =  [(int(time.time()), f"task {i}") for i in range(10)]
        cursor = conn.cursor()
        cursor.executemany("insert into tasks(created_at,content) values(?,?)",tasks)
