from database.postgres import PostgresDB as db

class FeralCatCensusDb:
    """
    This class encapsulates the operations for the feral cat census database.  It makes use
    of a database connection, but we separate the application-specific operations from the 
    more general database operations.
    """

    def __init__(self, db):
        """
            db: The underlying database object itself.  We assume there is an open connection.
        """
        self.database = db

        # Verify there is an open connection to the database
        if not db.is_open():
            print("There is no open connection to the database!")

    def insert_original_photo(self, df_row):
        """
        Insert an original photo into the original_photo table.

        Args:
            df_row: Row from a dataframe that describes an original_photo (filename, GPS data, cluster ID)

        Returns: None
        """
        filename = df_row['filename']
        gps = df_row['gps']
        cluster = df_row['cluster']

        if gps == (None, None):
            gps = None # Will result in a NULL field for the lat_long of the original_photo
        
        query = "INSERT INTO original_photo (image_filename, lat_long) VALUES (%s, %s)"
        params = (filename, gps)