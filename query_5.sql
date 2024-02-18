SELECT p.przedmiot_nazwa
FROM Przedmioty AS p
FULL JOIN Wykladowcy AS w ON p.wykladowca = w.wykladowca_id
WHERE w.nazwisko = 'nazwisko';
