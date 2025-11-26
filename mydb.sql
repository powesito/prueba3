-- ========================
--        Schema
-- ========================

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS veterinaria;
USE veterinaria;

-- ========================
-- Tabla usuario
-- ========================
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL
);

-- Datos iniciales
INSERT INTO usuario(username, password) VALUES
('admin', SHA2('admin123',256)),
('usuario1', SHA2('pass123',256));

-- ========================
-- Tabla cuidador
-- ========================
CREATE TABLE IF NOT EXISTS cuidador (
    rut_cuidador VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(80),
    telefono VARCHAR(20),
    email VARCHAR(80)
);

-- Datos iniciales
INSERT INTO cuidador(rut_cuidador, nombre, direccion, telefono, email) VALUES
('111-1','Juan Pérez','Calle Falsa 123','+56912345678','juan@gmail.com'),
('111-2','Ana López','Av. Siempre Viva 456','+56987654321','ana@gmail.com');

-- ========================
-- Tabla mascota (singular, coincide con tus clases)
-- ========================
CREATE TABLE IF NOT EXISTS mascota (
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    especie VARCHAR(50),
    raza VARCHAR(50),
    edad INT,
    peso FLOAT,
    sexo ENUM('M','F','Desconocido') DEFAULT 'Desconocido',
    rut_cuidador VARCHAR(12),
    FOREIGN KEY (rut_cuidador) REFERENCES cuidador(rut_cuidador)
);

-- Datos iniciales
INSERT INTO mascota(nombre, especie, raza, edad, peso, sexo, rut_cuidador) VALUES
('Firulais','Perro','Labrador',5,20.5,'M','111-1'),
('Michi','Gato','Siames',3,5.2,'F','111-2');

-- ========================
-- Tabla veterinario
-- ========================
CREATE TABLE IF NOT EXISTS veterinario (
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(50),
    especialidad VARCHAR(80),
    anios_experiencia INT,
    contacto VARCHAR(20)
);

-- Datos iniciales
INSERT INTO veterinario(rut, nombre, especialidad, anios_experiencia, contacto) VALUES
('222-1','Dr. Martín','Cirugía',10,'+56911223344'),
('222-2','Dra. Carla','Vacunación',5,'+56922334455');

-- ========================
-- Tabla procedimiento
-- ========================
CREATE TABLE IF NOT EXISTS procedimiento (
    id_procedimiento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    fecha_creacion DATE,
    tipo_procedimiento VARCHAR(50),
    veterinario_responsable VARCHAR(12),
    indicaciones VARCHAR(200),
    costo INT,
    FOREIGN KEY (veterinario_responsable) REFERENCES veterinario(rut)
);

-- Datos iniciales
INSERT INTO procedimiento(nombre, fecha_creacion, tipo_procedimiento, veterinario_responsable, indicaciones, costo) VALUES
('Vacuna antirrábica','2025-11-01','Vacunación','222-2','Aplicar 1 dosis',20000),
('Desparasitación interna','2025-11-05','Desparasitación','222-1','Administrar según peso',15000);

-- ========================
-- Tabla ficha_clinica
-- ========================
CREATE TABLE IF NOT EXISTS ficha_clinica (
    id_ficha INT AUTO_INCREMENT PRIMARY KEY,
    id_mascota INT,
    rut_cuidador VARCHAR(12),
    rut_veterinario VARCHAR(12),
    id_procedimiento INT,
    fecha DATE,
    notas TEXT,
    FOREIGN KEY(id_mascota) REFERENCES mascota(id_mascota),
    FOREIGN KEY(rut_cuidador) REFERENCES cuidador(rut_cuidador),
    FOREIGN KEY(rut_veterinario) REFERENCES veterinario(rut),
    FOREIGN KEY(id_procedimiento) REFERENCES procedimiento(id_procedimiento)
);

-- Datos iniciales
INSERT INTO ficha_clinica(id_mascota, rut_cuidador, rut_veterinario, id_procedimiento, fecha, notas) VALUES
(1,'111-1','222-2',1,'2025-11-02','Mascota sin antecedentes graves'),
(2,'111-2','222-1',2,'2025-11-06','Se recomienda repetir desparasitación en 3 meses');
