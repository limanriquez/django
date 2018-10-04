(function(){
	'use strict';
	angular
		.module('src.monitoreo',[
			'dx',
			'ui.bootstrap',
			'src.monitoreo.controllers',
			'agricola.config',
			])
	angular
		.module('src.monitoreo.controllers',[]);
	angular
		.module('src.monitoreo')
		.run(run);
	run.$inject=['$http']
	function run($http){
		$http.defaults.xsrfHeaderName='X-CSRFToken';
		$http.defaults.xsrfCookieName='csrftoken';
	}
})();