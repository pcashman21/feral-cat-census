CREATE TABLE IF NOT EXISTS cluster_segmented_image (
    -- Relates a cluster to all the segmented images derived from the
    -- original photos in the geocluster
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    cluster_id UUID NOT NULL,
    segmented_image_id UUID NOT NULL,
    CONSTRAINT fk_segmented_images FOREIGN KEY(segmented_image_id) REFERENCES segmented_image(id),
    CONSTRAINT fk_clusters FOREIGN KEY(cluster_id) REFERENCES cluster(id)
);