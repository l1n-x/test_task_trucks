$( document ).ready(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    // Устанавливаем селект в нужный стейт
    $(function() {
        let searchParams = new URLSearchParams(window.location.search)
        if (searchParams.has('model')){
            let model_param = searchParams.get('model')
            $('#model-select').val(model_param)
        }
    });

    // Редиректим на нужную страницу по модели
    $('#apply').on('click', function(){
        let page_val = $('#model-select').val()
        if (page_val !== '') {
            page_val = '?model=' + page_val
        }
        window.location.href = window.location.pathname + page_val
    })

});  // End of document ready script