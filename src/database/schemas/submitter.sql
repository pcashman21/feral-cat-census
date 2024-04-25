CREATE TABLE IF NOT EXISTS submitter (
    -- A person who submits photos
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Email address of submitter
    email_address VARCHAR(100) NOT NULL ,

    -- Location information provided by submitter may relate to
    -- the submitter or to the photos being submitted
    location_string text NULL
);

CREATE INDEX IF NOT EXISTS submitter_email ON submitter (email_address);