from selenium import webdriver

driver = webdriver.Chrome()
driver.set_script_timeout(60)  # таймаут для async скриптов
driver.get = (
    ("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
)
try:
    script = """
    let callback = arguments[0];
    let observer = null;

    function checkAllLoaded() {
        let imgs = Array.from(document.images);
        if (imgs.length >= 4 && imgs.every\
        (img => img.complete && img.naturalWidth > 0)) {
            if (observer) observer.disconnect();  // отключаем observer
            callback(imgs.map(img => img.src));  // вызываем callback
        }
    }

    observer = new MutationObserver(checkAllLoaded);
    observer.observe(document.body, { childList: true, subtree: true });
    checkAllLoaded();  // сразу проверяем
    """

    all_src = driver.execute_async_script(script)

    # Выводим src третьей картинки
    print(all_src[2])

finally:
    driver.quit()  # теперь браузер закроется корректно
