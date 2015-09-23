$('#btn-ldbox_login').on('click', function(e) {
    e.preventDefault();
    var url = $(this).attr('href');
    $.get(url, function(data){
        parser = new DOMParser();
        doc = parser.parseFromString(data, "text/html");
        elem = doc.getElementById("loginform");
        $('#login-modal .modal-body').empty().append(elem.innerHTML);
        $('#login-modal').modal('show');
    });
});

$('#btn-ldbox_logout').on('click', function(e) {
    e.preventDefault();
    var ret = document.URL;
    var url = $(this).attr('href');
    $.get(url, function(data){
        window.location.href = ret;
    });
});

if ($('#btn-ldbox_login').length) {
    var ldbox_login_url = $('#btn-ldbox_login').attr('href');
    var ldbox_login_keyword = "login";
    var ldbox_login_progress = 0;
    $('#btn-ldbox_login').remove();
    $(window).keypress(function(ev) {
        if (ev.which == ldbox_login_keyword.charCodeAt(ldbox_login_progress)) {
            ++ldbox_login_progress;
            if (ldbox_login_progress >= ldbox_login_keyword.length) {
                ldbox_login_progress = 0;
                $.get(ldbox_login_url, function(data){
                    doc = $.parseHTML(data);
                    elem = $("#loginform", doc);
                    $('#login-modal .modal-body').empty().append(elem);
                    $('#login-modal').modal('show');
                });
            }
        } else {
            ldbox_login_progress = 0;
        }
    });
}
