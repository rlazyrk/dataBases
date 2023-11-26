INSERT INTO iot_db.places (`addresses`, `Place_name`)
VALUES
    ('вул. Личаківська 23', 'Львівський оперний театр'),
    ('пл. Ринок 1', 'Львівська ратуша'),
    ('вул. Вірменська 20', 'Музей книги в Львові'),
    ('пл. Музеїв 1', 'Львівський музей'),
    ('вул. Шевська 3', 'Арсенал (музей)'),
    ('пл. Леона 1', 'Домініканський собор'),
    ('вул. Краківська 8', 'Арена Львів'),
    ('вул. Бандери 15', 'Центр мистецтв "Арсенал"'),
    ('вул. Галицька 18', 'Парк ім. Б. Хмельницького'),
    ('вул. Коперника 73', 'Львівська галерея мистецтв');

INSERT INTO iot_db.artists (`genre`, `Artist_name`)
VALUES
('Рок', 'Іван Дорн'),
('Поп', 'Оля Полякова'),
('Електронна музика', 'The Maneken'),
('Реп', 'Артем Пивоваров'),
('Фольк', 'ДахаБраха'),
('Джаз', 'Олег Скрипка'),
('Поп', 'MONATIK'),
('Рок', 'Скрябін'),
('Електронна музика', 'Alina Pash'),
('Реп', 'Zhadan i sobaki'),
('Фольк', 'Друга Ріка'),
('Джаз', 'TNMK');

INSERT INTO iot_db.events (`eventname`, `datetime`, `Places_idPlaces`)
VALUES
('Концерт "Рок вечірка"', '2023-11-01 18:00:00', 2),
('Театральна постанова "Лісова пісня"', '2023-11-05 19:30:00', 3),
('Виставка "Сучасне мистецтво"', '2023-11-10 15:00:00', 1),
('Концерт "Джазові ноти"', '2023-11-15 20:00:00', 7),
('Театральна постанова "Ромео і Джульєтта"', '2023-11-20 19:00:00', 5),
('Концерт "Електронна музика"', '2023-11-25 21:00:00', 6),
('Виставка "Сучасні тенденції"', '2023-11-30 16:30:00', 4),
('Театральна постанова "Король Лів"', '2023-12-05 18:45:00', 9),
('Концерт "Поп-музика наживо"', '2023-12-10 22:00:00', 10),
('Театральна постанова "Дивовижна країна Оз"', '2023-12-15 17:15:00', 8);

INSERT INTO iot_db.artists_events_connect (`Artists_idArtists`, `Events_idevent`)
VALUES
(2, 1),
(2, 2),(4, 5),(6, 4),
(5, 7),(6, 1),(7, 10),
(8, 9),(9, 10),(10, 10);

INSERT INTO iot_db.users (`User_name`, `User_lastname`, `User_email`, `User_phonenumber`)
VALUES
('Іван', 'Петров', 'ivan@example.com', '123456789'),
('Олена', 'Іванова', 'olena@example.com', '987654321'),
('Андрій', 'Сидоренко', 'andriy@example.com', '111223344'),
('Наталія', 'Коваль', 'nataliya@example.com', '998872665'),
('Олександр', 'Федоренко', 'oleksandr@example.com', '112233445'),
('Юлія', 'Сергіївна', 'yulia@example.com', '554433221'),
('Михайло', 'Мельник', 'mikhailo@example.com', '667788990'),
('Анастасія', 'Дмитрівна', 'anastasiya@example.com', '223344556'),
('Віктор', 'Григорович', 'viktor@example.com', '998877665'),
('Людмила', 'Ігорівна', 'lyudmyla@example.com', '112211221'),
('Артем', 'Васильович', 'artem@example.com', '334455667'),
('Ірина', 'Миколаївна', 'iryna@example.com', '778899001'),
('Дмитро', 'Анатолійович', 'dmytro@example.com', '0011223344');


INSERT INTO iot_db.seats (`Places_idPlaces`, `row`, `seat_number`, `free`)
VALUES
(1, 1, 1, 1),
(1, 2, 3, 1),
(1, 3, 2, 0),
(4, 4, 5, 1),
(5, 1, 6, 0),
(8, 2, 4, 1),
(7, 3, 1, 1),
(4, 4, 3, 0),
(9, 1, 2, 1),
(2, 2, 7, 1);

