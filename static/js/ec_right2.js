var pressure4 = echarts.init(document.getElementById('r2'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchpressureData3(pressure4);
            setInterval(fetchpressureData3, 20000);
        }
    );

    function fetchpressureData3() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/r2",
            dataType: 'json',
            success: function (result) {
                pressure4.setOption(result);
            },

        });
    }

