/**
 * Created by gua on 7/11/16 4:28:01
 */

// log
var log = function () {
    console.log(arguments);
};

// form
var formFromKeys = function(keys, prefix) {
    var form = {};
    for(var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var tagid = prefix + key;
        var value = $('#' + tagid).val();
        if (value.length < 1) {
            // alert('字段不能为空');
            break;
        }
        form[key] = value;
    }
    return form;
};

// vip API
var vip = {
//  data:{}
};

vip.ajax = function(url, method, form, response) {
    var request = {
        url: url,
        type: method,
        contentType: 'application/json',
        success: function (r) {
            log('vip post success', url, r);
            response(r);
        },
        error: function (err) {
            r = {
                success: false,
                message: '我们自行生成的网络错误',
                data: err
            };
            log('vip post err', url, err);
            response(r);
        }
    };
    if(method == 'post') {
        var data = JSON.stringify(form);
        request.data = data;
    }
    $.ajax(request);
};

vip.get = function(url, response) {
    var method = 'get';
    var form = {};
    this.ajax(url, method, form, response);
};

vip.post = function(url, form, response) {
    var method = 'post';
    this.ajax(url, method, form, response);
};

// API products
vip.products = function(response) {
    var api = this;
    var path = '/api/products';
    api.get(path, response);
// 自己写 ajax 调用
//    var request = {
//        url: path,
//        type: 'get',
//        success: function(r){
//        },
//        error:function(r) {
//        }
//    };
//    $.ajax(request);
};

vip.product_delete = function(product_id, response) {
    var path = '/api/products/delete/' + product_id;
    this.get(path, response);
};

// API articles
vip.articles = function(response) {
    var path = '/api/articles';
    this.get(path, response);
};