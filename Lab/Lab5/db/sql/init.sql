CREATE TABLE IF NOT EXISTS meal (
    meal_id SERIAL PRIMARY KEY,
    meal_name TEXT NOT NULL,
    meal_price INTEGER NOT NULL
);

INSERT INTO meal(meal_name, meal_price) VALUES ('Burger', 11);
INSERT INTO meal(meal_name, meal_price) VALUES ('Fish', 22);
INSERT INTO meal(meal_name, meal_price) VALUES ('Pizza', 13);
INSERT INTO meal(meal_name, meal_price) VALUES ('Beef', 24);
INSERT INTO meal(meal_name, meal_price) VALUES ('Sandwich', 15);
INSERT INTO meal(meal_name, meal_price) VALUES ('Turkey', 16);
INSERT INTO meal(meal_name, meal_price) VALUES ('Dumplings', 27);
INSERT INTO meal(meal_name, meal_price) VALUES ('Hotpot', 18);
INSERT INTO meal(meal_name, meal_price) VALUES ('Dumsum', 29);
INSERT INTO meal(meal_name, meal_price) VALUES ('Noodle', 10);
INSERT INTO meal(meal_name, meal_price) VALUES ('Taco', 11);
INSERT INTO meal(meal_name, meal_price) VALUES ('Chaofan', 22);
INSERT INTO meal(meal_name, meal_price) VALUES ('Baozi', 13);
INSERT INTO meal(meal_name, meal_price) VALUES ('Wantan', 24);
INSERT INTO meal(meal_name, meal_price) VALUES ('Meatball', 15);
