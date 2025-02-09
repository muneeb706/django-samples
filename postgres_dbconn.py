import psycopg
from psycopg import sql
from psycopg import connect

def connect_to_db():
    # Database connection parameters
    db_params = {
        'dbname': 'django_samples',
        'user': 'postgres',
        'host': 'localhost',
        'port': '5432'
    }

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        print("Connected to PostgreSQL database")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a simple query
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()

        # Print the list of tables
        print("Tables in the database:")
        for table in tables:
            print(table[0])

        # Close the cursor and connection
        cursor.close()
        conn.close()
        print("Connection closed")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    connect_to_db()