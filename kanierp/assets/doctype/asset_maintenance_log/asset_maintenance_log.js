// Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Asset Maintenance Log", {
	asset_maintenance: (frm) => {
		frm.set_query("task", function (doc) {
			return {
				query: "kanierp.assets.doctype.asset_maintenance_log.asset_maintenance_log.get_maintenance_tasks",
				filters: {
					asset_maintenance: doc.asset_maintenance,
				},
			};
		});
	},
});
