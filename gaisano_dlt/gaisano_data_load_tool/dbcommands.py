import frappe, pymysql, clickhouse_connect

def connect_to_mysql(pipeline_name, hostname,username,dbname,src_port):
    pipeline_doc = frappe.get_doc("Data Pipeline", pipeline_name)
    password = pipeline_doc.get_password('source_password')
    test_conn = pymysql.connect(
		host = hostname,
		user = username, 
		passwd= password,
		database = dbname,
		port = int(src_port),
		cursorclass=pymysql.cursors.DictCursor
	)
    return test_conn


def connect_to_clickhouse(pipeline_name, hostname,username,dbname,src_port):
    pipeline_doc = frappe.get_doc("Data Pipeline", pipeline_name)
    password = pipeline_doc.get_password('source_password')
    test_conn = clickhouse_connect.get_client(
                host=hostname,
                port=src_port,
                username=username,
                password=password,
                database=dbname)
    return test_conn