$(function(){
    let students = []
    let searchVal = "name"
    $(".selected-students").hide()

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
        students.push(parseInt($(this).find('.id').text()))
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
        switch ($(this).text()) {
            case "Name":
                searchVal = "name"
                break;
            case "Student ID":
                searchVal = "id"
                break;
        
            default:
                break;
        }
    })


})