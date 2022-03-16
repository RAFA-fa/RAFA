var pressure2 = echarts.init(document.getElementById('l1'), 'dark', {renderer: 'canvas'});

    $(
        function () {
            fetchpressureData4(pressure2);
            setInterval(fetchpressureData4, 20000);
        }
    );

    function fetchpressureData4() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/l1",
            dataType: 'json',
            success: function (result) {
                pressure2.setOption(result);
            },

        });
    }