INSERT INTO iot_db.delivery (`Delivery_cost`, `Delivery_address`)
VALUES
(1000, 'вул. Шевська 10, Львів'),
(2000, 'вул. Коперника 25, Львів'),
(3000, 'пл. Ринок 5, Львів'),
(4000, 'вул. Личаківська 30, Львів'),
(5000, 'вул. Вірменська 15, Львів'),
(7000, 'вул. Галицька 40, Львів'),
(6000, 'вул. Бандери 22, Львів'),
(10000, 'вул. Краківська 12, Львів'),
(11111, 'вул. Леона 5, Львів'),
(121212, 'пл. Музеїв 3, Львів');

INSERT INTO iot_db.orders (`Users_idUsers`, `Order_date_time`, `Cost`, `Delivery_idDelivery`)
VALUES
(3, '2023-10-23 12:30:00', 1000, 10),
(1, '2023-10-23 14:45:00', 1234, 5),
(2, '2023-10-24 09:15:00', 65464, 8),
(5, '2023-10-24 11:30:00', 7654, 2),
(6, '2023-10-25 15:00:00', 2134, 2),
(4, '2023-10-26 17:45:00', 7564, 6),
(8, '2023-10-27 10:20:00', 21356, 6),
(7, '2023-10-27 13:15:00', 66666, 8),
(9, '2023-10-28 16:30:00', 12335, 3),
(2, '2023-10-28 18:45:00', 2546, 1),
(6, '2023-10-29 09:30:00', 11235, 9),
(7, '2023-10-29 12:15:00', 17677, 1),
(4, '2023-10-30 14:00:00', 100, 7),
(1, '2023-10-30 16:45:00', 12344, 2),
(9, '2023-10-31 18:30:00', 500, 4);

INSERT INTO iot_db.payments (`Orders_idOrders`, `Payment_status`)
VALUES
(7, 'Оплачено'),
(3, 'Очікується'),
(12, 'Оплачено'),
(9, 'Відмова'),
(2, 'Оплачено'),
(6, 'Оплачено'),
(15, 'Очікується'),
(8, 'Оплачено'),
(5, 'Відмова'),
(1, 'Оплачено'),
(14, 'Оплачено'),
(11, 'Оплачено'),
(10, 'Оплачено'),
(4, 'Відмова'),
(13, 'Оплачено');


INSERT INTO iot_db.traveltickets (`Orders_idOrders`, `Transport_type`, `Cost`, `Date_time`)
VALUES
(9, 'Поїзд', 250, '2023-11-01 12:00:00'),
(4, 'Автобус', 180, '2023-11-05 14:30:00'),
(6, 'Літак', 500, '2023-11-08 10:15:00'),
(12, 'Автобус', 190, '2023-11-12 09:45:00'),
(8, 'Поїзд', 220, '2023-11-16 11:20:00'),
(15, 'Літак', 480, '2023-11-20 13:10:00'),
(3, 'Автобус', 210, '2023-11-24 15:40:00'),
(7, 'Поїзд', 260, '2023-11-28 17:25:00'),
(13, 'Літак', 510, '2023-12-02 19:15:00'),
(1, 'Автобус', 195, '2023-12-06 21:00:00'),
(11, 'Поїзд', 230, '2023-12-10 22:45:00'),
(5, 'Літак', 490, '2023-12-14 01:30:00'),
(10, 'Автобус', 205, '2023-12-18 03:15:00'),
(2, 'Поїзд', 240, '2023-12-22 05:00:00'),
(14, 'Літак', 520, '2023-12-26 07:45:00'),
(9, 'Автобус', 195, '2023-11-02 14:20:00'),
(4, 'Літак', 480, '2023-11-06 16:10:00'),
(6, 'Поїзд', 245, '2023-11-09 18:00:00'),
(12, 'Автобус', 200, '2023-11-13 20:00:00'),
(8, 'Літак', 510, '2023-11-17 22:00:00');

INSERT INTO iot_db.tickets (`Orders_idOrders`, `Events_idevent`, `Seats_idSeats`, `Seats_Places_idPlaces`)
VALUES
(5, 7, 9, 2),
(8, 3, 5, 6),
(10, 8, 6, 3),
(2, 4, 10, 1),
(6, 2, 4, 9),
(4, 1, 8, 5),
(3, 6, 7, 10),
(1, 9, 3, 4),
(7, 10, 1, 8),
(9, 10, 2, 7),
(11, 5, 5, 6),
(12, 1, 8, 3),
(15, 4, 10, 9),
(14, 2, 3, 1),
(13, 7, 9, 10);