function createLink(text) {
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
        return "siteContent/Hem";
    return site[site.length - 2];
}

function submitSubMenu(subMenu) {
    var link = createLink(subMenu.menu.value);
    var text = subMenu.menu.value;
    var site = subMenu.site.value;

    $.ajax({
        type: "POST",
        url: "submitMenu/",
        data: '{"text": "' + text + '", "link": "' + link + '", "site": "' + site + '"}',

        success: function(result){
            if (result) {
                $('#cssmenu ul li ul').append('<li><a href="/' + site + '/' + link + '/">' + text + '</a></a></li>');
            }
        }
    });
}

function submitMenu(menu) {
    var link = createLink(menu.menu.value);
    var text = menu.menu.value;

    $.ajax({
        type: "POST",
        url: "submitMenu/",
        data: '{"text": "' + text + '", "link": "' + link + '"}',

        success: function(result){
            if (result) {
                $('#cssmenu ul').append('<li><a href="/' + link + '/">' + text + '</a></li>');
            }
        }
    });
}

function loadMenu(loggedIn) {
    $.getJSON('/menu/', function(data) {
        var menu = [];

        $.each (data, function (i) {
            if (data[i].subs.length > 0) {
                menu.push('<li class="has-sub" id="tabs"><a href="/' + data[i].linked + '/">' + data[i].menu + '</a>');

                /*if (loggedIn) {
                    menu.push('<img ');
                }*/
                menu.push('<ul>');

                $.each (data[i].subs, function (j) {
                    menu.push('<li><a href="/' + data[i].linked + '/' + data[i].subs[j].linked + '/">' + data[i].subs[j].sub + '</a>');

                    /*if (loggedIn) {
                        menu.push('<img ');
                    }*/
                    menu.push('</li>');
                });

                if (loggedIn) {
                    id = 'newSubMenu' + i;
                    menu.push('<li><form id="' + id + '" action="javascript:submitSubMenu(' + id + ')"><input type="hidden" name="site" value="' + data[i].linked + '"/><input type="text" name="menu" value="New menu"/><input type="submit" value="Add"/></form></li>');
                }

                menu.push('</ul></li>');
            } else {
                menu.push('<li><a href="/' + data[i].linked + '/">' + data[i].menu + '</a>');

                /*if (loggedIn) {
                    menu.push('<img ');
                }*/
                menu.push('</li>');
            }
        });

        if (loggedIn) {
            menu.push('<li><form id="newMenu" action="javascript:submitMenu(newMenu)"><input type="text" name="menu" value="New menu"/><input type="submit" value="Add"/></form></li>');
        }

        $('<ul/>', {
            html: menu.join('')
        }).appendTo('#cssmenu');
    });
}