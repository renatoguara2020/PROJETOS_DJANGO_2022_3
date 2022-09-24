import psycopg2

conn = psycopg2.connect(database="python",
                        host="localhost",
                        user="postgres",
                        password="456ALVES",
                        port="5432")

print(conn)
