function submitText(form) {
    var text = form.newText.value.replace(/\r\n|\r|\n/g,"\\r\\n");
    var site = form.site.value;
    var isAlbum = form.isAlbum.checked;
    var string = '';
    if (isAlbum) {
        string = '{"text": "' + text.substring(0,60).replace(',', '&#44;').replace(':', '&#58;') + '", "site": "' + 
        site.replace(',', '&#44;').replace(':', '&#58;') + '", "isAlbum": ' + isAlbum + '}';
    } else {
        string = '{"text": "' + text + '", "site": "' + site + '", "isAlbum": ' + isAlbum + '}';
    }
    console.log(string);

    $.ajax({
        type: "POST",
        url: "submitContent/",
        data: string,

        success: function(result) {
            if (isAlbum) {
                adminloadFileContent('/administrationpage/fileLoader/'+site+'/');
            } else {
                loadContent('/administrationpage/siteContent/'+site+'/');
            }
        }
    });
}

function loadContent(site) {
    $.getJSON(site, function(data) {
        var content = [''];
        if (data.admin) {
            var subSite = site.split('/');
            content.push('<form id="newSiteContent" action="javascript:submitText(newSiteContent)">'+
                '<input type="hidden" name="site" value="' + subSite[subSite.length - 2] + '"/><textarea cols="100" rows="' +
                 data.siteContent.length / 100 + '" name="newText">' + data.siteContent + '</textarea><br/>Is it an album: '+
                 '<input type="checkbox" name="isAlbum" value="isAlbum"/><br/><input type="submit" value="Submit"/></form>');
            //Has pictures: <input type="checkbox" name="hasFiles" value="hasFiles"/><br/>
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

function loadFileContent(site) {
    $.getJSON(site, function(data) {
        var file = '';
        var title = data.shift().title;
        var content = ['<div class="scroll-pane ui-widget ui-widget-header ui-corner-all"><div class="scroll-content">'];
        var path = data.shift().path;
        var active = data[0].fileLoader.split(':');
        var cnt = 0;

        $.each (data, function (i) {
            file = data[i].fileLoader.split(':');
            content.push('<div class="scroll-content-item ui-widget-header"><img id="' + i + '" src="' + path + file[1] + '" alt="' + 
                file[0] + '">&nbsp;&nbsp;</div>');
            cnt++;
        });


        content.push('</div><div class="scroll-bar-wrap ui-widget-content ui-corner-bottom"><div class="scroll-bar"></div></div></div>');
        $('#siteContent').html('<h2>' + title + '</h2><div id="picture"></div>');

        $('<div/>', {
            id:"gallery",
            html: content.join('')
        }).appendTo('#siteContent');

        $('#picture').html('<img src="' + path + active[1] + '" alt="' + active[0] + '"><p>Beskrivning: ' + active[0] + '</p>');

        setNumbPic();
        setScrollBar();
        console.log($('#siteContent').width() - $('.scroll-bar').width() + '   ' + $('#siteContent').width() + '   ' + $('.scroll-bar').width());
    });
}

function submitAlbum(form) {
    var formData = new FormData($('#newAlbumContent')[0]);

    $.ajax({
        url: 'upload/',
        type: 'POST',
        xhr: function() {
            var myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },

        success: function(data){
            var json = $.parseJSON(data);
            if (json['newFile'] === 'True') {
                var path = json['path'];
                var file = '';
                $.each(json['file'].split(', '), function(i, img) {
                    file = img.split(':')[0];
                    $('#descriptionlist').append('<li>' + file + ': <input type"text" value="' + file + 
                        '" name="file"/><input type="hidden" value="' + file + '" name="file"/><img height="35px" id="' + i + 
                        '" src="' + path + file + '" alt="' + file + '">&nbsp;&nbsp;</li>');
                });
            }
        },

        data: formData,
        cache: false,
        contentType: false,
        processData: false
    });
}

function adminloadFileContent(site) {
    $.getJSON(site, function(data) {
        var file = '';
        var title = data.shift().title;
        var path = data.shift().path;
        var cnt = 0;
        var content = ['<form id="newAlbumContent" enctype="multipart/form-data" action="javascript:submitAlbum(newAlbumContent)">'+
         'Title: <input type="text" name="title" value="' + title + '"/><ul id="descriptionlist">'];

        $.each (data, function (i) {
            file = data[i].fileLoader.split(':');
            content.push('<li>' + file[1] + ': <input type"text" value="' + file[0] + '" name="file"/><input type="hidden" value="' +
             file[1] + '" name="file"/><img height="35px" id="' + i + '" src="' + path + file[1] + '" alt="' + file[0] + '">&nbsp;&nbsp;</li>');
            cnt++;
        });

        content.push('</ul><ul><li><p>Add files... <input type="file" name="files[]" class="multiupload" multiple></p></li><li>'+
            '<input type="hidden" value="' + site.split('/')[3] + '" name="site"/><input type="submit" value="Submit"/></li></ul></form>');

        $('#siteContent').html(content.join(''));
    });
}

var prev;
function reloadPage(e, preAdress, loggedIn) {
    if (e.toElement.href !== undefined) {
        e.stopImmediatePropagation();

        if (prev !== undefined)
            prev.removeClass("cssmenu-active");
        prev = $(e.target.parentElement);
        prev.addClass("cssmenu-active");

        var href = e.toElement.href.split('/');
        if (href[href.length - 2] == 'fileLoader') {
            if (loggedIn) {
                adminloadFileContent(preAdress + '/fileLoader/' + href[href.length - 3] + '/');
            } else {
                loadFileContent('/fileLoader/' + href[href.length - 3] + '/');
            }
        } else {
            loadContent(preAdress + '/siteContent/' + href[href.length - 2] + '/');
        }
        return false;
    }
}
