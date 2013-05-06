function loadContent(site){
    $.getJSON('/siteContent/' + site + '/', function(data) {
        $('#siteContent').html('<p>' + data.siteContent + '</p>');
    });
}

function changePicture(src, alt) {
    if (src !== undefined) {
        var file = src.split('http://localhost:8000');
        $('#picture').html('<p>Beskrivning: ' + alt + '</p><img src="' + file[1] + '" alt="' + alt + '">');
    }
}

function loadFileContent(site){
    $.getJSON('/fileLoader/' + site + '/', function(data) {
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
        $('#siteContent').html('<h2>' + title + '</h2><div id="picture"><p>Beskrivning: ' + active[0] + '</p></div>');

        $('<div/>', {
            id:"gallery",
            html: content.join('')
        }).appendTo('#siteContent');

        $('<img>', {
            src: path + active[1],
            alt: active[0]
        }).appendTo('#picture');

        $(document).trigger('IssuesReceived');
    });
}
