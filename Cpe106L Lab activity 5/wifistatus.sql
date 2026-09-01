PRAGMA foreign_keys = ON;
DROP Table IF EXISTS WIFISESSIONS;
CREATE TABLE WIFISESSIONS(
    device_number INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    connection_status TEXT CHECK(connection_status IN ('CONNECTED','DISCONNECTED', 'QUEUING')) NOT NULL DEFAULT 'QUEUING',
    joined_at TEXT DEFAULT (datetime('now'))
);

