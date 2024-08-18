-- Active: 1715350134884@@127.0.0.1@3306
CREATE PROCEDURE mascotas_db.InsertarHistorialMedico(
    IN p_id INT,
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_id_veterinario INT,
    IN p_id_mascota INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_db.historiales_medicos 
    VALUES(p_id,p_fecha,p_descripcion,p_tratamiento,p_id_veterinario,p_id_mascota);

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.ActualizarHistorialMedico(
    IN p_id INT,
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_id_veterinario INT,
    IN p_id_mascota INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    UPDATE mascotas_db.historiales_medicos
    SET fecha = p_fecha,
        descripcion = p_descripcion,
        tratamiento = p_tratamiento,
        id_veterinario = p_id_veterinario,
        id_mascota = p_id_mascota
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.EliminarHistorialMedico(
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

    DELETE FROM mascotas_db.historiales_medicos
    WHERE id = p_id;

    COMMIT;
    SET autocommit = 1;
END //

CREATE PROCEDURE mascotas_db.BuscarHistorialMedicoID(
    IN p_id INT
)
BEGIN
    SELECT 
        up.nombre AS Nombre_Propietario,
        u.nombre AS Nombre_Veterinario,
        m.nombre AS Nombre_Mascota,
        h.fecha AS Fecha_Tratamiento,
        h.descripcion AS Descripcion_Tratamiento,
        h.tratamiento AS Tipo_Tratamiento
    FROM 
        mascotas_db.historiales_medicos h
    INNER JOIN 
        mascotas_db.mascotas m ON m.id = h.id_mascota
    INNER JOIN 
        mascotas_db.usuarios u ON u.id_usuario = h.id_veterinario
    LEFT JOIN
        mascotas_db.propietarios p ON p.id_usuario = m.id_propietario
    INNER JOIN
        mascotas_db.usuarios up ON up.id_usuario = p.id_usuario
    WHERE 
        h.id = p_id;
END //

CREATE PROCEDURE mascotas_db.BuscarHistorialesMedicos()
BEGIN
    SELECT 
        up.nombre AS Nombre_Propietario,
        u.nombre AS Nombre_Veterinario,
        m.nombre AS Nombre_Mascota,
        h.fecha AS Fecha_Tratamiento,
        h.descripcion AS Descripcion_Tratamiento,
        h.tratamiento AS Tipo_Tratamiento
    FROM 
        mascotas_db.historiales_medicos h
    INNER JOIN 
        mascotas_db.mascotas m ON m.id = h.id_mascota
    INNER JOIN 
        mascotas_db.usuarios u ON u.id_usuario = h.id_veterinario
    LEFT JOIN
        mascotas_db.propietarios p ON p.id_usuario = m.id_propietario
    INNER JOIN
        mascotas_db.usuarios up ON up.id_usuario = p.id_usuario;
END //