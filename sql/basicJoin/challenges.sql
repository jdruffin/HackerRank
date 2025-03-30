SELECT
    h.hacker_id,
    h.name,
    p.challenge_count
FROM 
    hackers h 
    INNER JOIN (
        SELECT
            hacker_id,
            COUNT(*) AS challenge_count
        FROM
            challenges
        GROUP BY
            hacker_id
    ) AS p ON h.hacker_id = p.hacker_id 
WHERE
    p.challenge_count = (
        SELECT 
            MAX(challenge_count)
                FROM (
                    SELECT
                        COUNT(*) AS challenge_count
                    FROM
                        challenges
                    GROUP BY
                        hacker_id
                ) AS max_count
    ) OR 
    p.challenge_count NOT IN (
        SELECT
            challenge_count
        FROM (
            SELECT
                COUNT(*) AS challenge_count
            FROM
                challenges
            GROUP BY
                hacker_id
        ) AS challenge_counts
        GROUP BY
            challenge_count
        HAVING
            COUNT(*) > 1 AND
            challenge_count < (
                SELECT
                    MAX(challenge_count)
                FROM (
                    SELECT
                        COUNT(*) AS challenge_count
                    FROM
                        challenges
                    GROUP BY
                        hacker_id) AS max_count
            ) 
    )
ORDER BY
    p.challenge_count DESC,
    h.hacker_id;