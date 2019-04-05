CREATE TABLE `memory` (id int);
ALTER TABLE memory ADD COLUMN qq_account varchar(20);
ALTER TABLE memory ADD COLUMN mKey varchar(50);
ALTER TABLE memory ADD COLUMN mValue varchar(200);
ALTER TABLE memory DROP COLUMN id;
