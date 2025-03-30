SELECT
    H.HACKER_ID,
    H.NAME,
    TS.TOTAL_SCORE
FROM
    HACKERS AS H
    JOIN (
        SELECT
            SUM(MAX_SCORE) AS TOTAL_SCORE,
            MS.HACKER_ID
        FROM (
            SELECT
                S.HACKER_ID,
                S.CHALLENGE_ID,
                MAX(SCORE) AS MAX_SCORE
            FROM
                SUBMISSIONS AS S
            GROUP BY
                S.HACKER_ID,
                S.CHALLENGE_ID
            HAVING
                MAX(SCORE) > 0
        ) AS MS
        GROUP BY
            MS.HACKER_ID
    ) AS TS ON H.HACKER_ID = TS.HACKER_ID
ORDER BY
    TS.TOTAL_SCORE DESC,
    H.HACKER_ID ASC