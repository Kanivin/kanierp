// Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

if (!window.kanierp) window.kanierp = {};

kanierp.subscribe_to_newsletter = function (opts, btn) {
	return frappe.call({
		type: "POST",
		method: "frappe.email.doctype.newsletter.newsletter.subscribe",
		btn: btn,
		args: { email: opts.email },
		callback: opts.callback,
	});
};
