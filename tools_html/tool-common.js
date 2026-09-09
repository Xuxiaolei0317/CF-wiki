(function () {
    const WIKI_URL = '../Tools/';
    const BUTTON_CLASS = 'wiki-back-button';

    function createBackButton() {
        document.querySelectorAll('#back-button').forEach(function (button) {
            button.remove();
        });

        if (document.querySelector(`.${BUTTON_CLASS}`)) {
            return;
        }

        const link = document.createElement('a');
        link.className = BUTTON_CLASS;
        link.href = WIKI_URL;
        link.textContent = '← 返回 Wiki';
        link.setAttribute('aria-label', '返回 Wiki 工具页');
        document.body.appendChild(link);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createBackButton);
    } else {
        createBackButton();
    }
})();
