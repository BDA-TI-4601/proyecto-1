/* POPULATION SCRIPT */

INSERT INTO PROVINCE VALUES
	('San José', NEWID()),
	('Alajuela', NEWID()), 
	('Cartago', NEWID()), 
	('Heredia', NEWID()),
	('Guanacaste', NEWID()),
	('Puntarenas', NEWID()),
	('Limón', NEWID())

INSERT INTO CLIENT_TYPE VALUES
	('Platino', NEWID()),
	('Oro', NEWID()),
	('Bronce', NEWID())

INSERT INTO CLIENT VALUES
	('207440546', 'Ernesto', 'Ulate Ramírez', '88649896', 'eulate', 'eulate123', 1, 2, NEWID()),
	('304960870', 'Fabián', 'Astorga Cerdas', '84333333', 'fabastorga', 'fabastorga123', 3, 3, NEWID()),
	('102540254', 'Walter', 'Blanco Harris', '88888888', 'wblanco', 'wblanco123', 3, 1, NEWID()),
	('102230469', 'Wendi', 'Salazar Pereira', '86665555', 'wsalazar', 'wendi123', 3, 5, NEWID()),
	('700540556', 'Heyreel', 'Davis Smith', '62151254', 'hdavis', 'hdavis123',  3, 7, NEWID()),
	('408550653', 'Jecsynior', 'Aguilar Rojas', '45511254', 'jaguilar', 'jaguilar123', 1, 4, NEWID())

INSERT INTO CATEGORY VALUES
	('Regular', NEWID()), ('Especial', NEWID())

INSERT INTO PACKAGE_TYPE VALUES
	('Electrónicos', 2000, 1, NEWID()),
	('Ropa', 455, 1, NEWID()),
	('Juguetes', 800, 1, NEWID()),
	('Elementos para el hogar', 600, 1, NEWID()),
	('Comida', 5000, 2, NEWID()),
	('Baterías', 7450, 2, NEWID()),
	('Químicos', 11000, 2, NEWID()),
	('Herramientas', 6700, 2, NEWID())

INSERT INTO PACKAGE VALUES
	('2018-01-09', 12300, 2, 8, NEWID()),
	('2018-06-10', 5545, 1, 5, NEWID()),
	('2018-03-21', 4500, 5, 4, NEWID()),
	('2018-02-28', 12000, 1, 2, NEWID()),
	('2018-05-12', 3600, 4, 1, NEWID()),
	('2018-03-25', 7800, 6, 7, NEWID()),
	('2018-07-10', 45000, 5, 4, NEWID()),
	('2018-01-04', 25000, 2, 3, NEWID()),
	('2018-04-26', 24025, 10, 5, NEWID()),
	('2018-09-07', 12456, 4, 3, NEWID()),
	('2018-06-12', 12014, 4, 8, NEWID()),
	('2018-04-14', 7895, 3, 4, NEWID()),
	('2018-05-01', 4520, 5, 1, NEWID()),
	('2018-02-28', 1234, 1, 2, NEWID()),
	('2018-06-18', 12400, 5, 4, NEWID())

INSERT INTO UBICATION VALUES
	('Heredia', '100m Norte de los Tribunales de Justicia', NEWID()),
	('San José', 'Diagonal al Auto Mercado de Plaza Víquez', NEWID()),
	('Cartago', 'A la vuelta del Sanatorio Durán', NEWID())

INSERT INTO JOB VALUES
	('Gerente', NEWID()),
	('Administrador', NEWID()),
	('Empleado', NEWID())

INSERT INTO WORKER VALUES
	('102540254', 'Pedro', 'Uribe Matamoros', '84568752', 'puribe', 'puribe123', NEWID()),
	('403250892', 'Jorge', 'Pérez Suárez', '45662154', 'jperez', 'jperez123', NEWID()),
	('405890226', 'Violeta', 'Venegas Ramírez', '30210212', 'vvenegas', 'vvenegas123', NEWID()),
	('302560256', 'Heidi', 'Prendas Johnson', '87789541', 'hprendas', 'hprendas123', NEWID()),
	('820201235', 'Tumiko', 'Meyama Soto', '78952145', 'tmeyama', 'tmeyama123', NEWID()),
	('122021254', 'Claudio', 'Sandí Huertas', '65452154', 'csandi', 'csandi123', NEWID()),
	('402540255', 'Widman', 'Meneses Sequeira', '12542154', 'wmeneses', 'wmeneses', NEWID()),
	('203360569', 'Espaider', 'Mora Villarán', '78995456', 'emora', 'emora', NEWID())

INSERT INTO BRANCH_TYPE VALUES
	('Central', NEWID()),
	('Secundaria', NEWID())

INSERT INTO BRANCH VALUES
	('22909595', '9:00-18:00', 'couriertec_heredia@courierTEC.cr', 1, 1, NEWID() ),
	('22919595', '7:30-16:45', 'couriertec_sanjose@courierTEC.cr', 2, 2, NEWID() ),
	('25509595', '10:00-20:00', 'couriertec_cartago@courierTEC.cr', 2, 3 , NEWID())

INSERT INTO WORKS_ON VALUES
	(1 , '102540254', 1, NEWID()),
	(1 , '403250892', 2, NEWID()),
	(1 , '405890226', 3, NEWID()),
	(2 , '302560256', 2, NEWID()),
	(2 , '820201235', 3, NEWID()),
	(3 , '122021254', 2, NEWID()),
	(3 , '402540255', 3, NEWID()),
	(3 , '203360569', 3, NEWID())

INSERT INTO PACKAGE_BRANCH VALUES
	(5000, NULL, 1, '102540254', 2, NEWID()),
	(2000, NULL, 2, '102540254', 1, NEWID()),
	(12000, '2018-01-09', 3, '304960870', 3, NEWID()),
	(14000, '2018-04-09', 4, '102230469', 2, NEWID()),
	(18000, NULL, 5, '102230469', 2, NEWID()),
	(190000, '2018-04-09', 6, '102230469', 2, NEWID()),
	(10000, '2018-04-09', 7, '700540556', 3, NEWID()),
	(12500, NULL, 8, '700540556', 3, NEWID()),
	(32000, '2018-04-09', 9, '408550653', 1, NEWID()),
	(900100, NULL, 10, '207440546', 1, NEWID()),
	(56090, NULL, 11, '207440546', 1, NEWID()),
	(24000, '2018-04-09', 12, '207440546', 1, NEWID()),
	(50000000, NULL, 13, '408550653', 1, NEWID()),
	(125000, NULL, 14, '304960870', 3, NEWID()),
	(78900, NULL, 15, '102540254', 2, NEWID())





