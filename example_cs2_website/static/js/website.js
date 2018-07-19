// initialization
function websiteInit() {
    updateTimes();
    updateIcons();
}

function updateTimes() {
    $.timeago.settings.allowFuture = true;
    // re-write all timefeed numbers
    timefeeds = document.getElementsByClassName('timefeed');
    for (i=0; i < timefeeds.length; i++) {
        let relativeTime = $.timeago(timefeeds[i].innerText);
        timefeeds[i].innerText = relativeTime;
    }
}

function updateIcons() {
    // determine website path
    var scripts = document.getElementsByTagName("script");
    var staticPath = '';
    for (var i=0; i < scripts.length; i++) {
        var src = scripts[i].src;
        if (src.endsWith('js/website.js')) { 
            staticPath = src.substr(0,src.indexOf("js/website.js"));
        }
    }
    icons = document.getElementsByClassName('icon');
    for (i=0; i < icons.length; i++) {
        let iconInfo = icons[i].innerText.split(":");
        iconName = iconInfo[0];
        iconSize = iconInfo[1];
        var sz = 32;
        if (iconSize == "medium") {
            sz = 32;
        } else if (iconSize == "large") {
            sz = 64;
        } else if (iconSize == "extralarge") {
            sz = 128;
        }
        width = sz;
        if (iconSize == "small") {
            width = 20;
        }


        icons[i].innerHTML = "<img src='"+staticPath+"/img/IKONS/PNG/" + sz + "/" + iconName + ".png' style='width: "+width+"px'>";
    }
}
