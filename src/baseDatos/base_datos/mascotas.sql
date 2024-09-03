-- Active: 1721867436095@@localhost@3306
CREATE DATABASE mascotas_db;
CREATE TABLE mascotas_db.usuarios(
    id_usuario INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(100) NOT NULL,
    es_propietario BOOLEAN DEFAULT 1,
    es_veterinario BOOLEAN DEFAULT 0,
    es_administrador BOOLEAN DEFAULT 0,
    email VARCHAR(100) NOT NULL,
    contrasenna VARCHAR(100) NOT NULL
);
CREATE TABLE mascotas_db.veterinarios(
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    FOREIGN KEY(id_usuario)  REFERENCES usuarios(id_usuario) ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE mascotas_db.propietarios(
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    barrio VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE mascotas_db.administradores(
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE mascotas_db.mascotas(
    id INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    especie VARCHAR(100) NOT NULL,
    raza VARCHAR(100) NOT NULL,
    edad FLOAT(12,10) UNSIGNED NOT NULL,
    peso FLOAT(12,10) UNSIGNED NOT NULL,
    id_propietario INT UNSIGNED NOT NULL,
    sexo ENUM('F','M')NOT NULL,
    FOREIGN KEY (id_propietario) REFERENCES propietarios(id_usuario) ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE mascotas_db.historiales_medicos(
    id INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    descripcion TEXT NOT NULL,
    tratamiento  TEXT NOT NULL,
    id_veterinario INT UNSIGNED NOT NULL,
    id_mascota INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id_usuario),
    Foreign Key (id_mascota) REFERENCES mascotas(id) ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE mascotas_db.productos(
    id INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(20,5) NOT NULL,
    stock SMALLINT NOT NULL
);
CREATE TABLE mascotas_db.servicios(
    id INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(20,5) NOT NULL
);
CREATE TABLE mascotas_db.citas(
    id INT UNSIGNED UNIQUE NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    servicio INT UNSIGNED NOT NULL,
    veterinario INT UNSIGNED NOT NULL,
    mascota INT UNSIGNED NOT NULL,
    estado ENUM("Pendiente","En espera","Cancelada","Rechazada","Realizada") NOT NULL,
    PRIMARY KEY (id,mascota),
    FOREIGN KEY(servicio) REFERENCES servicios(id),
    FOREIGN KEY(veterinario) REFERENCES veterinarios(id_usuario) ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(mascota) REFERENCES mascotas(id)
);

