mysql -h localhost -u root -p'UncleClam3!' -e "use clam_db; load data local infile 'urine.csv' into table piss_table
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
"