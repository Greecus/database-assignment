SELECT s.imie, s.nazwisko, o.ocena
FROM Oceny AS o
FULL JOIN Studenci AS s ON o.student = s.student_id
FULL JOIN StudenciWGrupach AS sg ON o.student = sg.student_id 
FULL JOIN Grupy AS g ON sg.grupa_id = g.grupa_id 
FULL JOIN Przedmioty AS p ON g.przedmiot_id = p.przedmiot_id
WHERE g.grupa_id = 1 AND p.przedmiot_nazwa = 'Chemia';