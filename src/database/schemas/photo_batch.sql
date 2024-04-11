CREATE TABLE IF NOT EXISTS photo_batch (
    -- Batch of photos submitted by a submitter
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Location data supplied by submitter
    location_string text NULL,
    
    -- Description of photos supplied by submitter
    description_string text NULL,
    
    -- Time of submission
    time_submitted timestamp NOT NULL -- All times must be stored in UTC
);