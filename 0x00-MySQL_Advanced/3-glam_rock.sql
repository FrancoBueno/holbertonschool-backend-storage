-- Lists all bands with Glam rock as their style
-- ranked for their long
-- asdasdasdassda

SELECT band_name, IF(ISNULL(split), 2020 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
