(function() {
  'use strict';

  // 【一括でチェックする機能の追加】
  var CHECK_ALL = '一括';
  var CHECK_MARK = '✓';
  var CHECKBOX = '貸与物';
  var CHECKBOX_VALUE = ['社員証', 'ノートパソコン', 'スマートフォン', 'デスクトップPC', 'その他'];
  var checkEvents = ['app.record.create.change.' + CHECK_ALL, 'app.record.edit.change.' + CHECK_ALL];

  function checkAll(event) {

    var record = event.record;
    var changes = event.changes.field.value;

    if (changes[0] === CHECK_MARK) {
      record[CHECKBOX].value = CHECKBOX_VALUE;
    } else {
      record[CHECKBOX].value = [];
    }
    return event;
  }

  kintone.events.on(checkEvents, checkAll);


  // 【レコード編集・作成時に各種ボタンを配置する】
  var LOAN_TABLE = '利用状況';
  var CHECKBOX = '貸与物';
  var PASSWORD = '初期パスワード';
  var ID = 'ID';
  var CREATE_ROW = 'createRow';
  var HINT_ROW = 'hintRow';
  var CREATE_PASS = 'createPassword';
  var HINT_PASS = 'hintPassword';
  var createButtonEvents = ['app.record.create.show', 'app.record.edit.show'];

  function addButton(event) {

    var record = event.record;
    var rowButton = document.createElement('button');
    var rowDiv = document.createElement('div');
    rowDiv.textContent = '行一括追加';

    rowButton.setAttribute('class', 'create');
    rowButton.appendChild(rowDiv);


    // 【チェックされた項目に応じた行をテーブルに追加する】
    function createRow() {
      var event = kintone.app.record.get();
      var record = event.record;
      var rowsToCreate = record[CHECKBOX].value.length;


      var table = record[LOAN_TABLE].value;
      var newRow;

      table.length = 0;

      for (var i = 0; i < rowsToCreate; i++) {
        newRow = {
          value: {
            ID: {type: 'NUMBER', value: i + 1},
            貸与物_テーブル: {type: 'DROP_DOWN', value: record[CHECKBOX].value[i]},
            備考: {type: 'MULTI_LINE_TEXT', value: ' '},
            状況: {type: 'RADIO_BUTTON', value: '未準備'},
            貸与日: {type: 'DATE', value: undefined},
            返却日: {type: 'DATE', value: undefined}
          }
        };

        if (record[CHECKBOX].value[i] === 'その他') {
          newRow.value.備考.value = '(貸出機器の詳細を記載して下さい。)';
        }
        table.push(newRow);
      }

      kintone.app.record.set(event);
    }


    // 【テーブルへの行追加のヒントを表示する】
    var hintRowDiv = document.createElement('div');
    var hintRowI = document.createElement('i');

    hintRowI.setAttribute('class', 'fas fa-question-circle fa-lg');
    hintRowDiv.appendChild(hintRowI);

    function showHintRow() {
      toastr.info('チェックされた貸与物を元に、自動でテーブル行を追加します。既に値があった場合、上書きされるのでご注意ください');
      toastr.options = {
        'closeButton': true,
        'positionClass': 'toast-bottom-left',
        'preventDuplicates': true
      };
    }


    // 【パスワードを自動生成する】
    var passButton = document.createElement('button');
    var passDiv = document.createElement('div');
    passDiv.textContent = 'パスワード自動生成';

    passButton.setAttribute('class', 'create');
    passButton.appendChild(passDiv);

    function createPass() {
      var event = kintone.app.record.get();
      var record = event.record;

      var newPassword = '';
      var str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      var len = 8;

      for (var i = 0; i < len; i++) {
        newPassword += str.charAt(Math.floor(Math.random() * str.length));
      }

      record[PASSWORD].value = newPassword;

      kintone.app.record.set(event);
    }


    // 【パスワード自動生成のヒントを表示する】
    var hintPassDiv = document.createElement('div');
    var hintPassI = document.createElement('i');

    hintPassI.setAttribute('class', 'fas fa-question-circle fa-lg');
    hintPassDiv.appendChild(hintPassI);

    function showHintPass() {
      toastr.info('半角英数字からランダムな 8桁文字列を生成します');
      toastr.options = {
        'closeButton': true,
        'positionClass': 'toast-bottom-left',
        'preventDuplicates': true
      };
    }


    rowButton.addEventListener('click', createRow);
    passButton.addEventListener('click', createPass);
    hintPassDiv.addEventListener('click', showHintPass);
    hintRowDiv.addEventListener('click', showHintRow);
    kintone.app.record.getSpaceElement(CREATE_ROW).appendChild(rowButton);
    kintone.app.record.getSpaceElement(CREATE_PASS).appendChild(passButton);
    kintone.app.record.getSpaceElement(HINT_PASS).appendChild(hintPassDiv);
    kintone.app.record.getSpaceElement(HINT_ROW).appendChild(hintRowDiv);
  }

  kintone.events.on(createButtonEvents, addButton);


  // 【テーブルの各行に ID を自動生成する】
  var LOAN_TABLE = '利用状況';
  var ID = 'ID';
  var addRowEvents = ['app.record.create.change.' + LOAN_TABLE, 'app.record.edit.change.' + LOAN_TABLE];

  function addID(event) {

    var record = event.record;
    var changes = event.changes.field.value;

    for (var i = 0; i < changes.length; i++) {
      changes[i].value[ID].value = i + 1;
    }
    return event;
  }
  kintone.events.on(addRowEvents, addID);


  // 【チェックボックスの状況に応じて、適切な日付を設定・削除する】
  var CHECKBOX = '貸与物';
  var LOAN_OBJECT = '貸与物_テーブル';
  var LOAN_SITUATION = '状況';
  var LOAN_DONE = '貸与済';
  var LOAN_RETURNED = '回収済';
  var LOAN_TABLE = '利用状況';
  var LOAN_PASSED_DATE = '貸与日';
  var LOAN_RETURNED_DATE = '返却日';
  var LOAN_NOTE = '備考';
  var checkSituationEvents = ['app.record.create.change.' + LOAN_SITUATION, 'app.record.edit.change.' + LOAN_SITUATION];

  function addDate(event) {

    var record = event.record;
    var changes = event.changes.field.value;
    var changedRow = event.changes.row.value.ID.value - 1;
    var today = moment().format('YYYY-MM-DD');
    var loanedObject = record[CHECKBOX].value;
    var changedObject = record[LOAN_TABLE].value[changedRow].value[LOAN_OBJECT].value;
    var idx = loanedObject.indexOf(changedObject);
    var returnedDate = record[LOAN_TABLE].value[changedRow].value[LOAN_RETURNED_DATE].value;

    if (changes === LOAN_DONE) {
      if (returnedDate) {
        record[LOAN_TABLE].value[changedRow].value[LOAN_NOTE].value +=
          '\n貸与日：' + record[LOAN_TABLE].value[changedRow].value[LOAN_PASSED_DATE].value +
          '\n返却日：' + record[LOAN_TABLE].value[changedRow].value[LOAN_RETURNED_DATE].value +
          '\n----';
      }
      record[LOAN_TABLE].value[changedRow].value[LOAN_PASSED_DATE].value = today;
      record[LOAN_TABLE].value[changedRow].value[LOAN_RETURNED_DATE].value = undefined;
      loanedObject.push(changedObject);
    } else if (changes === LOAN_RETURNED) {
      record[LOAN_TABLE].value[changedRow].value[LOAN_RETURNED_DATE].value = today;
      if (idx >= 0) {
        loanedObject.splice(idx, 1);
      }
    }
    return event;
  }
  kintone.events.on(checkSituationEvents, addDate);

})();
