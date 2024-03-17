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
WITH SalaryRank AS (
    SELECT 
        id_dep,
        name,
        sal,
        RANK() OVER (PARTITION BY id_dep ORDER BY sal DESC) AS max_salary_rank,
        RANK() OVER (PARTITION BY id_dep ORDER BY sal ASC) AS min_salary_rank
    FROM 
        Personal
)

SELECT 
    p.name AS employee_name,
    d.name AS department_name,
    p.sal AS salary
FROM 
    SalaryRank s
JOIN 
    Department d ON s.id_dep = d.id
JOIN 
    Personal p ON s.id_dep = p.id_dep
WHERE 
    s.max_salary_rank = 1 OR s.min_salary_rank = 1;