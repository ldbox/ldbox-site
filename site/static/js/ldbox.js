// Copyright 2015 Oleg Girko <ol@infoserver.lv>
//
// This file is part of ldbox.site Python package.
//
// ldbox.site Python package is free software: 
// you can redistribute it and/or modify
// it under the terms of the GNU Affero Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Foobar is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero Public License for more details.
//
// You should have received a copy of the GNU Affero Public License
// along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

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
