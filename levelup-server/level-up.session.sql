SELECT * FROM levelupapi_gametype;
SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;
SELECT * FROM levelupapi_event;

DELETE 
FROM levelupapi_event
WHERE id = 2;
DELETE 
FROM levelupapi_event
WHERE id = 5;
DELETE 
FROM levelupapi_event
WHERE id = 6;

DROP TABLE levelupapi_event;