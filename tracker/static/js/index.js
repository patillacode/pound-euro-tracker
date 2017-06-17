
var config = {
    type: 'line',
    data: {
        labels: dates,
        datasets: [{
            label: from_currency + "/" + to_currency + " rate",
            backgroundColor: 'rgba(255, 105, 0, 0.6)',
            borderColor: 'rgba(255, 105, 0, 0.6)',
            data: values,
            fill: false,
        }]
    },
    options: {
        responsive: true,
        title:{
            display:true,
            text:from_currency + "/" + to_currency + " rate"
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: from_currency + " to " + to_currency + " rate"
                }
            }]
        }
    }
};

window.onload = function() {
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = new Chart(ctx, config);
};

$('#reload-button').on('click', function() {
    $('#overlay').toggle();
    var d = new Date();
    var year = d.getFullYear();

    $.get('http://currency.patilla.es/populate/'+year+'-01-01/' , function(data) {
        console.log('Reloading status: ', data.status);
    });
    window.location.reload();
});