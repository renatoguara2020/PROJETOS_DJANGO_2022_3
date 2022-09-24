import psycopg2


conn = psycopg2.connect(database="python",
                        host="localhost",
                        user="postgres",
                        password="456ALVES",
                        port="5432")

if conn:
    # db_Info = conn.get_server_info()
    print("Connected to PostgreSQL Server version")
    print(conn)
