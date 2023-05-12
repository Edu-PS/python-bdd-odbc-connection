import BDD_ODBC_Connection as bddconn
import BDD_Execute_StoredProcedure as spr

# Setting the values to excecute
Nro_serie = 32229781
sp = "{call sp_Get_DataReport_ModHEM_Gen2_Beckhoff_By_NroSerie(" + str(Nro_serie) + ")}"

# Opening connection
[conn, cursor, message] = bddconn.open_connection('DB_FPY')

# Excecuting the Store Procedure (sp)
[result, message] = spr.excecute_sp(cursor, sp)

# Printing the message
print('MENSAJE -> ' + message)

# Colecting the return values of Stored Procedure
rows1 = result.fetchall()
cursor.nextset()
rows2 = result.fetchall()

# Closing the connection
bddconn.close_connection(conn, cursor)

for row in rows1:
   print('PRIMERO -- ' + str(row))

# rows = cursor.fetchall()
for row in rows2:
   print('SEGUNDO -- ' + str(row))

