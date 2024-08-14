CREATE DATABASE mascotas_db;
/* 2024-07-31 16:17:14 [37 ms] */ 
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
/* 2024-07-31 16:17:15 [44 ms] */ 
CREATE TABLE mascotas_db.veterinarios(
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    FOREIGN KEY(id_usuario)  REFERENCES usuarios(id_usuario)
);
/* 2024-07-31 16:17:17 [30 ms] */ 
CREATE TABLE mascotas_db.propietarios(
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    barrio VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
/* 2024-07-31 16:17:22 [29 ms] */ 
CREATE TABLE mascotas_db.historiales_medicos(
    codigo INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    tratamiento VARCHAR(255) NOT NULL,
    id_veterinario INT UNSIGNED NOT NULL,
    codigo_mascota INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id)
);
/* 2024-07-31 16:17:30 [31 ms] */ 
CREATE TABLE mascotas_db.mascotas(
    codigo INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100),
    especie VARCHAR(100),
    raza VARCHAR(100),
    edad INT UNSIGNED NOT NULL,
    peso FLOAT UNSIGNED NOT NULL,
    id_propietario INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_propietario) REFERENCES propietarios(id)
);
/* 2024-07-31 16:17:35 [45 ms] */ 
CREATE TABLE mascotas_db.administradores(,
    id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
/* 2024-07-31 16:17:40 [29 ms] */ 
CREATE TABLE mascotas_db.productos(
    codigo INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio FLOAT NOT NULL,
    id_administrador INT UNSIGNED NOT NULL,
    codigo_servicio INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_administrador) REFERENCES administradores(id)
);
/* 2024-07-31 16:17:44 [25 ms] */ 
CREATE TABLE mascotas_db.servicios(
    codigo INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio FLOAT NOT NULL,
    codigo_producto INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo)
);
/* 2024-07-31 16:17:49 [33 ms] */ 
CREATE TABLE mascotas_db.citas(
    codigo INT UNSIGNED UNIQUE PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    servicio INT UNSIGNED NOT NULL,
    veterinario INT UNSIGNED NOT NULL,
    mascota INT UNSIGNED NOT NULL,
    estado VARCHAR(100) NOT NULL,
    FOREIGN KEY(servicio) REFERENCES servicios(codigo),
    FOREIGN KEY(veterinario) REFERENCES veterinarios(id),
    FOREIGN KEY(mascota) REFERENCES mascotas(codigo)
);