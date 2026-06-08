use `online`;
show tables;
drop table `users`;

create table if not exists `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(999) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  primary key (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

describe product;
select * from product;
drop table 	`product`;

CREATE TABLE `product` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL,
	`name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`image` text COLLATE utf8mb4_unicode_ci NOT NULL,
	`price` int COLLATE utf8mb4_unicode_ci NOT NULL,
	 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

INSERT INTO `product`(id, name, code, image, price) VALUES (1, "Desktop1", "D01" , "desktop1.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (2, "Desktop2", "D02" , "desktop2.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (3, "Desktop3", "D03" , "desktop3.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (4, "Desktop4", "D04" , "desktop4.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (5, "Desktop5", "D05" , "desktop5.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (6, "Desktop6", "D06" , "desktop6.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (7, "Desktop7", "D07" , "desktop7.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (8, "Desktop8", "D08" , "desktop8.jpg", "2000");

INSERT INTO `product`(id, name, code, image, price) VALUES (9,  "Laptop1", "L01" , "laptop1.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (10, "Laptop2", "L02" , "laptop2.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (11, "Laptop3", "L03" , "laptop3.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (12, "Laptop4", "L04" , "laptop4.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (13, "Laptop5", "L05" , "laptop5.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (14, "Laptop6", "L06" , "laptop6.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (15, "Laptop7", "L07" , "laptop7.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (16, "Laptop8", "L08" , "laptop8.jpg", "2000");

INSERT INTO `product`(id, name, code, image, price) VALUES (17, "Cellphone1", "C01" , "cellphone1.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (18, "Cellphone2", "C02" , "cellphone2.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (19, "Cellphone3", "C03" , "cellphone3.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (20, "Cellphone4", "C04" , "cellphone4.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (21, "Cellphone5", "C05" , "cellphone5.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (22, "Cellphone6", "C06" , "cellphone6.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (23, "Cellphone7", "C07" , "cellphone7.jpg", "2000");
INSERT INTO `product`(id, name, code, image, price) VALUES (24, "Cellphone8", "C08" , "cellphone8.jpg", "2000");














