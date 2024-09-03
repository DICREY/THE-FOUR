-- Active: 1721867436095@@localhost@3306@mascotas_db

DELIMITER //

CREATE PROCEDURE InsertarVeterinario(
    IN p_id_usuario VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(100)
)
BEGIN 
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;
    START TRANSACTION;
    INSERT INTO mascotas_db.usuarios(
        id_usuario,
        nombre,
        apellido,
        ciudad,
        direccion,
        telefono,
        es_propietario,
        es_veterinario,
        email,
        contrasenna) 
        VALUES(
            p_id_usuario,
            p_nombre,
            p_apellido,
            p_ciudad,
            p_direccion,
            p_telefono,
            0,
            1,
            p_email,
            p_contrasenna);
    INSERT INTO mascotas_db.veterinarios(id_usuario,especialidad,horario)
    VALUES(p_id_usuario,p_especialidad,p_horario);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarVeterinario(
    IN p_id_usuario VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(100) 
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END ;

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

    UPDATE mascotas_db.veterinarios
    SET especialidad = p_especialidad,
        horario = p_horario
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.EliminarVeterinarios(
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

    DELETE FROM mascotas_db.usuarios
    WHERE id_usuario = p_id_usuario;

    DELETE FROM mascotas_db.veterinarios
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarVeterinarioID(
    IN p_id_usuario VARCHAR(20)
)
BEGIN
    SELECT 
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email,
        v.especialidad,
        v.horario
    FROM
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.veterinarios v ON u.id_usuario = v.id_usuario
    WHERE
        v.id_usuario = p_id_usuario;
END //

CREATE PROCEDURE mascotas_db.BuscarVeterinarioNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    SELECT 
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email,
        v.especialidad,
        v.horario
    FROM
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.veterinarios v ON u.id_usuario = v.id_usuario
    WHERE
        nombre LIKE CONCAT("%",p_nombre,"%");
END //

CREATE PROCEDURE mascotas_db.BuscarVeterinarios()
BEGIN
    SELECT 
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email,
        v.especialidad,
        v.horario
    FROM
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.veterinarios v ON u.id_usuario = v.id_usuario;
END //