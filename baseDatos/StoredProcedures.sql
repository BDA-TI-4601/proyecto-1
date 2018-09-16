/* Monto recaudado en una sucursal */
CREATE PROCEDURE branchTotalAmount @branch VARCHAR(30)
AS
BEGIN
SELECT SUM(pb_total) AS "Dinero recaudado"
FROM PACKAGE_BRANCH
INNER JOIN BRANCH ON PACKAGE_BRANCH.pb_id_branch = BRANCH.b_id
INNER JOIN UBICATION ON BRANCH.b_ubication = UBICATION.u_id
WHERE pb_delivery_date IS NOT NULL AND u_place=@Branch
END

EXEC branchTotalAmount "Heredia"

/* Monto recaudado por sucursal para período específico */
CREATE PROCEDURE branchAmount @branch VARCHAR(30), @initialDate DATE, @finalDate DATE 
AS
BEGIN
SELECT SUM(pb_total) AS "Monto Total"
FROM PACKAGE_BRANCH
INNER JOIN BRANCH ON PACKAGE_BRANCH.pb_id_branch = BRANCH.b_id
INNER JOIN UBICATION ON BRANCH.b_ubication = UBICATION.u_id
WHERE pb_delivery_date IS NOT NULL AND pb_delivery_date>@initialDate AND pb_delivery_date<@finalDate AND u_place=@branch
END

EXEC branchAmount "Heredia", '2017-02-10', '2019-02-10'

/* Cantidad de paquetes según cliente en un período */ 
CREATE PROCEDURE packagesPerClient @initialDate DATE, @finalDate DATE
AS
BEGIN
SELECT c_id as ID, c_name as Nombre, c_lname as Apellido, pb_id as Orden, p_reception_date as Fecha  
FROM CLIENT 
INNER JOIN PACKAGE_BRANCH ON CLIENT.c_id = PACKAGE_BRANCH.pb_id_client
INNER JOIN PACKAGE ON PACKAGE_BRANCH.pb_id_package = PACKAGE.p_id
WHERE p_reception_date<@finalDate AND p_reception_date>@initialDate
ORDER BY c_id
END

EXEC packagesPerClient '2017-02-10', '2019-02-10'

/* Monto promedio pagado por cliente en un período*/
CREATE PROCEDURE averageAmountPerClient @initialDate DATE, @finalDate DATE
AS
BEGIN
SELECT c_name AS Nombre, c_lname AS Apellido, AVG(pb_total) AS "Promedio"
FROM PACKAGE_BRANCH 
INNER JOIN CLIENT ON CLIENT.c_id = PACKAGE_BRANCH.pb_id_client
INNER JOIN PACKAGE ON PACKAGE_BRANCH.pb_id_package = PACKAGE.p_id
WHERE p_reception_date<@finalDate AND p_reception_date>@initialDate
GROUP BY c_name, c_lname
END

EXEC averageAmountPerClient '2017-02-10', '2019-02-10'

/* Monto total para un tipo de paquete */
CREATE PROCEDURE packageTypeAmount @type INT, @initialDate DATE, @finalDate DATE
AS
BEGIN
SELECT p_type AS "Tipo paquete", SUM(p_value) AS "Total de montos"
FROM PACKAGE
WHERE p_reception_date>@initialDate AND p_reception_date<@finalDate AND p_type=@type
GROUP BY p_type
END

EXEC packageTypeAmount 3, '2017-02-10', '2019-02-10'

/* Tres mejores clientes (monto mayor en paquetes traídos) en un período*/
CREATE PROCEDURE bestClients @initialDate DATE, @finalDate DATE
AS
BEGIN
SELECT TOP 3 sum(pb_total) AS "Monto Total", c_name AS Nombre, c_lname AS Apellido
FROM PACKAGE_BRANCH
INNER JOIN CLIENT ON PACKAGE_BRANCH.pb_id_client = CLIENT.c_id
INNER JOIN PACKAGE ON PACKAGE_BRANCH.pb_id_package = PACKAGE.p_id
WHERE p_reception_date<@finalDate and p_reception_date>@initialDate
GROUP BY c_name, c_lname
ORDER BY "Monto Total" DESC
END

EXEC bestClients '2017-02-10', '2019-02-10'