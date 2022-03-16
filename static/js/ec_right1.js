var pressure3 = echarts.init(document.getElementById('r1'), 'dark', {renderer: 'canvas'});

    $(
        function () {
            fetchpressureData2(pressure3);
            setInterval(fetchpressureData2, 20000);
        }
    );

    function fetchpressureData2() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/r1",
            dataType: 'json',
            success: function (result) {
                pressure3.setOption(result);
            },

        });
    }