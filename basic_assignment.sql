CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

INSERT INTO Ages (name, age) VALUES ('Saarah', 22);
INSERT INTO Ages (name, age) VALUES ('Kean', 22);
INSERT INTO Ages (name, age) VALUES ('Ammarah', 19);
INSERT INTO Ages (name, age) VALUES ('Fion', 24);
INSERT INTO Ages (name, age) VALUES ('Orin', 26);
INSERT INTO Ages (name, age) VALUES ('Gareth', 17);

SELECT hex(name || age) AS X FROM Ages ORDER BY X

