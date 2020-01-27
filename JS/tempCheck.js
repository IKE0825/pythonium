(function(){
    "use strict";
    //添付ファイルのチェック
    kintone.events.on('app.record.edit.change.status',function(event){
        var record = event.record;
        console.log(record);
        var strStatus = String(record.status.value); //状況の入力値取得
        console.log(strStatus);
        var count = document.getElementsByClassName('plupload_file_name').length; //添付ファイル有無情報取得
        console.log(count);
        if (strStatus == '納品待ち'){
            if (count === 0){
                alert('見積書を必ず添付してください');
            }
        }
    });
})();