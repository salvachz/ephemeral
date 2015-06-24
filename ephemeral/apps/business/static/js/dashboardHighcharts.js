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
            categories: $dashPageViewsDays
        },
        yAxis: {
            title: {
                text: 'page views'
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
            name: 'page views',
            data: $dashPageViews
        }]
    });
});