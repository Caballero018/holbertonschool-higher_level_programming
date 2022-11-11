-- Script that computes the score average of all records in the table second_table.
ALTER TABLE second_table ADD average INT;
INTO INSERT second_table (average) VALUES (avg(score));
SELECT average FROM second_table;
