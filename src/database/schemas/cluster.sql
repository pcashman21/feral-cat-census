CREATE TABLE IF NOT EXISTS cluster (
    -- A feature cluster, i.e., a set of segmented images collected into
    -- a cluster based on their cosine similarity metric as calculated by
    -- the SentenceTransformer model.
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    
    -- Average similarity of images in this cluster,
    -- if this cluster is NOT a singleton
    average_similarity FLOAT NUll,

    -- Maximum similarity between the image in this singleton cluster
    -- and all other singleton clusters in this geocluster
    maximum_similarity FLOAT NULL
);