(function(){
    "use strict";
    //メール作成ボタンの設置
    kintone.events.on('app.record.detail.show', function(event) {
        var mySpaceFieldButton = document.createElement('button');
        mySpaceFieldButton.id = 'getRecord_button';
        mySpaceFieldButton.innerText = 'メール送信';
        mySpaceFieldButton.onclick = function() {
            //kintoneのレコード値取得
            var CamName = ''; //発注先（ルックアップフィールド）
            var rec_cpny = kintone.app.record.get();
            if (rec_cpny){
                CamName = rec_cpny.record.lookup.value;
            }
            console.log(rec_cpny.record.lookup.value);

            var ToPSN = ''; //発注先担当者メールアドレス（メールTo)
            var rec_to = kintone.app.record.get();
            if (rec_to){
                ToPSN = rec_to.record.mailAdd.value;
            }
            console.log(rec_to.record.mailAdd.value);

            var ToName = ''; //発注先担当者名
            var rec_tName = kintone.app.record.get();
            if (rec_tName){
                ToName = rec_tName.record.tName.value;
            }
            console.log(rec_tName.record.tName.value);

            var Menu = ''; //発注品名
            var rec_menu = kintone.app.record.get();
            if (rec_menu){
                Menu = rec_menu.record.SelectionMenu.value;
            }
            console.log(rec_menu.record.SelectionMenu.value);
            var StrRecMenu = String(rec_menu.record.SelectionMenu.value); // オブジェクトを文字型に変換

            var FromName = ''; //発注者名(メールFrom)
            var rec_frm = kintone.app.record.get();
            if (rec_frm){
                FromName = rec_frm.record.inCharge.value;
            }
            console.log(rec_frm.record.inCharge.value);

            var Body = ''; //PCスペック内容
            var rec_body= kintone.app.record.get();
            if (rec_body){
                Body = rec_body.record.detail.value;
            }
            var StrRecBody = String(rec_body.record.detail.value); //変数オブジェクトを文字型に変換
            var RplRecBody = StrRecBody.replace(/<br>/g,"%0d%0a"); //改行表現の置換
            //console.log(rec_body.record.detail.value);
            console.log(RplRecBody);

            var softWare = ''; //ソフトウェア内容
            var rec_soft= kintone.app.record.get();
            if (rec_soft){
                softWare = rec_soft.record.software.value;
            }
            var StrRecSoftware = String(rec_soft.record.software.value); //変数オブジェクトを文字型に変換
            var RplRecSoftware = StrRecSoftware.replace(/<br>/g,"%0d%0a"); //改行表現の置換
            //console.log(rec_body.record.software.value);
            console.log(RplRecSoftware);      

            //mail作成フェーズ
            location.href = "mailto:" + rec_to.record.mailAdd.value  + '?CC=' + 'ken_itou@daiseki-eco.co.jp;' + 'm_tanaka@daiseki-eco.co.jp;' + 'a_senga@daiseki-eco.co.jp;' + '&subject=' + '見積もり依頼'
             + '&body=' + rec_cpny.record.lookup.value + '%0d%0a' + rec_tName.record.tName.value + '様%0d%0a%0d%0a' + 'いつも大変お世話になっております。%0d%0a' 
             + '(株)ダイセキ環境ソリューションの' +rec_frm.record.inCharge.value + 'です。%0d%0a%0d%0a下記内容のお見積りをいただきたく存じます%0d%0a%0d%0a'
             + '発注品：' + StrRecMenu + '%0d%0a' + RplRecBody + RplRecSoftware +'よろしくお願いいたします。%0d%0a' ;
        };
    kintone.app.record.getSpaceElement('getRecord').appendChild(mySpaceFieldButton);
    });
})();
