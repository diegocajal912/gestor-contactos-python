import pyodbc

def get_connection():
    connection = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=DESKTOP-XENEIZE;"
        "DATABASE=projetc_simple;"
        "Trusted_Connection=yes;"
    )
    return connection