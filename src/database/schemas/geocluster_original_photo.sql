CREATE TABLE IF NOT EXISTS geocluster_original_photo (
    -- Relates a geocluster to all the original photos in it
    geocluster_id UUID NOT NULL,
    original_photo_id UUID NOT NULL,
    CONSTRAINT fk_original_photos FOREIGN KEY(original_photo_id) REFERENCES original_photo(id),
    CONSTRAINT fk_geoclusters FOREIGN KEY(geocluster_id) REFERENCES geocluster(id)
);