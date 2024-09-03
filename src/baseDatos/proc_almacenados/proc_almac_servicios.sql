DELIMITER //

CREATE PROCEDURE mascotas_db.InsertarServicio(
    IN p_id VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(18,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_db.servicios VALUES(p_id,p_nombre,p_descripcion,p_precio);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarServicio(
    IN p_id VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(18,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_db.servicios
    SET id = p_id,
        nombre = p_nombre,
        descripcion = p_descripcion,
        precio = p_precio
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.EliminarServicio(
    IN p_id VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    DELETE FROM mascotas_db.servicios
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarServicioID(
    IN p_id VARCHAR(20)
)
BEGIN
    SELECT * FROM mascotas_db.servicios
    WHERE id = p_id;
END //

CREATE PROCEDURE mascotas_db.BuscarServicioNombre(
    IN p_nombre VARCHAR(20)
)
BEGIN
    SELECT * FROM mascotas_db.servicios
    WHERE nombre LIKE CONCAT("%",p_nombre,"%");
END //

CREATE PROCEDURE mascotas_db.BuscarServicios()
BEGIN
    SELECT * FROM mascotas_db.servicios;
END //