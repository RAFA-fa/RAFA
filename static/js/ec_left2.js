var line = echarts.init(document.getElementById('l2'), 'dark', {renderer: 'canvas'});
var old_data = [];
$(
    function () {
        fetchlineData(line);
        setInterval(fetchlineData, 20000);
    }
);

function fetchlineData() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/l2",
        dataType: "json",
        success: function (result) {
            line.setOption(result);
            old_data = line.getOption().series[0].data;
        }
    });
}
