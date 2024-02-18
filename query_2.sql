SELECT avg(ocena) AS avg_ocena, student AS student_id, przedmiot_id
FROM Oceny
GROUP BY student_id, przedmiot_id
ORDER BY avg_ocena DESC 
LIMIT 1;