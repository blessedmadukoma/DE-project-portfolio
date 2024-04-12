
    conn = psycopg2.connect(f"host={os.getenv('POSTGRES_HOST')} dbname={os.getenv('POSTGRES_DB')} user={os.getenv('POSTGRES_USER')} password={os.getenv('POSTGRES_PASSWORD')} port={os.getenv('POSTGRES_PORT')}")
except psycopg2.Error as e:
    print("Error: could not connect to postgres database ->", e)