$(document).ready(function() {
	
	$('#When').datetimepicker({
		useSeconds: false,
		format: 'dd/MM/yyyy hh:mm',
	});
	
	$("input,select").addClass('form-control');
})