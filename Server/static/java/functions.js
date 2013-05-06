function loadContent(site){
    $.getJSON('/siteContent/' + site + '/', function(data) {
        $('#siteContent').html('<p>' + data.siteContent + '</p>');
    });
}

function changePicture(src) {
    if (src != undefined) {
        var file = src.split('http://localhost:8000');
        $('#picture').html('<img src="' + file[1] + '" alt="' + file[1] + '">');
    }
}

function loadFileContent(site){
    $.getJSON('/fileLoader/' + site + '/', function(data) {
        var active = '';
        var file = '';
        var title = data.shift().title;
        var content = ['<ul class="pictureList">'];
        $.each (data, function (i) {
            file = data[i].fileLoader;
            content.push('<li><img src="' + file + '" alt="' + file + '">&nbsp;&nbsp;</li>');
        });

        active = file;

        content.push('</ul>');
        $('#siteContent').html('<h2>' + title + '</h2><div id="picture"></div>');

        $('<div/>', {
            id:"gallery",
            html: content.join('')
        }).appendTo('#siteContent');

        $('<img>', {
            src: active,
            alt: active
        }).appendTo('#picture');
    });
}
