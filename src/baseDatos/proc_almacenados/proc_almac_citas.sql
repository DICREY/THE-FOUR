-- Active: 1723829021103@@127.0.0.1@3306@mascotas_db
CREATE PROCEDURE mascotas_db.InsertarCita(
    IN p_codigo INT UNSIGNED,
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_servicio INT,
    IN p_veterinario INT,
    IN p_mascota INT,
    IN p_estado ENUM("Pendiente","En espera","Cancelada","Rechazada","Realizada")
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    INSERT INTO mascotas_db.citas
    VALUES(
        p_codigo,
        p_fecha,
        p_hora,
        p_servicio,
        p_veterinario,
        p_mascota,
        p_estado);

    COMMIT;
    SET autocommit = 1;
END //


CREATE PROCEDURE mascotas_db.BuscarCitaPorFecha(
    IN p_fecha DATE
)
BEGIN
    SELECT * FROM mascotas_db.citas
    WHERE fecha LIKE p_fecha;
END //


CREATE PROCEDURE mascotas_db.BuscarCitaPorMascota(
    IN p_mascota INT
)
BEGIN
    SELECT * FROM mascotas_db.citas
    WHERE mascota LIKE p_mascota;
END //

CREATE PROCEDURE mascotas_db.BuscarCitas()
BEGIN 
    SELECT * FROM mascotas_db.citas;
END //

CREATE PROCEDURE mascotas_db.EliminarCitaPorCodigo(
    IN p_codigo INT
)
BEGIN 
    DELETE  FROM mascotas_db.citas
    WHERE id = p_codigo;
END //
