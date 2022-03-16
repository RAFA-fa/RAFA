var line = echarts.init(document.getElementById('l1'), 'dark', {renderer: 'canvas'});
var old_data = [];
$(
    function () {
        fetchlineData(line);
        // setInterval(getDynamicData, 20000);
        setInterval(fetchlineData, 20000);
    }
);

function fetchlineData() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/lineChart",
        dataType: "json",
        success: function (result) {
            line.setOption(result);
            old_data = line.getOption().series[0].data;
        }
    });
}

var pressure = echarts.init(document.getElementById('l2'), 'dark', {renderer: 'canvas'});

$(
    function () {
        fetchpressureData(pressure);
        setInterval(fetchpressureData, 20000);
    }
);

function fetchpressureData() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/pressureChart",
        dataType: 'json',
        success: function (result) {
            pressure.setOption(result);
        },

    });
}






