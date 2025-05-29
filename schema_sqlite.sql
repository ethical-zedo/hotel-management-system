-- ----------  DDL  ----------
PRAGMA foreign_keys = ON;

CREATE TABLE Hotel (
    id           INTEGER PRIMARY KEY,
    ville        TEXT NOT NULL,
    pays         TEXT NOT NULL,
    code_postal  INTEGER
);

CREATE TABLE Client (
    id           INTEGER PRIMARY KEY,
    adresse      TEXT,
    ville        TEXT,
    code_postal  INTEGER,
    email        TEXT UNIQUE,
    telephone    TEXT,
    nom          TEXT NOT NULL
);

CREATE TABLE Prestation (
    id           INTEGER PRIMARY KEY,
    prix         REAL,
    description  TEXT
);

CREATE TABLE TypeChambre (
    id           INTEGER PRIMARY KEY,
    libelle      TEXT,
    prix_nuit    REAL
);

CREATE TABLE Chambre (
    id               INTEGER PRIMARY KEY,
    numero           INTEGER,
    etage            INTEGER,
    est_fumeur       INTEGER DEFAULT 0,            -- 0 = non-fumeur, 1 = fumeur
    id_type_chambre  INTEGER NOT NULL,
    id_hotel         INTEGER NOT NULL,
    FOREIGN KEY (id_type_chambre) REFERENCES TypeChambre(id),
    FOREIGN KEY (id_hotel)        REFERENCES Hotel(id)
);

CREATE TABLE Reservation (
    id            INTEGER PRIMARY KEY,
    date_debut    DATE    NOT NULL,
    date_fin      DATE    NOT NULL,
    id_client     INTEGER NOT NULL,
    id_chambre    INTEGER NOT NULL,
    FOREIGN KEY (id_client)  REFERENCES Client(id),
    FOREIGN KEY (id_chambre) REFERENCES Chambre(id)
);

CREATE TABLE Evaluation (
    id           INTEGER PRIMARY KEY,
    date_eval    DATE,
    note         INTEGER CHECK(note BETWEEN 0 AND 5),
    commentaire  TEXT,
    id_client    INTEGER,
    FOREIGN KEY (id_client) REFERENCES Client(id)
);
