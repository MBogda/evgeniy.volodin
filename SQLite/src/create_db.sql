DROP TABLE IF EXISTS State;
CREATE TABLE State (
  id     INTEGER PRIMARY KEY,
  value  TEXT
);
INSERT INTO State(value) VALUES ('Sunny');
INSERT INTO State(value) VALUES ('Partly sunny');
INSERT INTO State(value) VALUES ('Cloudy');
INSERT INTO State(value) VALUES ('Partly cloudy');
INSERT INTO State(value) VALUES ('Foggy');
INSERT INTO State(value) VALUES ('Rainy');
INSERT INTO State(value) VALUES ('Snowy');

DROP TABLE IF EXISTS Direction;
CREATE TABLE Direction (
  id     INTEGER PRIMARY KEY,
  value  TEXT
);
INSERT INTO Direction(value) VALUES ('North');
INSERT INTO Direction(value) VALUES ('Northeast');
INSERT INTO Direction(value) VALUES ('East');
INSERT INTO Direction(value) VALUES ('Southeast');
INSERT INTO Direction(value) VALUES ('South');
INSERT INTO Direction(value) VALUES ('Southwest');
INSERT INTO Direction(value) VALUES ('West');
INSERT INTO Direction(value) VALUES ('Northwest');

DROP TABLE IF EXISTS City;
CREATE TABLE City (
  id     INTEGER PRIMARY KEY,
  value  TEXT
);
INSERT INTO City(value) VALUES ('Moscow');
INSERT INTO City(value) VALUES ('Saint Petersburg');
INSERT INTO City(value) VALUES ('Novosibirsk');
INSERT INTO City(value) VALUES ('Yekaterinburg');
INSERT INTO City(value) VALUES ('Nizhny Novgorod');
INSERT INTO City(value) VALUES ('Kazan');
INSERT INTO City(value) VALUES ('Chelyabinsk');
INSERT INTO City(value) VALUES ('Omsk');
INSERT INTO City(value) VALUES ('Samara');
INSERT INTO City(value) VALUES ('Rostov-on-Don');
INSERT INTO City(value) VALUES ('Ufa');
INSERT INTO City(value) VALUES ('Krasnoyarsk');
INSERT INTO City(value) VALUES ('Perm');
INSERT INTO City(value) VALUES ('Voronezh');
INSERT INTO City(value) VALUES ('Volgograd');
INSERT INTO City(value) VALUES ('Krasnodar');
INSERT INTO City(value) VALUES ('Saratov');
INSERT INTO City(value) VALUES ('Tyumen');
INSERT INTO City(value) VALUES ('Tolyatti');
INSERT INTO City(value) VALUES ('Izhevsk');

DROP TABLE IF EXISTS Observation;
CREATE TABLE Observation (
  id      INTEGER PRIMARY KEY,
  datetime  TIMESTAMP,
  city  INTEGER REFERENCES City (id),
  state   INTEGER REFERENCES State (id),
  temperature   REAL,
  precipitation   REAL,
  pressure   REAL,
  wind_direction  INTEGER REFERENCES Direction (id),
  wind_value  REAL
);
