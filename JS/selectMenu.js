(function(){
    "use strict";
    //添付メニューの設定
    kintone.events.on("app.record.create.change.SelectionMenu",function(event){
        var record = event.record;
        console.log(record);
        var strSelectMenu = String(record.SelectionMenu.value); //発注品の入力値取得
        console.log(strSelectMenu);
        if (strSelectMenu == "ソフトウェア"){
            record.detail.value = "";
            record.software.disabled = false;
            record.detail.disabled = true;
            return event;
        }
        else if (strSelectMenu == "ノートPC"||strSelectMenu == "デスクトップPC"){
            record.software.value = "";
            record.detail.disabled = false;
            record.software.disabled = true;
            return event;
        }
        else{
            record.software.disabled = false;
            record.detail.disabled = false;
            return event;
        }
    });
})();