    function gettime() {
        $.ajax({
            url: "/time",
            timeout: 100000,
            success: function (data) {
                $("#time").html(data)
            }
        });

    }

    setInterval(gettime, 1000)

    function get_demographic_data() {
        $.ajax({
            url: "/demo",
            timeout: 100000,
            success: function (data) {
                $(".num h2").eq(0).text('IN_ICU_TIME : ' + data.INICUDATETIME + ' : ' + data.Age)
                $(".num h2").eq(1).text('IN_ICU_TIME : ' + data.INICUDATETIME + ' : ' + data.Gender)
            }
        });
    }

    setInterval(get_demographic_data, 1000)

    function get_lab_data() {
        $.ajax({
            url: "/lab",
            timeout: 100000,
            success: function (data) {
                $(".num h2").eq(2).text('Chart : ' + data.Charttime + ' : ' + data.CLUCOSE)
                $(".num h2").eq(3).text('Chart : ' + data.Charttime + ' : ' + data.PO2)
                $(".num h2").eq(4).text('Chart : ' + data.Charttime + ' : ' + data.PAO2)
                $(".num h2").eq(5).text('Chart : ' + data.Charttime + ' : ' + data.PCO2)
                $(".num h2").eq(6).text('Chart : ' + data.Charttime + ' : ' + data.PH)
                $(".num h2").eq(7).text('Chart : ' + data.Charttime + ' : ' + data.BASE_EXCESS)
                $(".num h2").eq(8).text('Chart : ' + data.Charttime + ' : ' + data.TOTALCO2)
                $(".num h2").eq(9).text('Chart : ' + data.Charttime + ' : ' + data.LACTATE)
            }
        });
    }

    setInterval(get_lab_data, 1000)
