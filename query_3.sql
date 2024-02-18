SELECT avg(m.ocena) AS avg_ocena, m.grupa_id, m.przedmiot_nazwa
FROM (SELECT o.ocena_id, o.ocena, o.student, g.grupa_id, p.przedmiot_id, p.przedmiot_nazwa
        FROM Oceny AS o
        FULL JOIN StudenciWGrupach AS sg ON o.student = sg.student_id 
        FULL JOIN Grupy AS g ON sg.grupa_id = g.grupa_id 
        FULL JOIN Przedmioty AS p ON g.przedmiot_id = p.przedmiot_id
        WHERE p.przedmiot_nazwa = 'Biologia' ) AS m
GROUP BY m.grupa_id, m.przedmiot_nazwa
ORDER BY avg_ocena DESC;