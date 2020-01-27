/**
 * Garoon JavaScript、SOAP APIを使ったサンプルプログラム
 *
 * 「wf_to_sch.js」ファイル
 *
 * Copyright (c) 2018 Cybozu
 *
 * Licensed under the MIT License
 */
jQuery.noConflict();
(function($) {
    'use strict';

    /**
     * 共通SOAPコンテンツ
     * ${XXXX}の箇所は実施処理等に合わせて置換して使用
     */
    var SOAP_TEMPLATE =
        '<?xml version="1.0" encoding="UTF-8"?>' +
         '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">' +
          '<soap:Header>' +
           '<Action>${ACTION}</Action>' +
           '<Timestamp>' +
            '<Created>${CREATED}</Created>' +
            '<Expires>2037-08-12T14:45:00Z</Expires>' +
           '</Timestamp>' +
           '<Locale>jp</Locale>' +
          '</soap:Header>' +
          '<soap:Body>' +
           '<${ACTION}>' +
            '<parameters>${PARAMETERS}</parameters>' +
           '</${ACTION}>' +
          '</soap:Body>' +
         '</soap:Envelope>';

    /**
     * スケジュール登録パラメータテンプレート
     * ${XXXX}の箇所は入力値等で置換して使用
     */
    var SCH_ADD_TEMPLATE =
        '<request_token>${REQUEST_TOKEN}</request_token>' +
         '<schedule_event xmlns="" id="dummy" event_type="normal" pubic_type="${SCOPE}" version="dummy" ' +
                        'plan="${MENU}" detail="${TITLE}" description="${MEMO}" ' +
                        'timezone="Asia/Tokyo" end_timezone="Asia/Tokyo" allday="false" start_only="false">' +
          '<members>' +
           '<member>' +
            '<user id="${USER_ID}"></user>' +
           '</member>' +
          '</members>' +
          '<when>' +
           '<datetime start="${START_TIME}" end="${END_TIME}"></datetime>' +
          '</when>' +
         '</schedule_event>';

    // 文字列をHTMLエスケープ
    var escapeHtml = function(str) {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    };

    // リクエストトークン取得
    var getRequestToken = function() {
        var defer = $.Deferred();

        // リクエストトークンの取得
        var tokenRequest = SOAP_TEMPLATE;
        tokenRequest = tokenRequest.replace('${PARAMETERS}', '');
        tokenRequest = tokenRequest.split('${ACTION}').join('UtilGetRequestToken');
        tokenRequest = tokenRequest.replace('${CREATED}', moment().add(-9, 'hours').format('YYYY-MM-DDTHH:mm:ssZ'));
        $.ajax({
            type: 'post',
            url: '/g/util_api/util/api.csp',
            cache: false,
            async: false,
            data: tokenRequest
        })
            .then(function(respForToken) {
                defer.resolve($(respForToken).find('request_token').text());
            });
        // 本来はエラー処理を実施

        return defer.promise();
    };

    // 指定のユーザ名に対応するユーザIDを取得する
    var getApplicantId = function(userNm) {
        var defer = $.Deferred();

        // 申請者情報（申請者のID）の取得
        var applicantRequest = SOAP_TEMPLATE;
        applicantRequest = applicantRequest.replace('${PARAMETERS}', '<login_name>' + userNm + '</login_name>');
        applicantRequest = applicantRequest.split('${ACTION}').join('BaseGetUsersByLoginName');
        applicantRequest = applicantRequest.replace(
            '${CREATED}', moment().add(-9, 'hours').format('YYYY-MM-DDTHH:mm:ssZ'));

        $.ajax({
            type: 'post',
            url: '/g/cbpapi/base/api.csp',
            cache: false,
            async: false,
            data: applicantRequest
        })
            .then(function(respForApplicant) {
                defer.resolve($(respForApplicant).find('user').attr('key'));
            });
        // 本来はエラー処理を実施

        return defer.promise();
    };

    // ワークフロー承認イベントで起動する
    // 申請内容をスケジュールに登録する
    garoon.events.on('workflow.request.approve.submit.success', function(event) {
        // 申請内容を取得する
        var request = event.request;

        return getRequestToken().then(function(requestToken) {
            // 申請者のユーザ名をSOAPで処理できるID形式に変換
            return getApplicantId(request.applicant.code).then(function(applicantId) {
                // スケジュールSOAP API固有のパラメータを設定
                var schAddParam = SCH_ADD_TEMPLATE;

                schAddParam = schAddParam.replace('${REQUEST_TOKEN}', escapeHtml(requestToken));
                schAddParam = schAddParam.replace('${MENU}', request.items.Menu.value); // 予定メニュー
                schAddParam = schAddParam.replace('${TITLE}', request.items.Title.value); // タイトル

                // メモ欄には申請へのURLを付加
                var url = location.protocol + '//' + location.hostname +
                    '/g/workflow/view.csp?pid=' + request.id +
                    '&amp;fid=' + request.folders[request.folders.length - 1].id + '&#xA;';
                // 改行の変換
                schAddParam = schAddParam.replace('${MEMO}', url + request.items.Memo.value.split('\n').join('&#xA;'));

                var startTime = moment(request.items.From.value.date + 'T' + request.items.From.value.time + ':00');
                schAddParam = schAddParam.replace(
                    '${START_TIME}', startTime.add(-9, 'hours').format('YYYY-MM-DDTHH:mm:ssZ')); // 開始日時（UTC対応）
                var endTime = moment(request.items.To.value.date + 'T' + request.items.To.value.time + ':00');
                schAddParam = schAddParam.replace(
                    '${END_TIME}', endTime.add(-9, 'hours').format('YYYY-MM-DDTHH:mm:ssZ')); // 終了日時（UTC対応）

                schAddParam = schAddParam.replace('${USER_ID}', applicantId); // 申請者

                // 公開方法は、公開⇒public、非公開⇒privateに変換
                var scope;
                if (request.items.Scope.value === '公開') {
                    scope = 'public';
                } else if (request.items.Scope.value === '非公開') {
                    scope = 'private';
                }

                schAddParam = schAddParam.replace('${SCOPE}', scope);

                var schAddRequest = SOAP_TEMPLATE;
                // SOAPパラメータを完成させる
                schAddRequest = schAddRequest.replace('${PARAMETERS}', schAddParam);
                // 実行処理を指定
                schAddRequest = schAddRequest.split('${ACTION}').join('ScheduleAddEvents');
                schAddRequest = schAddRequest.replace(
                    '${CREATED}', moment().add(-9, 'hours').format('YYYY-MM-DDTHH:mm:ssZ'));

                // スケジュール登録の実行
                $.ajax({
                    type: 'post',
                    url: '/g/cbpapi/schedule/api.csp',
                    cache: false,
                    async: false,
                    data: schAddRequest
                });
                // 本来はエラー処理を実施
            });
        });
    });
})(jQuery);