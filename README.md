### Install required plugins run:  
```commandline
pip install -r requirements.txt
```

### Allure install (local)
In order to serve allure html report, java installation is required.
```commandline
java --version
```
Please follow official allure installation [guide](https://docs.qameta.io/allure/#_installing_a_commandline).  
```commandline
allure --version
```
#### Generate report:  
After allure is installed, follow allure-pytest [usage](https://docs.qameta.io/allure/#_pytest).
```commandline
pytest ./suite_tests --alluredir=alluredir
allure serve alluredir
```