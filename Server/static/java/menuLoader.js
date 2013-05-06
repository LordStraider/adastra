function replaceAAO(text) {
    text = text.replace('å', 'a');
    text = text.replace('ä', 'a');
    text = text.replace('ö', 'o');
    text = text.replace('Å', 'A');
    text = text.replace('Ä', 'A');
    text = text.replace('Ö', 'O');
    text = text.replace(' ', '');
    return text;
}

function getSiteString() {
    var site = window.location.href.split('/');
    if (site.length <= 4)
        return "Hem";
    return site[site.length - 2];
}

function loadMenu() {
    $.getJSON('/menu/', function(data) {
        var menu = [];

        $.each (data, function (i) {
            if (data[i].subs.length > 0) {
                menu.push('<li class="has-sub"><a id="deny" href="/' + data[i].linked + '/">' + data[i].menu + '</a><ul>');

                $.each (data[i].subs, function (j) {
                    menu.push('<li><a id="deny" href="/' + data[i].linked + '/' + data[i].subs[j].linked + '/">' + data[i].subs[j].sub + '</a></li>');
                });

                menu.push('</ul></li>');

            } else {
                menu.push('<li class="active"><a id="deny" href="/' + data[i].linked + '/">' + data[i].menu + '</a></li>');
            }
        });

        $('<ul/>', {
            html: menu.join('')
        }).appendTo('#cssmenu');
    });
}