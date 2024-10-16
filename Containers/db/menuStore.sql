CREATE DATABASE IF NOT EXISTS menu_store;

USE menu_store;

-- create table with burgers
CREATE TABLE IF NOT EXISTS menu_store.menu_item (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  ingredients VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- create table with ingredients
CREATE TABLE IF NOT EXISTS menu_store.ingredients (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- create table with burger ingredients
CREATE TABLE IF NOT EXISTS menu_store.menu_item_ingredients (
  name VARCHAR(100) NOT NULL,
  ingredients VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- inserting burgers into menu_items
INSERT INTO menu_item (name) VALUES ("signeburgare");
INSERT INTO menu_item (name) VALUES ("eidamburgare");
INSERT INTO menu_item (name) VALUES ("mostafaburgare");

-- inserting ingredients into ingredients
INSERT INTO ingredients (name) VALUES ("bread");
INSERT INTO ingredients (name) VALUES ("plantbeef");
INSERT INTO ingredients (name) VALUES ("sauce");
INSERT INTO ingredients (name) VALUES ("onion");
INSERT INTO ingredients (name) VALUES ("halloumi");
INSERT INTO ingredients (name) VALUES ("salad");
INSERT INTO ingredients (name) VALUES ("tomato");
INSERT INTO ingredients (name) VALUES ("meat");
INSERT INTO ingredients (name) VALUES ("cheddar");
INSERT INTO ingredients (name) VALUES ("pickle");
INSERT INTO ingredients (name) VALUES ("ranch mayo");
INSERT INTO ingredients (name) VALUES ("portabello mushroom");
INSERT INTO ingredients (name) VALUES ("avocado");
INSERT INTO ingredients (name) VALUES ("cucumber");

-- inserting menu_item_ingredients where ingredients for each burger is a string with ingredients separated with comma
INSERT INTO menu_item_ingredients (name, ingredients) VALUES ("signeburgare", "bread,halloumi,sauce,onion,salad,avocado");
INSERT INTO menu_item_ingredients (name, ingredients) VALUES ("mostafaburgare", "bread,plantbeef,sauce,onion,salad,tomato,cucumber");
INSERT INTO menu_item_ingredients (name, ingredients) VALUES ("eidamburgare", "bread,meat,cheddar,pickle,ranch mayo,portabello mushroom");
