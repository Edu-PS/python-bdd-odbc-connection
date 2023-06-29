import pyodbc;

def open_connection(odbc):
    # Connect to datasource
    conn = pyodbc.connect('DSN='+odbc+'', autocommit=True)

    # Create cursor associated with connection
    try:
        cursor = conn.cursor()
        message='Connection opened'
    except:
        message='Error opening connection'

    return conn, cursor, message


def close_connection(conn, cursor):
    try:
        # Close and delete cursor
        cursor.close()
        del cursor
        # Close Connection
        conn.close()
        message= 'Connection closed'
    except:
        message='Error closing connection'
    
    return message

