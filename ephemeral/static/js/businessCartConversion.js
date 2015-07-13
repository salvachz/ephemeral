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
            categories: $dashCartConversion
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
            name: 'carrinhos',
            data: $cartData
        }, {
            name: 'compras',
            data: $orderData
        }]
    });

});