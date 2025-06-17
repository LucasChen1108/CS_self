PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "birthday"(
"Year" TEXT, "Date" TEXT, "Name" TEXT);
INSERT INTO birthday VALUES('2007','09/26','M+7');
INSERT INTO birthday VALUES('2007','07/18','Mo Haoyu');
INSERT INTO birthday VALUES('2007','03/14','Rita');
INSERT INTO birthday VALUES('2006','11/08','Lucas');
INSERT INTO birthday VALUES('2006','10/31','Cecilia');
INSERT INTO birthday VALUES('2006','07/25','Ryan');
INSERT INTO birthday VALUES('2007','05/31','Shan Gou');
INSERT INTO birthday VALUES('2006','12/31','Meng');
INSERT INTO birthday VALUES('2006','12/19','YY Chen');
INSERT INTO birthday VALUES('2007','04/21','Zuo');
COMMIT;
