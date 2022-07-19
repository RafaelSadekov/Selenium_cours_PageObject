# Selenium Final Project cours PageObject 

Хранилище для итогового проекта по курсу Stepik "**Автоматизация тестирования с помощью Selenium и Python**".

**Для работы использовались**:
* Win 10
* Python 3.10.5
* Google Chrome 103.0.5060.53
* Firefox 102.0

**Дополнительное в коде**:
* Чтобы при добавлении продукта в корзину, тесты могли работать с сылками с "?promo=" и без: в классе "ProductPage", в функции "add_product_button_click", добавлена проверка на наличие "?promo=" в адрессе. Если "?promo=" присутствует, то запускается функция "solve_quiz_and_get_code" из базового класса.
* Изменен код для установки опций в Firefox в файле "conftest.py". Так как в новой версии Selenium, использование устаревших методах (которые приведены в пример в уроках курса) приводит к появлению предупреждения о необходимости использовать новые методы.  

        from selenium.webdriver.firefox.options import Options # for new selenium version
        options = Options() # for new selenium version
        options.set_preference('intl.accept_languages', user_language) # for new selenium version
        browser = webdriver.Firefox(options=options) # for new selenium version
