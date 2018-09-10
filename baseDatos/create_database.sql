
/* EXEC [CRIMSONKING\CRIMSONSQL].tempdb.dbo.sp_executesql N'CREATE DATABASE COURIERTEC_SJ;'; */

CREATE DATABASE COURIERTEC_HEREDIA
USE COURIERTEC_HEREDIA

CREATE TABLE CLIENT_TYPE (
	ct_id INT IDENTITY(1,1) PRIMARY KEY,
	ct_name VARCHAR(20) NOT NULL
);

CREATE TABLE PROVINCE (
	p_id INT IDENTITY(1,1) PRIMARY KEY,
	p_name VARCHAR(30) NOT NULL
);

CREATE TABLE CLIENT (
	c_account INT IDENTITY(1,1) NOT NULL UNIQUE,
	c_id VARCHAR(30) PRIMARY KEY,
	c_name VARCHAR(30) NOT NULL,
	c_lname VARCHAR(50) NOT NULL,
	c_telephone VARCHAR(30) NOT NULL,
	c_username VARCHAR(20) NOT NULL UNIQUE,
	c_password VARCHAR(16) NOT NULL,
	c_type INT FOREIGN KEY REFERENCES CLIENT_TYPE(ct_id),
	c_province INT FOREIGN KEY REFERENCES PROVINCE(p_id)
);

CREATE TABLE CATEGORY (
	ca_id INT IDENTITY(1,1) PRIMARY KEY,
	ca_name VARCHAR(30) NOT NULL
);

CREATE TABLE PACKAGE_TYPE (
	pt_id INT IDENTITY(1,1) PRIMARY KEY,
	pt_name VARCHAR(50) NOT NULL,
	pt_price_kg INT NOT NULL,
	pt_category INT FOREIGN KEY REFERENCES CATEGORY(ca_id)
);

CREATE TABLE PACKAGE (
	p_id INT IDENTITY(1,1) PRIMARY KEY,
	p_reception_date DATE NOT NULL,
	p_value INT NOT NULL,
	p_weight INT NOT NULL,
	p_type INT FOREIGN KEY REFERENCES PACKAGE_TYPE(pt_id)
);

CREATE TABLE UBICATION (
	u_id INT IDENTITY(1,1) PRIMARY KEY,
	u_place VARCHAR(50) NOT NULL,
	u_address VARCHAR(100) NOT NULL
);

CREATE TABLE JOB (
	j_id INT IDENTITY(1,1) PRIMARY KEY,
	j_name VARCHAR(50) NOT NULL
);

CREATE TABLE WORKER (
	w_id VARCHAR(30) PRIMARY KEY,
	w_name VARCHAR(30) NOT NULL,
	w_lname VARCHAR(50) NOT NULL,
	w_telephone VARCHAR(30) NOT NULL,
	w_username VARCHAR(20) NOT NULL UNIQUE,
	w_password VARCHAR(16) NOT NULL
);

CREATE TABLE BRANCH_TYPE (
	bt_id INT IDENTITY(1,1) PRIMARY KEY,
	bt_name VARCHAR(30) NOT NULL
);

CREATE TABLE BRANCH (
	b_id INT IDENTITY(1,1) PRIMARY KEY,
	b_telephone VARCHAR(30) NOT NULL,
	b_schedule VARCHAR(30) NOT NULL,
	b_email VARCHAR(100) NOT NULL,
	b_type INT FOREIGN KEY REFERENCES BRANCH_TYPE(bt_id),
	b_ubication INT FOREIGN KEY REFERENCES UBICATION(u_id)
);

CREATE TABLE WORKS_ON (
	wo_branch INT FOREIGN KEY REFERENCES BRANCH(b_id),
	wo_worker VARCHAR(30) FOREIGN KEY REFERENCES WORKER(w_id),
	wo_job INT FOREIGN KEY REFERENCES JOB(j_id)
);

CREATE TABLE PACKAGE_BRANCH (
	pb_id INT IDENTITY(1,1) PRIMARY KEY,
	pb_total INT,
	pb_delivery_date DATE,
	pb_id_package INT FOREIGN KEY REFERENCES PACKAGE(p_id),
	pb_id_client VARCHAR(30) FOREIGN KEY REFERENCES CLIENT(c_id),
	pb_id_branch INT FOREIGN KEY REFERENCES BRANCH(b_id)
);

INSERT INTO PROVINCE VALUES
	('San José'),
	('Alajuela'), 
	('Cartago'), 
	('Heredia'),
	('Guanacaste'),
	('Puntarenas'),
	('Limón')

INSERT INTO CLIENT_TYPE VALUES
	('Platino'),
	('Oro'),
	('Bronce')

