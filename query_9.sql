SELECT p.przedmiot_nazwa
FROM Studenci AS s
FULL JOIN StudenciWGrupach AS sg ON s.student_id = sg.student_id
FULL JOIN Grupy AS g ON sg.grupa_id = g.grupa_id
FULL JOIN Przedmioty AS p ON g.przedmiot_id = p.przedmiot_id
WHERE s.imie = 'imie' AND s.nazwisko = 'nazwisko';