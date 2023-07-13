import pymysql
import charts
# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "Ar0340252",
    "db": "test_db",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "INSERT INTO charts(id, name, artist)VALUES(%s, %s, %s)"
        # 取得華語單曲日榜
        charts = charts.get_charts_tracks("H_PilcVhX-E8N0qr1-")
        for chart in charts:
            cursor.execute(
                command, (chart["UserID"], chart["UserName"], chart["UserPassword"], chart["UserType"]))
        # 儲存變更
        conn.commit()

except Exception as ex:
    print(ex)