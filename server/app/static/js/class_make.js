const student_card = ({
    id,
    student_id,
    student_name
}) => `
<div class="student card text-white mb-3 col">
    <div class="card-body">
        <h5 class="card-title student-id">${id}</h5>
        <p class="card-text">${student_id}<br>${student_name}</p>
    </div>
</div>
`
let students = []
let temp_students = []
let searchVal = "name"




$(() => {

    $(".selected-students").hide() // hides second tab

    $(".changes-apply").on('click', () => {
        students = temp_students.slice()
        temp_students = []
    })

    $(".student").on('mouseenter', function() {
        $(this).animate({
            backgroundColor: "#007bff",
        }, 100)
    }).on('mouseleave', function() {
        $(this).animate({
            backgroundColor: "#868e96",
        }, 100)
    }).on('click', function() {
        $(this).animate({
            backgroundColor: "#0067eb",
        }, 100)
        $(this).removeClass("student").addClass("added-student")
        temp_students.push(parseInt($(this).find('.student-id').text()))
    })

    $(".added-student").on('click', function(){
        $(this).animate({
            backgroundColor: "#007bff",
        }, 100)
        $(this).removeClass("added-student").addClass("student")
        let id = parseInt($(this).find('.id').text())
        students.splice(students.indexOf(id), 1)
    })

    $(".class-groups").on('click', function(e){
        e.preventDefault()
        $(".class-tabs").find(".active").removeClass("active")
        $(this).addClass('active')
        $('.search-students').toggle()
        $('.selected-students').toggle()
    })

    $(".search-choose").on('click', function(e){
        e.preventDefault()
        $(".search-choose-menu").find('.active').removeClass('active')
        $(this).addClass('active')
        $('.search-name').text($(this).text())
    })

    $(".search-text-input").on("keyup", () => {
        console.log("TYPETYPE")

        // Clear all timeouts
        for (i = 0; i < 100; i++) {
            window.clearTimeout(i);
        }

        setTimeout(() => {
            let active_search = ($("#name-selected").hasClass("active"))
                ? "student_name"
                : "student_id"
            $.ajax({
                type: "POST",
                contentType: 'application/json;charset=UTF-8',
                url: "/api/db/query/Student",
                data: JSON.stringify({
                    "key": `Student.${active_search}`,
                    "val": $(".search-text-input").val(),
                })
            }).fail((resp) => {
                console.log(`UPDATING WITH:\n${resp.responseText}`)
                $(".search-students").empty()
                JSON.parse(resp.responseText).map((student) => {
                    $(".search-student").append(
                        student.map(student_card).join("")
                    )
                })
            })
        }, 1000)
    })

    $(".make-class-btn").on('click', function(e) {
        e.preventDefault()
        if (
            $("#class-name").val() &&
            $("#class-desc").val() &&
            students.length >= 1
        ){
            data = {
                "title": $("#class-name").val(),
                "desc": $("#class-desc").val(),
                "students": students,
            }
            $.ajax({
                type: "POST",
                url: "/api/class/make",
                contentType: 'application/json;charset=UTF-8',
                dataType: 'jsonp',
                data: data,
            }).fail((resp) => {
                if (resp.status === 200 | resp.status === 201) {
                    $.notify({
                        message: "Class created!, Redirecting!",
                    }, {
                        type: "success",
                        animate: {
                            enter: 'animated fadeInDown',
                            exit: 'animated fadeOutUp'
                        },
                        allow_dismiss: true,
                    })
                    setTimeout(2000, () => {
                        window.location.pathname = "/dash"
                    })
                } else {
                    $.notify({
                        message: resp.responseText,
                    }, {
                        type: "danger",
                        animate: {
                            enter: 'animated fadeInDown',
                            exit: 'animated fadeOutUp'
                        },
                        allow_dismiss: true,
                    })
                }
            })
        } else {
            $.notify({
                message: "You have empty fields.<br> Do you have a title, description and atleast one student?",
            }, {
                type: "danger",
                animate: {
                    enter: 'animated fadeInDown',
                    exit: 'animated fadeOutUp'
                },
                allow_dismiss: true,
            })
        }
    })

    $(".register-student").on('click', () => {
        window.location.pathname = "/student/make"
    })
})