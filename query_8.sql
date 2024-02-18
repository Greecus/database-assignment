SELECT avg(o.ocena)
FROM Oceny AS o
FULL JOIN Studenci AS s ON o.student = s.student_id
FULL JOIN Przedmioty AS p ON o.przedmiot_id = p.przedmiot_id
FULL JOIN Wykladowcy AS w ON p.wykladowca = w.wykladowca_id
WHERE w.nazwisko = 'nazwisko' AND p.przedmiot_nazwa = 'Chemia';