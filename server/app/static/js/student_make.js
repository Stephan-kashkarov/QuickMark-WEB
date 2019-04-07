$(() => { // document ready

    // Globals ahhhhh!
    let choose = 0
    let rfid

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
    $(document).on("click", ".search-station", () => {
        let id = $(".dropdown-rfid").find('.active').attr('id')
        rfid = 0
        if (Boolean(id)){
            console.log(`Choose was ${choose}`)
            choose = setInterval(() => {
                $.ajax({
                    type: "POST",
                    url: "/api/get_rfid",
                    contentType: 'application/json;charset=UTF-8',
                    data: JSON.stringify({
                        "rfid_id": id
                    }),
                }).fail((resp) => {
                    // Update IF statement
                    if (resp.status === 201){
                        rfid = resp.responseText
                    }
                    // Notif If statement
                    if (resp.status !== 404){
                        $.notify({
                            message: (resp.status === 201) ? `Scan found RFID: ${resp.responseText}`: "Scan Starting",
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
            }, 2000)
            console.log(`Choose is ${choose}`)
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

    // Cancle button
    $(document).on('click', ".searching-station", () => {
        console.log(`Clearing: ${choose}`)
        clearInterval(choose)
        $(".searching-station")
            .removeClass("searching-station")
            .addClass("search-station")
            .text("Get RFID")
    })

    // Station select
    $(document).on('click', ".station-choose", function (e) {
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

    // Create student button
    $('.create-student').on('click', () => {
        console.log("HELLO!Z")
        $.ajax({
            type: "POST",
            url: "/api/student/make",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                "id": $("#student-id").val(),
                "name": $("#student-name").val(),
                "rfid": (rfid > 0) ? rfid : null,
            }),
        }).fail((resp)=>{
            console.log(resp.responseText)
        })
    })
})