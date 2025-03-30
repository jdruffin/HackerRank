SELECT
    W.ID,
    WP.AGE,
    W.COINS_NEEDED,
    W.POWER
FROM
    WANDS AS W
    JOIN WANDS_PROPERTY AS WP ON W.CODE = WP.CODE
WHERE
    WP.IS_EVIL = 0 AND
    W.COINS_NEEDED = ( 
        SELECT
            MIN(W1.COINS_NEEDED) 
        FROM
            WANDS W1 
        WHERE
            W1.POWER = W.POWER AND
            W1.CODE = W.CODE 
    ) 
ORDER BY
    W.POWER DESC,
    WP.AGE DESC