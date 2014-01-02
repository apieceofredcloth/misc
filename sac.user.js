// ==UserScript==
// @name           Steepandcheap.com (SAC) sort 
// @author         fishsjoy
// @namespace      sac
// @description    Add sort support for sac gear cache.
// @version        0.1
// @include        http://www.steepandcheap.com/gear-cache/*
// ==/UserScript==

var price_rxp = /[0-9\.]+/g;
var $reset = document.querySelector('.collection-facets .reset');

function trim(str) {
    return str.replace(/^\s+|\s+$/g, '');
}

function get_discount(ele) {
    return parseInt(ele.querySelector('.product-discount').innerText)
}

function cmp_discount(a, b) {
    return get_discount(a) - get_discount(b);
}

function get_price(ele) {
    var price = ele.querySelector('.product-price').innerText;
    return parseFloat(price.match(price_rxp)[0])
}

function cmp_price(a, b) {
    return get_price(a) - get_price(b);
}

function sort(sort_type) {
    var goods=[];
    var nodes = document.querySelectorAll('.collection-product:not(.ng-hide)');
    for(var i=0; i<nodes.length; i++){
        goods.push(nodes[i]);
    }
    if( sort_type == 'discount') {
        goods.sort(cmp_discount);
    } else {
        goods.sort(cmp_price);
    }
    for(var i=0; i<goods.length; i++){
        document.querySelector('.collection-products').appendChild(goods[i]);
    }
}

function parseDom(htmlStr) {
    var objE = document.createElement("div");
    objE.innerHTML = htmlStr;
    return objE.childNodes;
}

function init() {
    var sort_ele_str = '<div class="facet order">order'+
        '<button>discount</button><button>price</button>'+
        '</div>';
    var $facet = parseDom(sort_ele_str)[0];
    $facet.addEventListener('click', function() {
        var sort_type = trim(this.innerText);
        sort(sort_type);
    }, false);
    $reset.parentNode.insertBefore($facet, $reset)
}

init();
