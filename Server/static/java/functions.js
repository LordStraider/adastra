function loadContent(site){
    console.log(site);
    $.getJSON(site, function(data) {
        $('#siteContent').html('<p>' + data.siteContent + '</p>');
    });
}

function changePicture(src, alt) {
    if (src !== undefined) {
        var file = src.split('http://localhost:8000');
        $('#picture').html('<img src="' + file[1] + '" alt="' + alt + '"><p>Beskrivning: ' + alt + '</p>');
    }
}

function loadFileContent(site){
    $.getJSON(site, function(data) {
        var file = '';
        var title = data.shift().title;
        var content = ['<ul class="pictureList">'];
        var path = data.shift().path;
        var active = data[0].fileLoader.split(':');
        var cnt = 0;

        $.each (data, function (i) {
            file = data[i].fileLoader.split(':');
            content.push('<li><img id="' + i + '" src="' + path + file[1] + '" alt="' + file[0] + '">&nbsp;&nbsp;</li>');
            cnt++;
        });

        content.push('</ul>');
        $('#siteContent').html('<h2>' + title + '</h2><div id="picture"></div>');

        $('<div/>', {
            id:"gallery",
            html: content.join('')
        }).appendTo('#siteContent');

        $('#picture').html('<img src="' + path + active[1] + '" alt="' + active[0] + '"><p>Beskrivning: ' + active[0] + '</p>');

        setNumbPic();
    });
}
var prev;
function reloadPage(e) {
    if (e.toElement.href === undefined) {
        return false;
    }

    if (prev !== undefined)
        prev.removeClass("cssmenu-active");
    prev = $(e.target.parentElement);
    prev.addClass("cssmenu-active");

    var href = e.toElement.href.split('/');
    if (href[href.length - 2] == 'fileLoader') {
        loadFileContent('/administrationpage/fileLoader/' + href[href.length - 3] + '/');
    } else {
        loadContent('/administrationpage/siteContent/' + href[href.length - 2] + '/');
    }
}
