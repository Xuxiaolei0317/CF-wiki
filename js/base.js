/**
 * 从URL中获取搜索词
 * @returns {string} 搜索词
 */
function getSearchTerm() {
    // 获取URL中的查询字符串部分，并去除开头的问号
    var sPageURL = window.location.search.substring(1);
    // 将查询字符串按&符号分割成数组
    var sURLVariables = sPageURL.split('&');
    // 遍历数组中的每个参数
    for (var i = 0; i < sURLVariables.length; i++) {
        // 将每个参数按=符号分割成数组
        var sParameterName = sURLVariables[i].split('=');
        // 如果参数名是q，则返回参数值
        if (sParameterName[0] == 'q') {
            return sParameterName[1];
        }
    }
}

/**
 * 应用顶部填充
 * 此函数用于更新各种绝对位置，以匹配主容器的起始位置。
 * 这对于处理多行导航头是必要的，因为这会将主容器向下推。
 */
function applyTopPadding() {
    // 获取body下的第一个.container元素的偏移量
    var offset = $('body > .container').offset();
    // 设置html元素的scroll-padding-top属性，以确保滚动时内容不会被导航栏遮挡
    $('html').css('scroll-padding-top', offset.top + 'px');
    // 设置侧边栏的顶部位置，使其与主容器对齐
    $('.bs-sidebar.affix').css('top', offset.top + 'px');
}

/**
 * 文档就绪事件处理函数
 * 当文档加载完成后，执行一系列初始化操作。
 */
$(document).ready(function() {

    // 应用顶部填充
    applyTopPadding();

    // 获取搜索词
    var search_term = getSearchTerm(),
        // 获取搜索模态框元素
        $search_modal = $('#mkdocs_search_modal'),
        // 获取键盘模态框元素
        $keyboard_modal = $('#mkdocs_keyboard_modal');

    // 如果存在搜索词，则显示搜索模态框
    if (search_term) {
        $search_modal.modal();
    }

    // 确保搜索输入框在模态框每次打开时自动获得焦点
    $search_modal.on('shown.bs.modal', function() {
        $search_modal.find('#mkdocs-search-query').focus();
    });

    // 当点击搜索结果中的链接时，关闭搜索模态框
    // 由于链接是后来添加的，所以监听父元素
    $('#mkdocs-search-results').click(function(e) {
        if ($(e.target).is('a')) {
            $search_modal.modal('hide');
        }
    });

    // 填充键盘模态框中的快捷键信息
    $keyboard_modal.find('.help.shortcut kbd')[0].innerHTML = keyCodes[shortcuts.help];
    $keyboard_modal.find('.prev.shortcut kbd')[0].innerHTML = keyCodes[shortcuts.previous];
    $keyboard_modal.find('.next.shortcut kbd')[0].innerHTML = keyCodes[shortcuts.next];
    $keyboard_modal.find('.search.shortcut kbd')[0].innerHTML = keyCodes[shortcuts.search];

    // 键盘导航
    document.addEventListener("keydown", function(e) {
        // 如果当前焦点在输入框中，则不处理键盘事件
        if ($(e.target).is(':input')) return true;
        // 获取按下的键的键码
        var key = e.which || e.keyCode || window.event && window.event.keyCode;
        var page;
        // 根据按下的键执行相应的操作
        switch (key) {
            case shortcuts.next:
                // 获取下一页的链接
                page = $('.navbar a[rel="next"]:first').prop('href');
                break;
            case shortcuts.previous:
                // 获取上一页的链接
                page = $('.navbar a[rel="prev"]:first').prop('href');
                break;
            case shortcuts.search:
                // 阻止默认行为
                e.preventDefault();
                // 隐藏键盘模态框
                $keyboard_modal.modal('hide');
                // 显示搜索模态框并聚焦搜索输入框
                $search_modal.modal('show');
                $search_modal.find('#mkdocs-search-query').focus();
                break;
            case shortcuts.help:
                // 隐藏搜索模态框
                $search_modal.modal('hide');
                // 显示键盘模态框
                $keyboard_modal.modal('show');
                break;
            default: break;
        }
        // 如果存在下一页或上一页的链接，则跳转到相应页面
        if (page) {
            $keyboard_modal.modal('hide');
            window.location.href = page;
        }
    });

    // 为表格添加样式
    $('table').addClass('table table-striped table-hover');

    // 改善滚动监听行为，确保点击目录项时正确高亮显示
    $(".bs-sidenav a").on("click", function() {
        var clicked = this;
        setTimeout(function() {
            var active = $('.nav li.active a');
            active = active[active.length - 1];
            if (clicked !== active) {
                $(active).parent().removeClass("active");
                $(clicked).parent().addClass("active");
            }
        }, 50);
    });

    /**
     * 显示内部下拉菜单
     * @param {HTMLElement} item - 触发下拉菜单显示的元素
     */
    function showInnerDropdown(item) {
        // 获取下拉菜单元素
        var popup = $(item).next('.dropdown-menu');
        // 添加显示类
        popup.addClass('show');
        // 添加打开类
        $(item).addClass('open');

        // 首先，关闭任何兄弟下拉菜单
        var container = $(item).parent().parent();
        container.find('> .dropdown-submenu > a').each(function(i, el) {
            if (el !== item) {
                hideInnerDropdown(el);
            }
        });

        // 设置下拉菜单的位置
        var popupMargin = 10;
        var maxBottom = $(window).height() - popupMargin;
        var bounds = item.getBoundingClientRect();

        popup.css('left', bounds.right + 'px');
        if (bounds.top + popup.height() > maxBottom &&
            bounds.top > $(window).height() / 2) {
            popup.css({
                'top': (bounds.bottom - popup.height()) + 'px',
                'max-height': (bounds.bottom - popupMargin) + 'px',
            });
        } else {
            popup.css({
                'top': bounds.top + 'px',
                'max-height': (maxBottom - bounds.top) + 'px',
            });
        }
    }

    /**
     * 隐藏内部下拉菜单
     * @param {HTMLElement} item - 触发下拉菜单隐藏的元素
     */
    function hideInnerDropdown(item) {
        // 获取下拉菜单元素
        var popup = $(item).next('.dropdown-menu');
        // 移除显示类
        popup.removeClass('show');
        // 移除打开类
        $(item).removeClass('open');

        // 重置下拉菜单的滚动位置
        popup.scrollTop(0);
        popup.find('.dropdown-menu').scrollTop(0).removeClass('show');
        popup.find('.dropdown-submenu > a').removeClass('open');
    }

    // 处理下拉菜单的点击事件
    $('.dropdown-submenu > a').on('click', function(e) {
        if ($(this).next('.dropdown-menu').hasClass('show')) {
            hideInnerDropdown(this);
        } else {
            showInnerDropdown(this);
        }

        // 阻止事件冒泡和默认行为
        e.stopPropagation();
        e.preventDefault();
    });

    // 在下拉菜单隐藏时，重置相关状态
    $('.dropdown-menu').parent().on('hide.bs.dropdown', function(e) {
        $(this).find('.dropdown-menu').scrollTop(0);
        $(this).find('.dropdown-submenu > a').removeClass('open');
        $(this).find('.dropdown-menu .dropdown-menu').removeClass('show');
    });
});

