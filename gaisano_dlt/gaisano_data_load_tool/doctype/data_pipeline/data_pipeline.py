# Copyright (c) 2024, littlehera and contributors
# For license information, please see license.txt

import frappe
from gaisano_dlt.gaisano_data_load_tool.dbcommands import connect_to_clickhouse, connect_to_mysql
from frappe.model.document import Document


class DataPipeline(Document):
	pass

@frappe.whitelist()
def test_source_conn(pipeline_name, hostname,username,dbname,src_port):
	print("Test source connection")
	
	test_conn = connect_to_mysql(
		pipeline_name=pipeline_name,
		hostname=hostname,
		username=username,
		dbname=dbname,
		src_port=src_port)
	try:
		with test_conn.cursor() as cursor:
			# Example query
			sql = "SELECT * FROM `tabItem` LIMIT 10"
			cursor.execute(sql)
			
			# Fetch all rows from the last executed query
			result = cursor.fetchall()
			print(result)
	finally:
		frappe.msgprint("Source Connection Successful!")
		test_conn.close()  # Make sure to close the connection

@frappe.whitelist()
def test_destination_conn(pipeline_name, hostname,username,dbname,src_port):
	print("Test destination connection")
	try:
		# Create a ClickHouse client instance
		client = connect_to_clickhouse(
			pipeline_name=pipeline_name,
			hostname=hostname,
			src_port=src_port,
			username=username,
			dbname=dbname)
		query = "show tables"	
		# Execute the query
		result = client.query(query)	
		# Fetch the result
		rows = result.result_rows	
		# Print the result
		for row in rows:
			print(row)
	except Exception as e:
		print(f"An error occurred: {e}")
	else:
		frappe.msgprint("Destination Connection Successful!")


@frappe.whitelist()
def get_tables_from_source():
	print("HATDOG")