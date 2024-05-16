$(document).ready(function() {

    $(".category-tag").each(function() {

        var categoryId = $(this).data("category-id");

        switch(categoryId) {
            case 1:
                $(this).addClass("bg-primary");
                break;
            case 2:
                $(this).addClass("bg-secondary");
                break;
            case 3:
                $(this).addClass("bg-success");
                break;
            case 4:
                $(this).addClass("bg-danger");
                break;
            case 5:
                $(this).addClass("bg-info");
                break;
            default:
                break;
        }
    });
});