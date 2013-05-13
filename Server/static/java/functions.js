function submitText(form) {
    var text = form.newText.value.replace(/\r\n|\r|\n/g,"\\r\\n");
    var site = form.site.value;
    var isAlbum = form.isAlbum.checked;
    console.log(text);
    $.ajax({
        type: "POST",
        url: "submitContent/",
        data: '{"text": "' + text + '", "site": "' + site + '", "isAlbum": ' + isAlbum + '}',

        success: function(result){
            loadContent(site);
        }
    });
}

function loadContent(site){
    $.getJSON(site, function(data) {
        var content = [''];
        if (data.admin) {
            var subSite = site.split('/');
            content.push('<form id="newSiteContent" action="javascript:submitText(newSiteContent)"><input type="hidden" name="site" value="' + subSite[subSite.length - 2] + '"/><textarea cols="100" rows="' + data.siteContent.length / 100 + '" name="newText">' + data.siteContent + '</textarea><br/>Has pictures: <input type="checkbox" name="hasFiles" value="hasFiles"/><br/>Is it an album: <input type="checkbox" name="isAlbum" value="isAlbum"/><br/><input type="submit" value="Submit"/></form>');
        } else {
            content.push('<p>');
            $(data.siteContent.split('\n')).each(function(key, text) {
                content.push('<br/>' + text);
            });
            content.push('</p>');
        }

        $('#siteContent').html(content.join(''));
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

    e.stopImmediatePropagation();
    
    if (prev !== undefined)
        prev.removeClass("cssmenu-active");
    prev = $(e.target.parentElement);
    prev.addClass("cssmenu-active");

    var href = e.toElement.href.split('/');
    if (href[href.length - 2] == 'fileLoader') {
        loadFileContent('/fileLoader/' + href[href.length - 3] + '/');
    } else {
        loadContent('/siteContent/' + href[href.length - 2] + '/');
    }
}
