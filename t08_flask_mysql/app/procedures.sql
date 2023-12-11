DROP PROCEDURE IF EXISTS ParameterInsertUser;

DELIMITER //
CREATE PROCEDURE ParameterInsertUser(IN insert_name VARCHAR(45), IN insert_lastname VARCHAR(45),
    IN insert_email VARCHAR(45), IN insert_phoneNumber VARCHAR(45))
BEGIN
    INSERT INTO iot_db.users (`User_name`, `User_lastname`, `User_email`, `User_phonenumber`)
    VALUES (insert_name, insert_lastname, insert_email, insert_phoneNumber);
END //
DELIMITER ;



DROP PROCEDURE IF EXISTS GeneratedUsersInsert;

DELIMITER //
CREATE PROCEDURE GeneratedUsersInsert(IN insert_name VARCHAR(45))
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE insert_value VARCHAR(45);

    WHILE i < 11 DO
        SET insert_value = CONCAT(insert_name, i);
        INSERT INTO iot_db.users (`User_name`, `User_lastname`, `User_email`, `User_phonenumber`)
        VALUES (insert_value, 'defaultLastName', 'defaultEmail', 'defaultPhoneNumber');
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS ManyToManyConnectArtists_to_Events;


DELIMITER //
CREATE PROCEDURE ManyToManyConnectArtists_to_Events(IN artist_id INT, IN event_id INT)
BEGIN
    IF EXISTS (
        SELECT * FROM iot_db.events
        WHERE idevent = event_id
    )
    THEN
        IF NOT EXISTS (
            SELECT Artists_idArtists, Events_idevent FROM iot_db.artists_events_connect
            WHERE Artists_idArtists = artist_id AND Events_idevent = event_id
        )
        THEN
            INSERT INTO iot_db.artists_events_connect (Artists_idArtists, Events_idevent)
            VALUES (artist_id, event_id);
        END IF;
    END IF;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS MinMaxAvgSumOrdersCost;

DELIMITER //
CREATE PROCEDURE MinMaxAvgSumOrdersCost(IN operator VARCHAR(25))
BEGIN
     DECLARE result DECIMAL(10, 2);
    IF(operator = 'MAX')
        THEN SELECT MAX(Cost) INTO result FROM iot_db.orders
    ELSEIF (operator = 'MIN')
        THEN SELECT MIN(Cost) INTO result FROM iot_db.orders
    ELSEIF (operator = 'AVG')
        THEN SELECT AVG(Cost) INTO result FROM iot_db.orders
    ELSEIF (operator = 'SUM')
        THEN SELECT SUM(Cost) INTO result FROM iot_db.orders
    END IF;
END//
DELIMITER ;


DROP PROCEDURE IF EXISTS CursorProcedureFirstTask;

DELIMITER //
CREATE PROCEDURE CursorProcedureFirstTask(IN db_name1 VARCHAR(25), IN db_name2 VARCHAR(25))
BEGIN
    DECLARE first_table VARCHAR(50);
    DECLARE second_table VARCHAR(50);
    DECLARE random_choice INT;
    DECLARE done BOOLEAN DEFAULT FALSE;

    DECLARE idPlaces INT;
    DECLARE addresses VARCHAR(45);
    DECLARE Place_name VARCHAR(45);

    DECLARE cursor_task CURSOR FOR SELECT * FROM iot_db.places;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET first_table = CONCAT('first_part_', db_name1);
    SET second_table = CONCAT('second_part_', db_name2);

    SET @query1 = CONCAT('CREATE TABLE IF NOT EXISTS ', first_table, ' (idPlaces INT, addresses VARCHAR(45), Place_name VARCHAR(45))');
    PREPARE creating_first_table FROM @query1;
    EXECUTE creating_first_table;
    DEALLOCATE PREPARE creating_first_table;

    SET @query2 = CONCAT('CREATE TABLE IF NOT EXISTS ', second_table, ' (idPlaces INT, addresses VARCHAR(45), Place_name VARCHAR(45))');
    PREPARE creating_second_table FROM @query2;
    EXECUTE creating_second_table;
    DEALLOCATE PREPARE creating_second_table;

    OPEN cursor_task;

    generate_data: LOOP
        FETCH cur_place INTO idPlaces, addresses, Place_name;

        IF done THEN
            LEAVE generate_data;
        END IF;

        SET random_choice = FLOOR(RAND() * 2);

        IF random_choice = 0 THEN
            SET @insert_query = CONCAT('INSERT INTO ', first_table, ' VALUES (', idPlaces, ', "', REPLACE(addresses, '"', '\"'), '", "', REPLACE(Place_name, '"', '\"'), '")');
            PREPARE insert_stmt FROM @insert_query;
            EXECUTE insert_stmt;
            DEALLOCATE PREPARE insert_stmt;
        ELSEIF random_choice = 1 THEN
            SET @insert_query = CONCAT('INSERT INTO ', second_table, ' VALUES (', idPlaces, ', "', REPLACE(addresses, '"', '\"'), '", "', REPLACE(Place_name, '"', '\"'), '")');
            PREPARE insert_stmt FROM @insert_query;
            EXECUTE insert_stmt;
            DEALLOCATE PREPARE insert_stmt;
        END IF;
    END LOOP;

    CLOSE cursor_task;
END;
 //
DELIMITER ;
