CREATE PROCEDURE mascotas_db.InsertarMascota(
    IN p_id INT UNSIGNED,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad INT UNSIGNED, 
    IN p_peso FLOAT,
    IN p_id_propietario INT UNSIGNED
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_bd.mascotas VALUES
    (p_id,p_nombre,p_especie,p_raza,p_edad,p_peso,p_id_propietario);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarMascota(
    IN p_id INT UNSIGNED,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad INT UNSIGNED, 
    IN p_peso FLOAT,
    IN p_id_propietario INT UNSIGNED
) 
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_bd.mascotas
    SET nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso,
        id_propietario = p_id_propietario
    WHERE id = p_id;
    
    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.EliminarMascota(
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    DELETE FROM mascotas_bd.mascotas
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarMascotaID(
    IN p_id_mascota INT UNSIGNED
)
BEGIN
    SELECT 
        u.nombre AS nombre,
        u.raza,
        u.especie, 
        u.peso,
        u.edad,
        u.sexo,
        m.nombre AS nombre_propietario
    FROM
        mascotas_db.mascotas u
    INNER JOIN 
        mascotas_db.propietarios p ON u.id_propietario = p.id_usuario
    INNER JOIN
        mascotas_db.usuarios m ON p.id_usuario = m.id_usuario
    WHERE
        u.id = p_id_mascota;
END //