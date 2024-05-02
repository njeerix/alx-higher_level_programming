$(document).ready(function() {
	$('#btn_translate').click(fetchTranslation);
	$('#language_code').keypress(function(event) {
		if (event.which === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation(0 {
		const languageCode = $('#language_code').val();
		$get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
			$('#hello').text(data.hello);
		});
	}
});
