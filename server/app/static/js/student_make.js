$(() => {
    $("#button-student-check").on('click', () => {
        $.ajax({
            type: "POST",
            url: "/api/db/student",
            data: JSON.stringify({
                "searchType": "Student ID",
                "searchVal": $("#student-id").val(),
            }),
            contentType: 'application/json;charset=UTF-8',
            dataType: 'jsonp',
        }).fail((resp) => {
            if (resp.status === 200 | resp.status === 201){
                $.notify({
                    message: "Student Exists",
                }, {
                    type: "warning",
                    animate: {
                        enter: 'animated fadeInDown',
                        exit: 'animated fadeOutUp',
                    },
                    allow_dismiss: true,
                })
            } else if (resp.status === 404){
                $.notify({
                    message: "Student Not Found",
                }, {
                    type: "info",
                    animate: {
                        enter: 'animated fadeInDown',
                        exit: 'animated fadeOutUp',
                    },
                    allow_dismiss: true,
                })
            }
        })
    })

    $(".search-station").on("click", () => {
        let check = setInterval(() => {
            $.ajax({
                type: "POST",
                url: "/api/get_rfid",
                contentType: 'application/json;charset=UTF-8',
                dataType: 'jsonp',
                data: JSON.stringify({
                    "rfid_id": $(".dropdown-rfid").find('active').attr('id')
                }),
            })
        }, 2000)
        $(".search-station")
        .removeClass("search-station")
        .addClass("searching-station")
        .text("Cancel")
        .on('click', () => {
            window.clearInterval(check)
            $(".searching-station")
            .removeClass("searching-station")
            .addClass("search-station")
            .text("Get RFID")
        })
    })
})