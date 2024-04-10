CREATE TABLE IF NOT EXISTS segmented_image (
    -- Descriptor for segmented image of a single cat, 
    -- extracted from an original_photo
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- ID of original_photo from which this was extracted
    original_photo_id UUID NOT NULL, 
    
    -- cat ID within that original_photo, supplied by
    -- instance segmentation model.  Of the form "cat-x",
    -- where x is an integer starting at 0 for the first
    -- cat extracted, 1 for second, etc.
    cat_id VARCHAR(8)
);