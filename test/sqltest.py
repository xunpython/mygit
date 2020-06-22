import pyodbc
db = pyodbc.connect('DRIVER={SQL Server Native Client 10.0}; SERVER=localhost; DATABASE=dtms_a; UID=sa; PWD=123456')
curs = db.execute('select getdate()')
print(curs.fetchone())
db.close()
