CREATE TABLE IF NOT EXISTS original_photo (
    -- Descriptor for an original photo, NOT a segmented image of a cat
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Full path and filename of where image is stored
    image_filename VARCHAR(255) NOT NULL, 
    
    -- Lat/long where photo was taken must be present for geoclustering to work
    -- However, some photos have no GPS data, so allow this field to be null.
    lat_long POINT
);