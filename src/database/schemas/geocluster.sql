CREATE TABLE IF NOT EXISTS geocluster (
    -- Descriptor for a geocluster, or set of photos grouped
    -- together by DBSCAN algorithm based on their proximity
    -- to one another.  All photos where taken within a radius R
    -- of the geocluster's centroid.
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Lat/long of the geocluster centroid.  Note: Some photos have no
    -- GPS data.  These will be put into one (giant) geocluster whose
    -- centroid is (0,0).  This way the geocluster will show up on a map
    -- with all other clusters and can be edited and approved.
    centroid POINT NOT NULL,

    -- The DBSCAN algorithm generates cluster IDs starting with 0.  
    dbscan_cluster_number INTEGER NOT NULL,

    -- We keep the DBSCAN cluster number along with the geocluster_generation as indexed
    -- fields, so we can recluster all photos at regular intervals (e.g., 3 months),
    -- adding new photos along the way, while keeping the historical cluster
    -- information if necessary.  This way we can distinguish two geoclusters with
    -- the same DBSCAN cluster number that were generated at different times.
    geocluster_generation_number INTEGER NOT NULL,

    -- Approval status (has a person agreed that all feature
    -- clusters are as they should be) 
    approval_status BOOLEAN DEFAULT FALSE,

    -- Editing status: Is someone editing this cluster now?
    editing_status BOOLEAN DEFAULT FALSE,

    -- Upper and lower bounds on number of cats in this geocluster
    population_lower_bound INTEGER DEFAULT 0 NOT NULL,
    population_upper_bound INTEGER DEFAULT 0 NOT NULL 
);

CREATE INDEX IF NOT EXISTS geocluster_dbscan_index ON geocluster (dbscan_cluster_number, geocluster_generation_number);