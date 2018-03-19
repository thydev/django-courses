function utcToLocal(utdDate){
    var date = new Date(utdDate + " UTC");
    return date.toString();
}

$(document).ready(function(){
    console.log('ready');
    console.log($('.cdate'));
    var dates = $('.cdate')
    for(let i = 0; i < dates.length; i++){
        console.log($(dates[i]).text());
        console.log(utcToLocal($(dates[i]).text()));
        console.log(utcToLocal('2018-03-18 04:50:11.450293'));
        // 2018-03-18 04:50:11.450293
        //Do not need anymore, all stuffs are already converted from server side
    }
    
});