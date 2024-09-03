-- Active: 1721867436095@@localhost@3306
DELIMITER //

CREATE PROCEDURE mascotas_db.InsertarAdministrador(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_cargo VARCHAR(100),
    IN p_fec_ing DATE
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_bd.usuarios(
        id_usuario,
        nombre,
        apellido,
        ciudad,
        direccion,
        telefono,
        es_propietario,
        es_veterinario,
        es_administrador,
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
        0,
        0,
        1,
        p_email,
        p_contrasenna
    );

    INSERT INTO mascotas_bd.administradores(id_usuario,cargo,fecha_ingreso) 
    VALUES(p_id_usuario,p_cargo,p_fec_ing);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarAdministrador(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contrasenna VARCHAR(100),
    IN p_cargo VARCHAR(100),
    IN p_fec_ing DATE
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_bd.usuarios
    SET nombre = p_nombre,
        apellido = p_apellido,
        ciudad = p_ciudad,
        direccion = p_direccion,
        telefono = p_telefono,
        email = p_email,
        contrasenna = p_contrasenna
    WHERE id_usuario = p_id_usuario;

    UPDATE mascotas_bd.administradores
    SET cargo = p_cargo,
        fecha_ingreso = p_fec_ing
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.EliminarAdministrador(
    IN p_id_usuario INT UNSIGNED
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

    DELETE FROM mascotas_db.administradores
    WHERE id_usuario = p_id_usuario;

    COMMIT;
    set autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarAdministradorID(
    IN p_id_usuario INT
)
BEGIN
    SELECT 
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email,
        u.contrasenna,
        a.cargo,
        a.fecha_ingreso
    FROM 
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.administradores a ON u.id_usuario = a.id_usuario
    WHERE 
        a.id_usuario = p_id_usuario;
END //

CREATE PROCEDURE mascotas_db.BuscarAdministradorNombre(
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
        u.contrasenna,
        a.cargo,
        a.fecha_ingreso
    FROM 
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.administradores a ON u.id_usuario = a.id_usuario
    WHERE 
        u.nombre = p_nombre;
END //

CREATE PROCEDURE mascotas_db.BuscarAdministradores()
BEGIN
    SELECT 
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email,
        u.contrasenna,
        a.cargo,
        a.fecha_ingreso
    FROM 
        mascotas_db.usuarios u
    INNER JOIN 
        mascotas_db.administradores a ON u.id_usuario = a.id_usuario;
END //