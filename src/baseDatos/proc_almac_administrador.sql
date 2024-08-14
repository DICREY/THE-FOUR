CREATE PROCEDURE InsertarAdministrador(
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