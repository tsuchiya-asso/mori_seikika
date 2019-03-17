# MySQLdb をインポート
import MySQLdb
 
# データベース接続とカーソル生成
connection = MySQLdb.connect(
    host='192.168.100.109', user='tsuchiya', passwd='', db='mori_seikika', charset='utf8')
cursor = connection.cursor()

i=1
# エラー処理（例外処理）
try:
    while i < 100000:
        cursor.execute("select id,body from kouji_joho LIMIT " + str(i) + "," + str(1) + ";")
        for row in cursor:
            #print(row[0])
            #text = row[0].strip()
            #text = row[0].replace('\n','')
            text = row[1]
            text = text.replace('\n','')
            text = text.replace(' ','')
            text = text.replace('　','')
            text = text.replace('"','')
            text = text.replace('\'','')
            #print(text)
            #print(len(text))
            #print("update projects SET body = '" + text + "' where id = " + str(row[0]) + ";")
            print(row[0])
            cursor.execute("update kouji_joho SET body = '" + text + "' where id = " + str(row[0]) + ";")
        i = i+1

except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)
 
# 保存を実行（忘れると保存されないので注意）
connection.commit()
 
# 接続を閉じる
connection.close()