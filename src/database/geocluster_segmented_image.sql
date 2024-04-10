CREATE TABLE IF NOT EXISTS geocluster_segmented_image (
    -- Relates a geocluster to all the segmented images derived from the
    -- original photos in the geocluster
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    geocluster_id UUID NOT NULL,
    segmented_image_id UUID NOT NULL,
    CONSTRAINT fk_segmented_images FOREIGN KEY(segmented_image_id) REFERENCES segmented_image(id),
    CONSTRAINT fk_geoclusters FOREIGN KEY(geocluster_id) REFERENCES geocluster(id)
);