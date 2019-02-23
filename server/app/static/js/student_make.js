$(() => {

    // Globals ahhhhh!
    let choose = 0

    // check for Student function
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

    // Get RFID function
    $(".search-station").on("click", () => {
        let id = $(".dropdown-rfid").find('.active').attr('id')
        if (Boolean(id)){
            let choose = setInterval(() => {
                $.ajax({
                    type: "POST",
                    url: "/api/get_rfid",
                    contentType: 'application/json;charset=UTF-8',
                    data: JSON.stringify({
                        "rfid_id": id
                    }),
                }).fail((resp) => {
                    $.notify({
                        message: resp.responseText,
                    }, {
                        type: "info",
                        animate: {
                            enter: 'animated fadeInDown',
                            exit: 'animated fadeOutUp',
                        },
                        allow_dismiss: true,
                    })
                })
            }, 2000)
            $(".search-station")
                .removeClass("search-station")
                .addClass("searching-station")
                .text("Cancel")
        } else {
            $.notify({
                message: "Please Select station",
            }, {
                type: "warning",
                animate: {
                    enter: 'animated fadeInDown',
                    exit: 'animated fadeOutUp',
                },
                allow_dismiss: true,
            })
        }
    })

    $(".search-station").on('click', () => {
        clearInterval(choose)
        $(".searching-station")
            .removeClass("searching-station")
            .addClass("search-station")
            .text("Get RFID")
    })

    // Station select
    $(".station-choose").on('click', function (e) {
        e.preventDefault()
        if ($(this).hasClass("active")){
            $(".dropdown-button-station").text("Select RFID")
            $(this).removeClass("active")
        } else {
            $(".dropdown-rfid")
                .find('.active')
                .removeClass('active')
            $(this).addClass('active')            
            $(".dropdown-button-station").text(
                $(this).text()
            )
        }
    })
})