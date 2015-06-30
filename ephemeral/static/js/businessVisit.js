$(function () {
    $('#visitGraph').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Visitas'
        },
        subtitle: {
            text: 'visitas nos ultimos 30 dias'
        },
        xAxis: {
            categories: $dashVisitDay
        },
        yAxis: {
            title: {
                text: 'Quantidade'
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: [{
            name: 'visitas',
            data: $visitData
        }]
    });

});