// 在窗口调整大小时，重新应用顶部填充
$(window).on('resize', applyTopPadding);

// 启用滚动监听，根据滚动位置高亮显示侧边栏导航项
$('body').scrollspy({
    target: '.bs-sidebar',
    offset: 100
});

/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});


// See https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes
// We only list common keys below. Obscure keys are omitted and their use is discouraged.
var keyCodes = {
    8: 'backspace',
    9: 'tab',
    13: 'enter',
    16: 'shift',
    17: 'ctrl',
    18: 'alt',
    19: 'pause/break',
    20: 'caps lock',
    27: 'escape',
    32: 'spacebar',
    33: 'page up',
    34: 'page down',
    35: 'end',
    36: 'home',
    37: '&larr;',
    38: '&uarr;',
    39: '&rarr;',
    40: '&darr;',
    45: 'insert',
    46: 'delete',
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    65: 'a',
    66: 'b',
    67: 'c',
    68: 'd',
    69: 'e',
    70: 'f',
    71: 'g',
    72: 'h',
    73: 'i',
    74: 'j',
    75: 'k',
    76: 'l',
    77: 'm',
    78: 'n',
    79: 'o',
    80: 'p',
    81: 'q',
    82: 'r',
    83: 's',
    84: 't',
    85: 'u',
    86: 'v',
    87: 'w',
    88: 'x',
    89: 'y',
    90: 'z',
    91: 'Left Windows Key / Left ⌘',
    92: 'Right Windows Key',
    93: 'Windows Menu / Right ⌘',
    96: 'numpad 0',
    97: 'numpad 1',
    98: 'numpad 2',
    99: 'numpad 3',
    100: 'numpad 4',
    101: 'numpad 5',
    102: 'numpad 6',
    103: 'numpad 7',
    104: 'numpad 8',
    105: 'numpad 9',
    106: 'multiply',
    107: 'add',
    109: 'subtract',
    110: 'decimal point',
    111: 'divide',
    112: 'f1',
    113: 'f2',
    114: 'f3',
    115: 'f4',
    116: 'f5',
    117: 'f6',
    118: 'f7',
    119: 'f8',
    120: 'f9',
    121: 'f10',
    122: 'f11',
    123: 'f12',
    124: 'f13',
    125: 'f14',
    126: 'f15',
    127: 'f16',
    128: 'f17',
    129: 'f18',
    130: 'f19',
    131: 'f20',
    132: 'f21',
    133: 'f22',
    134: 'f23',
    135: 'f24',
    144: 'num lock',
    145: 'scroll lock',
    186: '&semi;',
    187: '&equals;',
    188: '&comma;',
    189: '&hyphen;',
    190: '&period;',
    191: '&quest;',
    192: '&grave;',
    219: '&lsqb;',
    220: '&bsol;',
    221: '&rsqb;',
    222: '&apos;',
};
