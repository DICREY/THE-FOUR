-- Active: 1715350134884@@127.0.0.1@3306@mascotas_db

DELIMITER //

CREATE PROCEDURE mascotas_db.InsertarPropietario(
    IN p_id_usuario VARCHAR(20),
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
    INSERT INTO mascotas_db.usuarios (
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

CREATE PROCEDURE mascotas_db.ActualizarPropietario(
    IN p_id_usuario VARCHAR(20),
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

    UPDATE mascotas_db.usuarios
    SET nombre = p_nombre,
        apellido = p_apellido,
        ciudad = p_ciudad,
        direccion = p_direccion,
        telefono = p_telefono,
        email = p_email,
        contrasenna = p_contrasenna
    WHERE id_usuario = p_id_usuario;

    UPDATE mascotas_db.propietarios
    SET barrio = p_barrio
    WHERE id_usuario = p_id_usuario;
END //

CREATE PROCEDURE mascotas_db.EliminarPropietario(
    IN p_id_usuario VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    DELETE FROM mascotas_db.propietarios
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarPropietarioID(
    IN p_id_usuario VARCHAR(20)
)
BEGIN
    SELECT 
        u.nombre AS nombre,
        u.apellido AS apellido,
        u.ciudad AS ciudad,
        u.direccion AS direccion,
        u.telefono,
        u.email AS email,
        p.barrio 
    FROM
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.propietarios p ON u.id_usuario = p.id_usuario
    WHERE
        u.id_usuario = p_id_usuario;
END //

CREATE PROCEDURE mascotas_db.BuscarPropietarioNombre(
    IN p_nombre VARCHAR(100) 
)
BEGIN
    SELECT 
        u.nombre AS nombre,
        u.apellido AS apellido,
        u.ciudad AS ciudad,
        u.direccion AS direccion,
        u.telefono,
        u.email AS email,
        p.barrio 
    FROM
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.propietarios p ON u.id_usuario = p.id_usuario
    WHERE
        nombre LIKE CONCAT("%",p_nombre,"%");
END //

CREATE PROCEDURE mascotas_db.BuscarPropietarios(
)
BEGIN
    SELECT 
        u.nombre AS nombre,
        u.apellido AS apellido,
        u.ciudad AS ciudad,
        u.direccion AS direccion,
        u.telefono,
        u.email AS email,
        p.barrio 
    FROM
        propietarios p
    INNER JOIN 
        usuarios u ON p.id_usuario = u.id_usuario;
END //