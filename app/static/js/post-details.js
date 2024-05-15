$(document).ready(function() {
    var categoryId = $("#categoryTag").data("category-id");

    switch(categoryId) {
        case 1:
            $("#categoryTag").addClass("bg-primary");
            break;
        case 2:
            $("#categoryTag").addClass("bg-secondary");
            break;
        case 3:
            $("#categoryTag").addClass("bg-success");
            break;
        case 4:
            $("#categoryTag").addClass("bg-danger");
            break;
        case 5:
            $("#categoryTag").addClass("bg-info");
            break;
        default:
            break;
    }
});

$(document).ready(function() {
    var $stickyElement = $("#newcommentBtn");
    var offsetThreshold = 205;

    $(window).scroll(function() {
        var scrollPosition = $(this).scrollTop();

        if (scrollPosition >= offsetThreshold) {
            $stickyElement.addClass("sticky");
        } else {
            $stickyElement.removeClass("sticky");
        }
    });
});

