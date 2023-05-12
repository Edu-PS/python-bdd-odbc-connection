import BDD_ODBC_Connection as bddconn
import BDD_Execute_StoredProcedure as spr

# Setting the Statement to excecute
sp = "SELECT * FROM bancos_hem"

# Opening connection
[conn, cursor, message] = bddconn.open_connection('DB_FPY')

# Excecuting the Store Procedure (sp)
[result, message] = spr.excecute_sp(cursor, sp)

# Printing the message
print('MENSAJE -> ' + message)

# Colecting the return values of Stored Procedure
rows1 = result.fetchall()

# Closing the connection
bddconn.close_connection(conn, cursor)

for row in rows1:
   print('PRIMERO -- ' + str(row))


