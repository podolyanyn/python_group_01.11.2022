CREATE TABLE City ("index" int, name varchar(200));

ALTER TABLE City RENAME TO Exstend_City;
ALTER TABLE Exstend_City ADD population int;
INSERT INTO Exstend_City VALUES (01001, 'Kiev', 2884000000);
INSERT INTO Exstend_City VALUES (30000, 'Slavuta', 35000);
INSERT INTO Exstend_City VALUES (79007, 'Lviv', 721301);

SELECT * FROM Exstend_City ORDER BY population DESC ;
DELETE FROM Exstend_City WHERE population < 36000 ;



