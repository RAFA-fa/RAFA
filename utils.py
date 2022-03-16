import time
import pymysql
import numpy as np
from itertools import chain


class DB:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "940530"
        self.db = "zddb"

    def get_conn(self):
        # 创建连接
        conn = pymysql.connect(host=self.host, user=self.user,
                               password=self.password, db=self.db, charset="utf8")
        # 创建游标
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        return conn, cursor

    def close_conn(self, conn, cursor):
        cursor.close()
        conn.close()

    def query(self, sql, *args):
        conn, cursor = self.get_conn()
        cursor.execute(sql, args)
        res = cursor.fetchall()
        self.close_conn(conn, cursor)
        return res


# vital：HR：心率、Temp：体温、SBP：心脏收缩压、DBP：心脏舒张压、Resp：呼吸频率、O2Sqt：氧饱和度、MBP：平均血压

# 血气分析:PH值、动脉血氧饱和度、PO2:动脉血氧分压、PCO2动脉血氧二氧化碳分压、
# 乳酸、实际碳酸氢盐、
# BaseExcess：碱剩余、Glucose:血红蛋白、血糖、Potassium:钾、钠、氯、Calcium:钙

# 已关注的检验指标：WBC:白细胞计数、红细胞计数、中性粒细胞、淋巴细胞、C-反应蛋白测定、肌酐、尿素
# 白细胞介素-6、血小板计数、血红蛋白测定
class DataSelect(DB):
    def get_time(self):
        time_str = time.strftime("%Y{}%m{}%d{} %X")
        return time_str.format("年", "月", "日")

    def get_lab_data(self):
        sql = """
        SELECT *
        from lab
        WHERE STAY_ID='ZY01010121023011'
        ORDER BY CHARRTIME DESC
        LIMIT 1
        """
        res = DB.query(self, sql)  # 使用类名调用父类函数
        return res[0]

    def get_demographic_data(self):
        sql = """
        SELECT *
        from cohort1
        WHERE STAY_ID='ZY01010121023011'
        """
        res = super().query(sql)  # 使用super调用父类函数
        # 返回值是一个元组，取元组中的第一个数
        return res[0]

    def get_vital_data(self):
        sql = """
        SELECT *
        FROM zddb.vital_new as vn
        WHERE STAY_ID ='ZY01010121023011'
        ORDER BY vn.charttime DESC limit 15
        
        """
        res = super().query(sql)

        data = np.column_stack((res[0], res[1], res[2], res[3], res[4],
                                res[5], res[6], res[7], res[8], res[9],
                                res[10], res[11], res[12])).T

        return data



    def get_age_data(self):
        sql = """
        with first as (
            SELECT 
            cast(age as FLOAT) as Age
            from cohort1
            )
            SELECT 
            age,
            COUNT(AGE) as age_number
            FROM first
            GROUP BY AGE
            order by AGE 		

        """
        res = super().query(sql)

        data = res

        return data


if __name__ == "__main__":
    dataselect = DataSelect()
    res = dataselect.get_age_data()
    x_data =[]
    y_data =[]
    for i in range(len(res)):
        x_data.append(int(res[i][0]))
        y_data.append(res[i][1])
    print(res)
    print(x_data)
    print(y_data)
