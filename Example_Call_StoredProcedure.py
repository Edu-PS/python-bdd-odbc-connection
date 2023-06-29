import BDD_ODBC_Connection as bddconn
import BDD_Execute_StoredProcedure as spr

# Setting the values to excecute
odbc = 'DB_LEP_DES' #'DB_FPY'
Nro_serie = 32229781
sp = 'call sp_Get_AllProtocols(\'{x2}\',\'{x1}\')'.format(x1='CASTELLANO', x2='FUTURE')
print(sp)
# Opening connection
[conn, cursor, message] = bddconn.open_connection(odbc)

# Excecuting the Store Procedure (sp)
[result, message] = spr.excecute_sp(cursor, sp)

# Printing the message
print('MENSAJE -> ' + message)
print(cursor.description)
for a in cursor.description:
   print(a[0])

# Colecting the return values of Stored Procedure
rows1 = result.fetchall()
cursor.nextset()
print(cursor.description)
rows2 = result.fetchall()

# Closing the connection
bddconn.close_connection(conn, cursor)

for row in rows1:
   print('PRIMERO -- ' + str(row))

# rows = cursor.fetchall()
for row in rows2:
   print('SEGUNDO -- ' + str(row))

