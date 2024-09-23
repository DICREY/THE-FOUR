-- Active: 1727129487513@@127.0.0.1@3306@mascotas_db
DELIMITER //
CREATE PROCEDURE mascotas_db.InsertarMascota(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad FLOAT(12,10),
    IN p_peso FLOAT(12,10),
    IN p_id_propietario INT,
    IN p_sexo ENUM('F','M')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_db.mascotas VALUES
    (p_id,p_nombre,p_especie,p_raza,p_edad,p_peso,p_id_propietario,p_sexo);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarMascota(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad FLOAT(12,10),
    IN p_peso FLOAT(12,10),
    IN p_id_propietario INT,
    IN p_sexo ENUM('F','M')
) 
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_db.mascotas
    SET nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso,
        id_propietario = p_id_propietario,
        sexo = p_sexo
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

    DELETE FROM mascotas_db.mascotas
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

CREATE PROCEDURE mascotas_db.BuscarMascotaNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    SELECT 
        m.nombre,
        m.raza,
        m.especie, 
        m.peso,
        m.edad,
        m.sexo,
        u.nombre AS nombre_propietario
    FROM
        mascotas_db.mascotas m
    INNER JOIN 
        mascotas_db.propietarios p ON m.id_propietario = p.id_usuario
    INNER JOIN
        mascotas_db.usuarios u ON p.id_usuario = u.id_usuario
    WHERE
        m.nombre LIKE p_nombre;
END //

CREATE PROCEDURE mascotas_db.BuscarMascotas()
BEGIN
    SELECT 
        m.nombre,
        m.raza,
        m.especie, 
        m.peso,
        m.edad,
        m.sexo,
        u.nombre AS nombre_propietario
    FROM
        mascotas_db.mascotas m
    INNER JOIN 
        mascotas_db.propietarios p ON m.id_propietario = p.id_usuario
    INNER JOIN
        mascotas_db.usuarios u ON p.id_usuario = u.id_usuario;
END //
