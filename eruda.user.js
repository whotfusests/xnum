// ==UserScript==
// @name         Inject Eruda Console into Body
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Injects Eruda console into every page via body.innerHTML-style script injection
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    const injectScripts = () => {
        const scriptContainer = document.createElement('div');
        scriptContainer.innerHTML = `
            <script src="https://cdn.jsdelivr.net/npm/eruda"><\/script>
            <script>eruda.init();<\/script>
        `;
        document.body.appendChild(scriptContainer);
    };

    if (document.body) {
        injectScripts();
    } else {
        // Wait for the body to load if not yet available
        new MutationObserver((mutations, observer) => {
            if (document.body) {
                injectScripts();
                observer.disconnect();
            }
        }).observe(document.documentElement, { childList: true, subtree: true });
    }
})();
