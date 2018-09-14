
from tools import *
from database_items import *
from sql_connection import *

def get_client_by_username( p_username ):
    client = 0
    query_client = "SELECT * FROM CLIENT WHERE c_username='"+p_username+"'"
    database_info_client = new_query( query_client )
    content_client = database_info_client.fetchall()
    print content_client
    if( len_database_info( content_client ) == 1 ):
        client = parse_client(  content_client[0][0],
                                content_client[0][1],
                                content_client[0][2],
                                content_client[0][3],
                                content_client[0][4],
                                content_client[0][5],
                                content_client[0][6],
                                content_client[0][7],
                                content_client[0][8] )
    return client

def get_worker_by_username( p_username ):
    worker = 0
    query_worker = "SELECT * FROM WORKER WHERE w_username='"+p_username+"'"
    database_info_worker = new_query( query_worker )
    content_worker = database_info_worker.fetchall()
    if( len_database_info( content_worker ) == 1 ):
        worker = parse_worker(  content_worker[0][0],
                                content_worker[0][1],
                                content_worker[0][2],
                                content_worker[0][3],
                                content_worker[0][4],
                                content_worker[0][5] )
    return worker

def get_worker_job_by_id( w_id ):
    job = 0
    query_worker_job = (    "SELECT j.j_name FROM JOB as j"
                            "INNER JOIN WORKS_ON as wo"
                            "ON j.j_id=wo.wo_job"
                            "WHERE wo.wo_worker='"+str(w_id)+"'")
    database_info = new_query( query_worker_job )
    content = database_info.fetchall()
    if( len_database_info( content ) == 1 ):
        job = content[0][0]
    return job