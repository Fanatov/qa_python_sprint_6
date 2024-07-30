# URL Тестовой страницы
BASE_URL = "https://stellarburgers.nomoreparties.site/"
# URL Ленты приготовлений
FEED_URL = "https://stellarburgers.nomoreparties.site/feed"
# URL Профиля аккаунта
PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"
# URL Страницы входа в аккаунт
ACCOUNT_URL = "https://stellarburgers.nomoreparties.site/login"
# URL Регистрации нового аккаунта
REGISTER_URL = "https://stellarburgers.nomoreparties.site/register"
# URL Страницы восстановления пароля
FORGOT_PASSWORD_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
# Логотип вверху страницы
LOGO_MAIN_PAGE = "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"
# Основной тайтл главного экрана
MAIN_PAGE_TITLE = "//h1[contains(text(),'Соберите бургер')]"
# Кнопка регистрации
REGISTER_BUTTON = "//button[.='Зарегистрироваться']"
# Кнопка войти
LOGIN_BUTTON = "//*[contains(text(),'Войти')]"
# Кнопка входа в аккаунт на главной странице
LOGIN_INTO_ACCOUNT_BUTTON = "//button[contains(text(),'Войти в аккаунт')]"
# Имя пользователя статика
LOGIN_NAME = "alexandervolobuev12000@yandex.ru"
# Пароль пользователя статика
LOGIN_PASSWORD = "etopassword12345"
# Тайтл "вход" на экране логина.
LOGIN_TITLE = "//h2[contains(text(),'Вход')]"
# Тайтл "регистрация" на экране регистрации
REGISTER_TITLE = "//h2[contains(text(),'Регистрация')]"
# Тайтл "восстановление пароля" на экране регистрации
RESTORE_PASSWORD_TITLE = "//h2[contains(text(),'Восстановление пароля')]"
# Кнопка восстановление пароля на экране логина.
RESTORE_PASSWORD_BUTTON = "//a[contains(text(),'Восстановить пароль')]"
# Поле ввода имени пользователя
NAME_FIELD = "input[name='name']"
# Поле ввода пароля пользователя
PASSWORD_FIELD = "input[name='Пароль']"
# Кнопка перехода в личный кабинет
ACCOUNT_PAGE_BUTTON = "//p[contains(text(),'Личный Кабинет')]"
# Кнопка "Конструктор"
BUILDER_BUTTON = "//p[contains(text(),'Конструктор')]"
# Имя в аккаунте
LOGIN_FILL_IN_ACCOUNT = "(//input[contains(@class,'text input__textfield')])[2]"
# Хэдер страницы
PAGE_HEADER = "//header[contains(@class,'AppHeader_header__X9aJA pb-4')]"
# Секция конструктора с доступными ингридиентами
INGRIDIENTS_SECTION = "//section[@class='BurgerIngredients_ingredients__1N8v2']"
# Кнопка "выход"
LOGOUT_BUTTON = "//button[text()='Выход']"
# Кнопка "Булки"
BUNS_BUTTON = "//span[.='Булки']"
# Кнопка "Соусы"
SAUCES_BUTTON = "//span[.='Соусы']"
# Кнопка "Начинки"
FILLINGS_BUTTON = "//span[.='Начинки']"
# Выбранный ингридиент
SELECTED_INGRIDIENT = "//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc')]"
# Поле регистрации "Имя"
REG_FIELD_NAME = "//label[.='Имя']/following-sibling::input"
# Поле регистрации "Email"
REG_FIELD_EMAIL = "//label[.='Email']/following-sibling::input"
# Поле регистрации "Пароль"
REG_FIELD_PASSWORD = "//label[.='Пароль']/following-sibling::input"
# Уведомление некорректных данных при регистрации или попытке повторной регистрации
ALERT_POPUP = "//p[.='Такой пользователь уже существует']"
# Уведомление некорректного пароля при регистрации
ALERT_INCORRECT_PASSWORD = "//p[.='Некорректный пароль']"
