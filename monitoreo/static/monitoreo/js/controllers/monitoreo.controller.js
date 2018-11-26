(function(){
	'use  strict';
	angular
		.module('src.monitoreo.controllers')
		.controller('Monitoreo',MonitoreoController);
	MonitoreoController.$inject=['$http','$scope'];
	function MonitoreoController($http,$scope){
		var vm = this;
		$scope.valor=10;
		var types = ["spline", "stackedspline", "fullstackedspline"];
		var ArrayRegistroSensores=[];
		function get_registro_sensores(){
			ArrayRegistroSensores.length=0;
			$http.get('/get_registro_sensores/').then(//Se llama al servicio registrado con esta URL
				function(response){
					for(let i = 0; i < response.data.length; i++){//Se recorre la respuesta del servivio
						ArrayRegistroSensores.push(response.data[i]);//Se agrega al arreglo cada elemento de la respuesta				
						console.log(response.data[i]);
					}
					Morris.Line({
					    data: ArrayRegistroSensores,
					    element:'line-chart',
					    xkey: 'y',
					    ykeys: ['a', 'b'],
					    labels: ['Sensor 1', 'Sensor 2'],
					    fillOpacity: 0.6,
					    hideHover: 'auto',
					    behaveLikeLine: true,
					    resize: true,
					    pointFillColors:['#ffffff'],
					    pointStrokeColors: ['black'],
					    lineColors:['blue','red']
				  	});
				}, function(response){
					
				}
			);
		}
		
		var data = [
	      { y: '2014', a: 50, b: 90},
	      { y: '2015', a: 65,  b: 75},
	      { y: '2016', a: 50,  b: 50},
	      { y: '2017', a: 75,  b: 60},
	      { y: '2018', a: 80,  b: 65},
	      { y: '2019', a: 90,  b: 70},
	      { y: '2020', a: 100, b: 75},
	      { y: '2021', a: 115, b: 75},
	      { y: '2022', a: 120, b: 85},
	      { y: '2023', a: 145, b: 85},
	      { y: '2024', a: 160, b: 95}
	    ];

		var dataSource = [{
		    year: 1997,
		    smp: 263,
		    mmp: 226,
		    cnstl: 10,
		    cluster: 1
		}, {
		    year: 1999,
		    smp: 169,
		    mmp: 256,
		    cnstl: 66,
		    cluster: 7
		}, {
		    year: 2001,
		    smp: 57,
		    mmp: 257,
		    cnstl: 143,
		    cluster: 43
		}, {
		    year: 2003,
		    smp: 0,
		    mmp: 163,
		    cnstl: 127,
		    cluster: 210
		}, {
		    year: 2005,
		    smp: 0,
		    mmp: 103,
		    cnstl: 36,
		    cluster: 361
		}, {
		    year: 2007,
		    smp: 0,
		    mmp: 91,
		    cnstl: 3,
		    cluster: 406
		}];

		var types = ["spline", "stackedspline", "fullstackedspline"];

		vm.buttons = {
			btnOptions:{
				icon: 'fa fa-search',
				type: 'success',
				width: 240,
				text: 'Solicitud de aseguramiento',
				disabled: false,	
				onInitialized: function(e){
					// botonBuscarSolicitudInstance = e.component;
				},
				onClick: function(){
					get_registro_sensores();
				}
			},
		}
	
		chartOptions = {
	        palette: "violet",
	        dataSource: dataSource,
	        commonSeriesSettings: {
	            argumentField: "year"
	        },
	        bindingOptions: { 
	            "commonSeriesSettings.type": "currentType"
	        },
	        commonAxisSettings: {
	            grid: {
	                visible: true
	            }
	        },
	        margin: {
	            bottom: 20
	        },
	        series: [
	            { valueField: "smp", name: "SMP" },
	            { valueField: "mmp", name: "MMP" },
	            { valueField: "cnstl", name: "Cnstl" },
	            { valueField: "cluster", name: "Cluster" }
	        ],
	        tooltip:{
	            enabled: true
	        },
	        legend: {
	            verticalAlignment: "top",
	            horizontalAlignment: "right"
	        },
	        "export": {
	            enabled: true
	        },
	        argumentAxis: {
	            label:{
	                format: {
	                    type: "decimal"
	                }
	            },
	            allowDecimals: false,
	            axisDivisionFactor: 60
	        },
	        title: "Architecture Share Over Time (Count)"
	    };
		

    
    vm.typesOptions = {
        dataSource: types,
        bindingOptions: { 
            value: "currentType"
        }
    };

		
	}
})();