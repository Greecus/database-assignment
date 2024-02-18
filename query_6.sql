SELECT s.imie, s.nazwisko
FROM Studenci AS s
FULL JOIN StudenciWGrupach AS sg ON s.student_id = sg.student_id
WHERE sg.grupa_id = 5;