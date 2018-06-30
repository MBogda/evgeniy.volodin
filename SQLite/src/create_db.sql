DROP TABLE IF EXISTS State;
CREATE TABLE State (
  id     INTEGER PRIMARY KEY,
  svalue  TEXT
);
INSERT INTO State(svalue) VALUES ('Sunny');
INSERT INTO State(svalue) VALUES ('Partly sunny');
INSERT INTO State(svalue) VALUES ('Cloudy');
INSERT INTO State(svalue) VALUES ('Partly cloudy');
INSERT INTO State(svalue) VALUES ('Foggy');
INSERT INTO State(svalue) VALUES ('Rainy');
INSERT INTO State(svalue) VALUES ('Snowy');

DROP TABLE IF EXISTS Direction;
CREATE TABLE Direction (
  id     INTEGER PRIMARY KEY,
  dvalue  TEXT
);
INSERT INTO Direction(dvalue) VALUES ('North');
INSERT INTO Direction(dvalue) VALUES ('Northeast');
INSERT INTO Direction(dvalue) VALUES ('East');
INSERT INTO Direction(dvalue) VALUES ('Southeast');
INSERT INTO Direction(dvalue) VALUES ('South');
INSERT INTO Direction(dvalue) VALUES ('Southwest');
INSERT INTO Direction(dvalue) VALUES ('West');
INSERT INTO Direction(dvalue) VALUES ('Northwest');

DROP TABLE IF EXISTS City;
CREATE TABLE City (
  id     INTEGER PRIMARY KEY,
  cvalue  TEXT
);
INSERT INTO City(cvalue) VALUES ('Moscow');
INSERT INTO City(cvalue) VALUES ('Saint Petersburg');
INSERT INTO City(cvalue) VALUES ('Novosibirsk');
INSERT INTO City(cvalue) VALUES ('Yekaterinburg');
INSERT INTO City(cvalue) VALUES ('Nizhny Novgorod');
INSERT INTO City(cvalue) VALUES ('Kazan');
INSERT INTO City(cvalue) VALUES ('Chelyabinsk');
INSERT INTO City(cvalue) VALUES ('Omsk');
INSERT INTO City(cvalue) VALUES ('Samara');
INSERT INTO City(cvalue) VALUES ('Rostov-on-Don');
INSERT INTO City(cvalue) VALUES ('Ufa');
INSERT INTO City(cvalue) VALUES ('Krasnoyarsk');
INSERT INTO City(cvalue) VALUES ('Perm');
INSERT INTO City(cvalue) VALUES ('Voronezh');
INSERT INTO City(cvalue) VALUES ('Volgograd');
INSERT INTO City(cvalue) VALUES ('Krasnodar');
INSERT INTO City(cvalue) VALUES ('Saratov');
INSERT INTO City(cvalue) VALUES ('Tyumen');
INSERT INTO City(cvalue) VALUES ('Tolyatti');
INSERT INTO City(cvalue) VALUES ('Izhevsk');

DROP TABLE IF EXISTS Observation;
CREATE TABLE Observation (
  oid      INTEGER PRIMARY KEY,
  datetime  DATETIME,
  city  INTEGER REFERENCES City (id),
  state   INTEGER REFERENCES State (id),
  temperature   REAL,
  precipitation   REAL,
  presure   REAL,
  wind_direction  INTEGER REFERENCES Direction (id),
  wind_value  REAL
);
