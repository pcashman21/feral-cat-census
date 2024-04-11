CREATE TABLE IF NOT EXISTS photo_batch_original_photo (
    -- Relates a photo batch to all the photos in it
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    photo_batch_id UUID NOT NULL,
    original_photo_id UUID NOT NULL,
    CONSTRAINT fk_original_photos FOREIGN KEY(original_photo_id) REFERENCES original_photo(id),
    CONSTRAINT fk_photo_batches FOREIGN KEY(photo_batch_id) REFERENCES photo_batch(id)
);