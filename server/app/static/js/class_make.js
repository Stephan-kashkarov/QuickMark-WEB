$(function(){
    let students = []


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
            backgroundColor: "#007bff",
        }, 100)
        $(this).removeClass("student").addClass("added-student")
        students.push(parseInt($(this).find('.id').innerText()))
    })

    $(".added-student").on('click', function(){
        $(this).animate({
            backgroundColor: "#868e96",
        }, 100)
        $(this).removeClass("added-student").addClass("student")
        let id = parseInt($(this).find('.id').innerText())
        students.splice(students.indexOf(id), 1)
    })
})