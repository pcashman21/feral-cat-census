import psycopg2

class PostgresDB:
  """
  This class encapsulates a connection to a PostgreSQL database.
  """

  def __init__(self, host, database, user, password):
    """
    Initializes the connection to the PostgreSQL database.

    Args:
        host: The hostname or IP address of the database server.
        database: The name of the database to connect to.
        user: The username for database access.
        password: The password for the database user.
    """
    self.connection = None
    try:
      self.connection = psycopg2.connect(
          host=host, database=database, user=user, password=password
      )
    except Exception as e:
      print(f"Error connecting to database: {e}")

  def is_open(self):
    """
        :return True if there is an open connection
    """
    return self.connection is not None
  
  def __del__(self):
    """
    Closes the connection to the database when the object is garbage collected.
    """
    if self.connection:
      self.connection.close()

  def execute_query(self, query, params=None):
    """
    Executes a SQL query on the database.

    Args:
        query: The SQL query string to be executed.
        params: A list of parameters to be used in the query (optional).

    Returns:
        A cursor object containing the results of the query, or None if an error occurs.
    """
    if not self.connection:
      print("Error: Database connection is not established.")
      return None
    cursor = self.connection.cursor()
    try:
      if params:
        cursor.execute(query, params)
      else:
        cursor.execute(query)
      return cursor
    except (Exception, psycopg2.Error) as e:
      print(f"Error executing query: {e}")
      return None

  def fetch_all(self, cursor):
    """
    Fetches all results from the provided cursor.

    Args:
        cursor: A database cursor object containing the query results.

    Returns:
        A list of rows returned by the query, or None if an error occurs.
    """
    if not cursor:
      return None
    try:
      return cursor.fetchall()
    except Exception as e:
      print(f"Error fetching data: {e}")
      return None

  def fetch_one(self, cursor):
    """
    Fetches the first row from the provided cursor.

    Args:
        cursor: A database cursor object containing the query results.

    Returns:
        The first row returned by the query, or None if an error occurs or no rows are present.
    """
    if not cursor:
      return None
    try:
      return cursor.fetchone()
    except Exception as e:
      print(f"Error fetching data: {e}")
      return None

  def commit(self):
    """
    Commits any pending changes to the database.
    """
    if not self.connection:
      print("Error: Database connection is not established.")
      return
    try:
      self.connection.commit()
    except Exception as e:
      print(f"Error committing changes: {e}")