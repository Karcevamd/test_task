SELECT 
    d.name AS department,
    CONCAT(
        CASE 
            WHEN p.name LIKE '%а' THEN 'г-жа ' 
            ELSE 'г-н ' 
        END,
        p.name
    ) AS employee
FROM 
    Department d
JOIN 
    Personal p ON d.id = p.id_dep;
SELECT 
    *,
    REGEXP_COUNT (LOWER(name), 'ё|у|е|ы|а|о|э|я|и|ю', 1, 'i') AS vowel_count
FROM 
    Personal p
ORDER BY 
    vowel_count;
WITH MaxMinSalaries AS (
    SELECT 
        id_dep,
        MAX(sal) AS max_salary,
        MIN(sal) AS min_salary
    FROM 
        Personal
    GROUP BY 
        id_dep
)
SELECT 
    p.id_dep,
    p.name AS employee_name,
    p.sal AS salary,
    'Max' AS salary_type
FROM 
    Personal p
    JOIN MaxMinSalaries m ON p.id_dep = m.id_dep AND p.sal = m.max_salary
UNION ALL
SELECT 
    p2.id_dep,
    p2.name AS employee_name,
    p2.sal AS salary,
    'Min' AS salary_type
FROM 
    Personal p2
    JOIN MaxMinSalaries m ON p2.id_dep = m.id_dep AND p2.sal = m.min_salary
ORDER BY 
    id_dep, salary_type;
