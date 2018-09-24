
from tools import *
from database_items import *
from sql_connection import *

def get_packages_by_id_client( p_id_client, p_id_branch ):
    client_packages = []
    query_packages_client = (   "select A2.p_id, A2.p_reception_date, A2.pt_name, c.ca_name, A2.p_weight, A2.pb_delivery_date, A2.pb_total "
                                " from CATEGORY as c "
                                " inner join "
                                " ( select * "
	                            " from PACKAGE_TYPE as pt "
	                            " inner join ( select p.p_id, p.p_reception_date, p.p_weight, pb.pb_delivery_date, pb.pb_total, p.p_type, pb.pb_id_client "
		                        " from PACKAGE_BRANCH as pb "
		                        " inner join PACKAGE as p "
		                        " on pb.pb_id_package=p.p_id "
		                        " where pb.pb_id_branch="+str(p_id_branch)+" "
	                            " ) as A1 "
	                            " on pt.pt_id=A1.p_type "
                                " ) as A2 "
                                " on c.ca_id=A2.pt_category "
                                " where A2.pb_id_client='"+p_id_client+"'"
                            )
    database_info = new_query( query_packages_client )
    content_packages = database_info.fetchall()
    for single_pkg in content_packages: 
        client_packages += [parse_package_client(   single_pkg[0],
                                                    single_pkg[1],
                                                    single_pkg[2],
                                                    single_pkg[3],
                                                    single_pkg[4],
                                                    single_pkg[5],
                                                    single_pkg[6]   )]
    return str(client_packages)


def get_packages_by_branch( p_id_branch ):
    branch_packages = []
    query_packages = (   "select A3.pb_id_package, A3.pb_id_client, A3.c_name, A3.c_lname, A3.p_reception_date, A3.pb_delivery_date, A3.p_weight, A3.p_value, A3.pb_total, A3.pt_name, ca.ca_name "
                                "from CATEGORY as ca "
                                " inner join "
                                " ( "
                                    " select * "
                                    " from PACKAGE_TYPE as pt "
                                    " inner join "
                                    " ( "
                                        " select A1.pb_total, A1.pb_delivery_date, A1.pb_id_package, A1.pb_id_client, A1.c_name, A1.c_lname, p.p_type, p_value, p_weight, p.p_reception_date "
                                        " from PACKAGE as p "
                                        " inner join "
                                        " ( "
                                            " select pb.pb_total, pb.pb_delivery_date, pb.pb_id_package, pb.pb_id_client, c.c_name, c.c_lname, c.c_id "
                                            " from PACKAGE_BRANCH as pb "
                                            " inner join CLIENT as c "
                                            " on c.c_id=pb.pb_id_client "
                                            " where pb.pb_id_branch="+str(p_id_branch)+
                                        " ) as A1 "
                                    " on p.p_id=A1.pb_id_package "
                                    " ) as A2 "
                                " on A2.p_type=pt.pt_id "
                                " ) as A3 "
                                " on A3.pt_category=ca.ca_id "
                            )
    database_info = new_query( query_packages )
    content_packages = database_info.fetchall()
    for single_pkg in content_packages: 
        branch_packages += [parse_packages_branch(   single_pkg[0],
                                                    single_pkg[1],
                                                    single_pkg[2],
                                                    single_pkg[3],
                                                    single_pkg[4],
                                                    single_pkg[5],
                                                    single_pkg[6],
                                                    single_pkg[7],
                                                    single_pkg[8],
                                                    single_pkg[9],
                                                    single_pkg[10]   )]
    return str(branch_packages)