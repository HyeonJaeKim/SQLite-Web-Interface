DROP TABLE IF EXISTS 'billboard_hot';
CREATE TABLE IF NOT EXISTS 'billboard_hot'(
	'url'	TEXT,
	'WeekID'	TEXT,
	'Week_Position'	INTEGER,
	'Song'	TEXT,
	'Performer'	TEXT,
	'SongID'	TEXT,
	'Instance'	INTEGER,
	'Previous_Week_Position'	INTEGER,
	'Peak_Position'	INTEGER,
	'Weeks_On_Chart'	INTEGER
);
