
DELIMITER //
CREATE PROCEDURE mascotas_bd.InsertarMascota(
    IN p_codigo INT UNSIGNED,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad INT UNSIGNED, 
    IN p_peso FLOAT,
    IN p_id_propietario INT UNSIGNED
)
BEGIN
    INSERT INTO mascotas_bd.mascotas VALUES
    (p_codigo,p_nombre,p_especie,p_raza,p_edad,p_peso,p_id_propietario);
END //
CREATE PROCEDURE mascotas_bd.EliminarMascota(
    IN p_codigo INT UNSIGNED
) 
BEGIN
    DELETE FROM mascotas_bd.mascotas WHERE codigo = p_codigo;
END //
/* CALL EliminarPropietario(2) */
DELIMITER ;