CREATE PROCEDURE mascotas_db.InsertarProducto(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_descripcion VARCHAR(100),
    IN p_precio DECIMAL(20,5),
    IN p_stock SMALLINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_db.productos VALUES(p_id,p_nombre,p_descripcion,p_precio,p_stock);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarProducto(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_descripcion VARCHAR(100),
    IN p_precio DECIMAL(20,5),
    IN p_stock SMALLINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_db.productos
    SET nombre = p_nombre,
        descripcion = p_descripcion,
        precio = p_precio,
        stock = p_stock
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //
