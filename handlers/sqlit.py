import sqlite3
import pytz
from datetime import datetime
def reg_user(id, refka):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
            id BIGINT,
            stat
            ) """)
    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        prokladka,
        finish_stat
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,refka,'0'))
        db.commit()

#Новое
def get_data_tag(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f"SELECT prokladka FROM user_time  WHERE id = '{id}'").fetchone()[0]
    return a


def update_status(user_id,n):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    try:
        status_all = int(sql.execute(f"SELECT finish_stat FROM user_time WHERE id = '{user_id}'").fetchall()[0][0])
        if status_all < n:
            sql.execute(f"UPDATE user_time SET finish_stat = '{n}'  WHERE id = '{user_id}'")
            db.commit()

    except Exception as ex:
        print("Произошла ошибка:", ex, "юзер:" , user_id)



def change_all():
    print('Заблокирована функция. Необходимо раскомитить код')
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1000'")
    db.commit()



def info_members(): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    all = sql.execute(f"SELECT COUNT(*) FROM user_time ").fetchone()[0]

    a1 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '1'").fetchone()[0]
    a2 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '2'").fetchone()[0]
    a3 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '3'").fetchone()[0]
    a4 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '4'").fetchone()[0]
    a5 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '5'").fetchone()[0]
    a6 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '6'").fetchone()[0]
    a7 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '7'").fetchone()[0]
    a8 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '8'").fetchone()[0]
    a9 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '9'").fetchone()[0]
    a10 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '10'").fetchone()[0]
    a11 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '11'").fetchone()[0]
    a12 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '12'").fetchone()[0]
    a13 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '13'").fetchone()[0]
    a14 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '14'").fetchone()[0]
    a15 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '15'").fetchone()[0]
    a16 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '16'").fetchone()[0]
    a17 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '17'").fetchone()[0]
    a18 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '18'").fetchone()[0]
    a19 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '19'").fetchone()[0]
    a20 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '20'").fetchone()[0]
    a21 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '21'").fetchone()[0]
    a22 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '22'").fetchone()[0]
    a23 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '23'").fetchone()[0]
    a24 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '24'").fetchone()[0]
    a25 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '25'").fetchone()[0]
    a26 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '26'").fetchone()[0]
    a27 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '27'").fetchone()[0]
    a28 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '28'").fetchone()[0]
    a29 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '29'").fetchone()[0]
    a30 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '30'").fetchone()[0]
    a31 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '31'").fetchone()[0]
    a32 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '32'").fetchone()[0]
    a33 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '33'").fetchone()[0]
    a34 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '34'").fetchone()[0]
    a35 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '35'").fetchone()[0]
    a36 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '36'").fetchone()[0]

    return [all,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36]




def get_stat(): # Количество челов, запустивших бота
    env = []
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    data = sql.execute(f'SELECT DISTINCT prokladka FROM user_time').fetchall()

    for d in data:
        i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{d[0]}"').fetchone()[0]
        env.append([d[0],i])

    return env

def get_my_link(user_name):
    print('Поиск')
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{user_name}"').fetchone()[0]
    return i



def get_connt_stat(n): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{n}"').fetchone()[0]
    return i



def change_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1' WHERE id = '{id}'")
    db.commit()


def change_prokladka(id, p):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '{p}' WHERE id = '{id}'")
    db.commit()

def add_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (int(id), '0'))
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (str(id), '0'))
        db.commit()

def get_username(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    q = (sql.execute(f"SELECT prokladka FROM user_time WHERE id = '{id}'").fetchone())[0]
    return q



def cheak_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None: #Список пуст, разрешает
        return 0
    else: #Запрещаем
        return 1