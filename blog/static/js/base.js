function randomHexColor() { //随机生成十六进制颜色
    var hex = Math.floor(Math.random() * 16777216).toString(16); //生成ffffff以内16进制数
    while (hex.length < 6) { //while循环判断hex位数，少于6位前面加0凑够6位
    hex = '0' + hex;
    }
    return '#' + hex; //返回‘#'开头16进制颜色
}
function randomRgbaColor() { //随机生成RGBA颜色
 var r = Math.floor(Math.random() * 256); //随机生成256以内r值
 var g = Math.floor(Math.random() * 256); //随机生成256以内g值
 var b = Math.floor(Math.random() * 256); //随机生成256以内b值
 var alpha = Math.random(); //随机生成1以内a值
 return `rgba(${r},${g},${b},${alpha})`; //返回rgba(r,g,b,a)格式颜色
}
function randomRgbColor() { //随机生成RGB颜色
 var r = Math.floor(Math.random() * 256); //随机生成256以内r值
 var g = Math.floor(Math.random() * 256); //随机生成256以内g值
 var b = Math.floor(Math.random() * 256); //随机生成256以内b值
 return `rgb(${r},${g},${b})`; //返回rgb(r,g,b)格式颜色
}
function onLoginError() {
    alert("你还没登录，不能对文章进行此操作。");
}
function goole_search(){
    window.open("https://www.google.com.hk/search?q="+document.getElementById("searchbar").value, "_search");
}
function bing_search(){
    window.open("https://cn.bing.com/search?q="+document.getElementById("searchbar").value, "_search");
}
function search_user(){
    window.open('/search/user?q='+document.getElementById("searchbar").value, "_self");
}
function search_post(){
    window.open('/search/post?q='+document.getElementById("searchbar").value, "_self");
}
function keyseach(event) {
    if (event.keyCode == 13) {
    search_post();
    }
}
function ajax(options) {
    options = options || {};
    options.type = (options.type || "GET").toUpperCase();
    options.dataType = options.dataType || "json";
    var params = formatParams(options.data);

    //创建 - 非IE6 - 第一步
    if (window.XMLHttpRequest) {
        var xhr = new XMLHttpRequest();
    } else { //IE6及其以下版本浏览器
        var xhr = new ActiveXObject('Microsoft.XMLHTTP');
    }

    //接收 - 第三步
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300) {
                options.success && options.success(xhr.responseText, xhr.responseXML);
            } else {
                options.fail && options.fail(status);
            }
        }
    };

    //连接 和 发送 - 第二步
    if (options.type == "GET") {
        xhr.open("GET", options.url + "?" + params, true);
        xhr.send(null);
    } else if (options.type == "POST") {
        xhr.open("POST", options.url, true);
        //设置表单提交时的内容类型
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send(params);
        }
}

//格式化参数
function formatParams(data) {
    var arr = [];
    for (var name in data) {
        arr.push(encodeURIComponent(name) + "=" + encodeURIComponent(data[name]));
    }
    arr.push(("v=" + Math.random()).replace(".",""));
    return arr.join("&");
}
console.log("%c 意中源码天仙路\t%c从此乃是逍遥人",'color:red;font-size:20px','color:blue;font-size:20px');
console.log("    卤蛋之路提醒你\n代码千万行，避坑第一条。\n爬虫不规范，亲人两行泪。");

function hello() {
    var hour=new Date().getHours();
    if(hour < 6){hello='凌晨好，'}
    else if(hour < 9){hello='早上好，'}
    else if(hour < 12){hello='上午好，'}
    else if(hour < 14){hello='中午好，'}
    else if(hour < 17){hello='下午好，'}
    else if(hour < 19){hello='傍晚好，'}
    else if(hour < 22){hello='晚上好，'}
    else {hello='夜深了，'}
    var webUrl = webUrl;
    document.write(' '+hello);
}

//写cookies

function setCookie(name,value,max_age)
{
    //var Days = 30;
    var exp = new Date();
    //exp.setTime(exp.getTime() + Days*24*60*60*1000);
    exp.setTime(exp.getTime()+ max_age *1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
    return true
}

//读取cookies
function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");

    if(arr=document.cookie.match(reg)){
        return unescape(arr[2]);
    }
    else{
        return null;
    }
}

//删除cookies
function delCookie(name)
{
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval=getCookie(name);
    if(cval!=null){
        document.cookie= name + "="+cval+";expires="+exp.toGMTString();
    }
}