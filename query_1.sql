SELECT avg(ocena) AS avg_ocena, student AS student_id
FROM Oceny
GROUP BY student_id
ORDER BY avg_ocena DESC 
limit 5;