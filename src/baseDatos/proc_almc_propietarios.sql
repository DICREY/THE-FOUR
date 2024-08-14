CREATE PROCEDURE InsertarPropietario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_barrio VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    SET autocommit = 0;
    START TRANSACTION;
    INSERT INTO mascotas_bd.usuarios (
        id_usuario,
        nombre,
        apellido,
        ciudad,
        direccion,
        telefono,
        email,
        contrasenna
    )
    VALUES(
        p_id_usuario,
        p_nombre,
        p_apellido,
        p_ciudad,
        p_direccion,
        p_telefono,
        p_email,
        p_contrasenna
    );
    INSERT INTO propietarios(id_usuario,barrio) VALUES(p_id_usuario,p_barrio);
    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE ActualizarPropietario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_barrio VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_bd.propietarios
    SET nombre = p_nombre,
        apellido = p_apellido,
        ciudad = p_ciudad,
        direccion = p_direccion,
        telefono = p_telefono,
        email = p_email,
        contrasenna = p_contrasenna,
        barrio = p_barrio
    WHERE id_usuario = p_id_usuario;
END //

CREATE PROCEDURE EliminarPropietario(
    IN p_id_usuario INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    DELETE FROM mascotas_bd.propietarios
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE BuscarPropietarioID(
    IN p_id_usuario INT
)
BEGIN
    SELECT 
        UPPER(u.nombre) AS nombre_usuario,
        UPPER(u.apellido) AS apellido_usuario,
        UPPER(u.ciudad) AS ciudad_usuario,
        UPPER(u.direccion) AS direccion_usuario,
        u.telefono,
        LOWER(u.email) AS email_usuario,
        UPPER(p.mascotas) AS mascotas_propietario
    FROM 
        mascotas_db.propietarios p
    INNER JOIN 
        mascotas_db.usuarios u ON p.id_usuario = u.id_usuario LIMIT 100;
END //