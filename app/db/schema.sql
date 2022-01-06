PRAGMA foreign_keys = OFF;

DROP TABLE IF EXISTS close_prices;

PRAGMA foreign_keys = ON;

CREATE TABLE close_prices (
  value FLOAT,
  created_at DATETIME
);
