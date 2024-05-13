CREATE TABLE IF NOT EXISTS geocluster_generation (
    -- Define table to hold the list of generations of geoclusters.  We envision that
    -- after the initial load of photos and their processing through DBSCAN into geoclusters,
    -- that we will want to reload the photos, including new ones, and recluster them
    -- periodically (say once a quarter or so).  Since DBSCAN will always generate
    -- clusters starting with 0, we need to have a generation number to distinguish
    -- different instantiations of DBSCAN cluster N.  
    generation_number INTEGER NOT NULL DEFAULT 0 PRIMARY KEY,

    -- The generation_radius is the radius, in miles, used in the DBSCAN clustering algorithm
    -- to create the geoclusters in this generation.  It is possible to have different radii for
    -- different generations, to have a coarser- or finer-grained depiction of the geocluster locations.
    generation_radius FLOAT NOT NULL DEFAULT 1,
    time_of_generation TIMESTAMP NOT NULL
);