INSERT INTO CLIENT VALUES
	('207440546', 'Ernesto', 'Ulate Ramírez', '88649896', 'eulate', 'eulate123', 1, 2),
	('304960870', 'Fabián', 'Astorga Cerdas', '84333333', 'fabastorga', 'fabastorga123', 3, 3),
	('102540254', 'Walter', 'Blanco Harris', '88888888', 'wblanco', 'wblanco123', 3, 1),
	('102230469', 'Wendi', 'Salazar Pereira', '86665555', 'wsalazar', 'wendi123', 3, 5),
	('700540556', 'Heyreel', 'Davis Smith', '62151254', 'hdavis', 'hdavis123',  3, 7),
	('408550653', 'Jecsynior', 'Aguilar Rojas', '45511254', 'jaguilar', 'jaguilar123', 1, 4)

INSERT INTO CATEGORY VALUES
	('Regular'), ('Especial')

INSERT INTO PACKAGE_TYPE VALUES
	('Electrónicos', 2000, 1),
	('Ropa', 455, 1),
	('Juguetes', 800, 1),
	('Elementos para el hogar', 600, 1),
	('Comida', 5000, 2),
	('Baterías', 7450, 2),
	('Químicos', 11000, 2),
	('Herramientas', 6700, 2)

INSERT INTO PACKAGE VALUES
	('2018-01-09', 12300, 2, 8),
	('2018-06-10', 5545, 1, 5),
	('2018-03-21', 4500, 5, 4),
	('2018-02-28', 12000, 1, 2),
	('2018-05-12', 3600, 4, 1),
	('2018-03-25', 7800, 6, 7),
	('2018-07-10', 45000, 5, 4),
	('2018-01-04', 25000, 2, 3),
	('2018-04-26', 24025, 10, 5),
	('2018-09-07', 12456, 4, 3),
	('2018-06-12', 12014, 4, 8),
	('2018-04-14', 7895, 3, 4),
	('2018-05-01', 4520, 5, 1),
	('2018-02-28', 1234, 1, 2),
	('2018-06-18', 12400, 5, 4)

INSERT INTO UBICATION VALUES
	('Heredia', '100m Norte de los Tribunales de Justicia'),
	('San José', 'Diagonal al Auto Mercado de Plaza Víquez'),
	('Cartago', 'A la vuelta del Sanatorio Durán')

INSERT INTO JOB VALUES
	('Gerente'),
	('Administrador'),
	('Empleado')

INSERT INTO WORKER VALUES
	('102540254', 'Pedro', 'Uribe Matamoros', '84568752', 'puribe', 'puribe123'),
	('403250892', 'Jorge', 'Pérez Suárez', '45662154', 'jperez', 'jperez123'),
	('405890226', 'Violeta', 'Venegas Ramírez', '30210212', 'vvenegas', 'vvenegas123'),
	('302560256', 'Heidi', 'Prendas Johnson', '87789541', 'hprendas', 'hprendas123'),
	('820201235', 'Tumiko', 'Meyama Soto', '78952145', 'tmeyama', 'tmeyama123'),
	('122021254', 'Claudio', 'Sandí Huertas', '65452154', 'csandi', 'csandi123'),
	('402540255', 'Widman', 'Meneses Sequeira', '12542154', 'wmeneses', 'wmeneses'),
	('203360569', 'Espaider', 'Mora Villarán', '78995456', 'emora', 'emora')

INSERT INTO BRANCH_TYPE VALUES
	('Central'),
	('Secundaria')

INSERT INTO BRANCH VALUES
	('22909595', '9:00-18:00', 'couriertec_heredia@courierTEC.cr', 1, 1 ),
	('22919595', '7:30-16:45', 'couriertec_sanjose@courierTEC.cr', 2, 2 ),
	('25509595', '10:00-20:00', 'couriertec_cartago@courierTEC.cr', 2, 3 )

INSERT INTO WORKS_ON VALUES
	(1 , '102540254', 1),
	(1 , '403250892', 2),
	(1 , '405890226', 3),
	(2 , '302560256', 2),
	(2 , '820201235', 3),
	(3 , '122021254', 2),
	(3 , '402540255', 3),
	(3 , '203360569', 3)




select * from PROVINCE
select * from CLIENT_TYPE
select * from CLIENT
select * from CATEGORY
select * from PACKAGE_TYPE
select * from PACKAGE
select * from UBICATION
select * from JOB
select * from WORKER
select * from BRANCH_TYPE
select * from BRANCH
select * from WORKS_ON
select * from PACKAGE_BRANCH

select *
from UBICATION
where u_place='San José'

select *
from WORKS_ON
inner join UBICATION 
on UBICATION.u_id=WORKS_ON.wo_branch