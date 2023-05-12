
def excecute_sql(cursor, SQLStatement):
    # Call SQLStatement and trap Error if raised
    try:
        result = cursor.execute(SQLStatement)
        message = 'SQL OK - ' + str(SQLStatement)
    except:
        message = 'SQL ERROR - ' + str(SQLStatement)

    return result, message

