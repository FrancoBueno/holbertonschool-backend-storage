-- Lists all bands with Glam rock as their style
-- ranked for their long
-- asdasdasdassda

SELECT band_name, ifnull(split, 2020)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
