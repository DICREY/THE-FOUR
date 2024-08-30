DELIMITER //

CREATE PROCEDURE mascotas_db.Login(
    IN p_email VARCHAR(50),
    IN p_password VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    SELECT email,contrasenna FROM mascotas_db.usuarios
    WHERE email LIKE p_email AND contrasenna LIKE p_password;

    COMMIT;
    SET autocommit = 1;
END //

CALL `Login`()