from database.postgres import PostgresDB as db

class OriginalPhoto:
    """
    This class encapsulates the operations for the original_photo table.  It makes use
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

    def insert_original_photo(self, image_filename, lat_long):
        """
        Insert an original photo into the original_photo table.

        Args:
            image_filename      fully-qualified pathname of image file
            lat_long            list of floats [latitude, longitude], or None if no GPS data in photo

        Returns: ID of original_photo table entry
        """

        if lat_long is None or lat_long[0] is None or lat_long[1] is None:
            lat_long = None # Will result in a NULL field for the lat_long of the original_photo
        
        query = "INSERT INTO original_photo (image_filename, lat_long) VALUES (%s, %s) RETURNING id"
        params = (image_filename, lat_long)
        cursor = self.database.execute_query(query, params)
        original_photo_id = self.database.fetch_one(cursor)
        return original_photo_id