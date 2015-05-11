
	      // Load the Visualization API and the piechart package.
	      google.load('visualization', '1.0', {'packages':['corechart']});

	      // Set a callback to run when the Google Visualization API is loaded.
	      google.setOnLoadCallback(drawChart);

	      // Callback that creates and populates a data table,
	      // instantiates the pie chart, passes in the data and
	      // draws it.
	      function drawChart() {

	        // Create the data table.
	        var data = new google.visualization.DataTable();
	        data.addColumn('string', 'Topping');
	        data.addColumn('number', 'Slices');
	        data.addRows([
	          ['Travel',1.2 ],  //{{userInfo.TravelWeight}}
	          ['Music', 1.1], //{{userInfo.MusicWeight}}
				['Politic', 0.8], // {{userInfo.PoliticWeight}}
	          ['Entertainment', 0.5],  //{{userInfo.EntertainmentWeight}}
	          ['Technology', 1.4 ] //{{userInfo.TechnologyWeight}}
	        ]);
	        // Set chart options
	        var options = {'title':'What are the general intersts',
	                       'width':500,
	                       'height':400};
	        // Instantiate and draw our chart, passing in some options.
	        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
	        chart.draw(data, options);
	      }
