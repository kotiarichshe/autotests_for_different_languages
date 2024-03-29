# Checking the launch of autotests for different interface languages.
Autotest of localization of the store's page with the possibility of cross-browser verification of the store's product page.  
The test implements launch capabilities for different user languages by passing the desired language on the command line.
The default language is English.  
```pytest --language=es test_items.py``` - run a test for the product page in Spanish. \
```pytest --language=fr test_items.py``` - run a test for the product page in French.\
In addition, you can perform cross-browser verification for two browsers chrome and firefox.
By default, the test runs in chrome, in order to run the test in firefox, you must enter:  
```pytest --browser_name=firefox test_items.py```  
P.S. If you see a similar message while trying to execute the code:  
```selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.```  
This means that geckodriver is not installed or the path to it is not registered in the system. Repeat the installation steps again.


# Проверка запуска автотестов для разных языков интерфейса.
Автотест локализации страницы магазина с возможностью кроссбраузерной проверки странички товара магизина.  
В тесте реализованы возможности запуска для разных языков пользователей, передавая нужный язык в командной строке.
  По умолчанию установлен английский язык.  
```pytest --language=es test_items.py``` - запустить тест для странички товара на испанском языке.   \
```pytest --language=fr test_items.py``` - запустить тест для странички товара на французском языке.\
Кроме того можно выполнить кроссбраузерную проверку для двух браузеров chrome и firefox.  
По умолчанию тест запускается в chrome, для того чтобы запустить тест в firefox необходимо в командной строке ввести:  
```pytest --browser_name=firefox test_items.py```  
P.S. Если при попытке выполнения кода вы увидели подобное сообщение:  
```selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.```   
Значит, geckodriver не установлен или к нему не прописан путь в системе. Повторите заново действия по установке.
