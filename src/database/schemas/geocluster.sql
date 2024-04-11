CREATE TABLE IF NOT EXISTS geocluster (
    -- Descriptor for a geocluster, or set of photos grouped
    -- together by DBSCAN algorithm based on their proximity
    -- to one another.  All photos where taken within a radius R
    -- of the geocluster's centroid.
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Lat/long of the geocluster centroid.  Note: Some photos have no
    -- GPS data.  These will be put into one (giant) geocluster whose
    -- centroid is (0,0).
    centroid POINT NOT NULL,

    -- Approval status (has a person agreed that all feature
    -- clusters are as they should be) 
    approval_status BOOLEAN DEFAULT FALSE,

    -- Editing status: Is someone editing this cluster now?
    editing_status BOOLEAN DEFAULT FALSE,

    -- Upper and lower bounds on number of cats in this geocluster
    population_lower_bound INTEGER DEFAULT 0 NOT NULL,
    population_upper_bound INTEGER DEFAULT 0 NOT NULL 
);