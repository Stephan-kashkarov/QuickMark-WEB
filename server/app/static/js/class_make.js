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

function updateThings() {
    let active_search = ($("#name-selected").hasClass("active")) ?
        "student_name" :
        "student_id"
    let resp = $.ajax({
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        url: "/api/db/query/Student",
        data: JSON.stringify({
            "key": `Student.${active_search}`,
            "val": $(".search-text-input").val(),
        }),
        async: false,
    })

    $(".search-students").empty()
    let data = JSON.parse(resp.responseText).filter((student) => {
        students.contains(student) < 0
    })
    data.map((student) => {
        $(".search-students").append([student].map(student_card).join(""))
    })
}



$(() => {
    try {
        updateThings()
    }
    catch (e) {}

    $(".selected-students").hide() // hides second tab

    $(".changes-apply").on('click', () => {
        students.push(temp_students.slice())
        temp_students = []
    })

    // look at this chain lol
    $(document).on('mouseenter', ".student", function () {
        $(this).animate({
            backgroundColor: "#007bff",
        }, 100)
    }).on('mouseleave', ".student", function () {
        $(this).animate({
            backgroundColor: "#868e96",
        }, 100)
    }).on('click', ".student", function () {
        $(this).animate({
            backgroundColor: "#0067eb",
        }, 100)
        $(this).removeClass("student").addClass("added-student")
        temp_students.push(parseInt($(this).find('.student-id').text()))
    }).on('click', ".added-student", function () {
        $(this).animate({
            backgroundColor: "#007bff",
        }, 100)
        $(this).removeClass("added-student").addClass("student")
        let id = parseInt($(this).find('.id').text())
        students.splice(students.indexOf(id), 1)
    }).on('mouseenter', '.added-student', function () {
        $(this).animate({
            backgroundColor: "#007bff",
        }, 100)
    }).on('mouseleave', '.added-student', function() {
        $(this).animate({
            backgroundColor: "#0067eb",
        }, 100)
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
        // Clear all timeouts
        for (i = 0; i < 100; ++i) {
            window.clearTimeout(i);
        }
        setTimeout(updateThings(), 4000)
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
                if (resp.status === 200 || resp.status === 201) {
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