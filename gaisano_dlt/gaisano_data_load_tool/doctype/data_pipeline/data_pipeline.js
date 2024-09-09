// Copyright (c) 2024, littlehera and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Data Pipeline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Data Pipeline", "source_test_conn", function(frm){
    var hostname = frm.doc.source_host;
    var username = frm.doc.source_username;
    var password = frm.doc.source_password;
    var dbname = frm.doc.source_database;
    var src_port = frm.doc.source_port;

    if (frm.doc.__islocal==1)
        frappe.throw("Please Save the Document.")
    else
    frappe.call({
        method: 'gaisano_dlt.gaisano_data_load_tool.doctype.data_pipeline.data_pipeline.test_source_conn',
        args: {
            pipeline_name: frm.doc.name,
            hostname: hostname,
            username: username,
            //password: password,
            dbname: dbname,
            src_port: src_port
        },
        callback: function(response) {
            if (response.message) {
                // Do something with the server response
            }
        },
        error: function(error) {
            // Handle errors if any
            frappe.msgprint(__('An error occurred: ') + error.message);
        }
    });

});

frappe.ui.form.on("Data Pipeline", "destination_test_conn", function(frm){
    var hostname = frm.doc.destination_host;
    var username = frm.doc.destination_username;
    var dbname = frm.doc.destination_database;
    var src_port = frm.doc.destination_port;

    if (frm.doc.__islocal==1)
        frappe.throw("Please Save the Document.")
    else
    frappe.call({
        method: 'gaisano_dlt.gaisano_data_load_tool.doctype.data_pipeline.data_pipeline.test_destination_conn',
        args: {
            pipeline_name: frm.doc.name,
            hostname: hostname,
            username: username,
            dbname: dbname,
            src_port: src_port
        },
        callback: function(response) {
            if (response.message) {
                // Do something with the server response
            }
        },
        error: function(error) {
            // Handle errors if any
            frappe.msgprint(__('An error occurred: ') + error.message);
        }
    });

});