CREATE TABLE IF NOT EXISTS submitter_photo_batch (
    -- Relates a submitter to all the batches submitted by him/her
    submitter_id UUID NOT NULL,
    photo_batch_id UUID NOT NULL,
    CONSTRAINT fk_submitters FOREIGN KEY(submitter_id) REFERENCES submitter(id),
    CONSTRAINT fk_photo_batches FOREIGN KEY(photo_batch_id) REFERENCES photo_batch(id)
);