-- Script that ranks country origins of bands by num of (non-unique) fans order.
SELECT origin, SUM(fans) as fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY fans DESC;
