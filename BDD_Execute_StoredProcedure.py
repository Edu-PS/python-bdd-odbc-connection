
def excecute_sp(cursor, StoredProcedure):
    # Call StoreProcedure and trap Error if raised
    try:
        result = cursor.execute(StoredProcedure)
        message = 'SP OK - ' + str(StoredProcedure)
    except:
        message = 'SP ERROR - ' + str(StoredProcedure)
        result = 0
    
    return result, message

