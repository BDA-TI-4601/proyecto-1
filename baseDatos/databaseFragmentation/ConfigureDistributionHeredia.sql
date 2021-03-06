/****** Scripting replication configuration. Script Date: 23/09/2018 09:05:56 p.m. ******/
/****** Please Note: For security reasons, all password parameters were scripted with either NULL or an empty string. ******/

/****** Installing the server as a Distributor. Script Date: 23/09/2018 09:05:56 p.m. ******/
use master
exec sp_adddistributor @distributor = N'CAR-GRMHUASTO\FABSQL', @password = N''
GO
exec sp_adddistributiondb @database = N'distribution_heredia', @data_folder = N'C:\courierTEC', @log_folder = N'C:\courierTEC', @log_file_size = 2, @min_distretention = 0, @max_distretention = 72, @history_retention = 48, @deletebatchsize_xact = 5000, @deletebatchsize_cmd = 2000, @security_mode = 1
GO

use [distribution_heredia] 
if (not exists (select * from sysobjects where name = 'UIProperties' and type = 'U ')) 
	create table UIProperties(id int) 
if (exists (select * from ::fn_listextendedproperty('SnapshotFolder', 'user', 'dbo', 'table', 'UIProperties', null, null))) 
	EXEC sp_updateextendedproperty N'SnapshotFolder', N'C:\courierTEC', 'user', dbo, 'table', 'UIProperties' 
else 
	EXEC sp_addextendedproperty N'SnapshotFolder', N'C:\courierTEC', 'user', dbo, 'table', 'UIProperties'
GO

exec sp_adddistpublisher @publisher = N'CAR-GRMHUASTO\FABSQL', @distribution_db = N'distribution_heredia', @security_mode = 0, @login = N'sa', @password = N'', @working_directory = N'C:\courierTEC', @trusted = N'false', @thirdparty_flag = 0, @publisher_type = N'MSSQLSERVER'
GO
