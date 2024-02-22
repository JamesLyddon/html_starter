DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 1', 2000, 5);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 2', 1995, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 3', 2012, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 4', 1989, 4);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Punk');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Disco');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');