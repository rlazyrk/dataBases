USE iot_db;

DROP TRIGGER IF EXISTS beforeInsertReferrals;

DELIMITER //
CREATE TRIGGER beforeInsertReferrals BEFORE INSERT ON iot_db.referrals
FOR EACH ROW
BEGIN
    IF NOT EXISTS (
        SELECT * FROM iot_db.users
        WHERE idUsers = NEW.user_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'USER з таким id не знайдений';
    END IF;
END;
// DELIMITER ;

DROP TRIGGER IF EXISTS blockEndWithOO;

DELIMITER //
CREATE TRIGGER blockEndWithOO BEFORE INSERT ON iot_db.traveltickets
FOR EACH ROW
BEGIN
    IF NEW.Cost % 100 = 0 THEN
        SIGNAL SQLSTATE '45000';
        SET MESSAGE_TEXT = 'Ціна не може закінчуватись на 2 нулі';
    END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS blockUpdate

DELIMITER //
CREATE TRIGGER blockUpdate BEFORE UPDATE ON iot_db.orders
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000';
    SET MESSAGE_TEXT = 'Модифікацію заборонено'
END //
DELIMITER

CREATE TABLE IF NOT EXISTS loggingTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    updateTime TIMESTAMP
);

DROP TRIGGER IF EXISTS loggingArtists;

DELIMITER //
CREATE TRIGGER loggingArtists BEFORE UPDATE ON iot_db.artists
FOR EACH ROW
BEGIN
    INSERT INTO loggingTable (updateTime) VALUES (NOW());
END //
DELIMITER ;