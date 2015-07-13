$(function () {
    $('#dashCartConversion').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Carrinhos vs. Compras'
        },
        subtitle: {
            text: 'Conversao de compras nos ultimos 30 dias'
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            title: {
                text: 'Data'
            }
        },
        yAxis: {
            title: {
                text: 'Quantidade'
            },
            min: 0
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
            name: 'carrinhos',
            data: $cartData
        }, {
            name: 'compras',
            data: $orderData
        }]
    });


    //pageViews
    $('#dashPageViews').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Paginas visitadas'
        },
        subtitle: {
            text: 'quantidade de paginas visitadas nos ultimos 30 dias'
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            title: {
                text: 'Data'
            }
        },
        yAxis: {
            title: {
                text: 'Quantidade'
            },
            min: 0
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
            name: 'page views',
            data: $visitData
        }]
    });
});
