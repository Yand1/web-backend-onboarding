DROP TABLE IF EXISTS notes;

CREATE TABLE notes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  note TEXT UNIQUE NOT NULL,
  completed INTEGER NOT NULL
);
