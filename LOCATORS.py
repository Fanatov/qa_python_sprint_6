class Locators:
    # URL Тестовой страницы
    BASE_URL = f"https://stellarburgers.nomoreparties.site/"
    # URL Ленты приготовлений
    FEED_URL = f"https://stellarburgers.nomoreparties.site/feed"
    # URL Профиля аккаунта
    PROFILE_URL = f"https://stellarburgers.nomoreparties.site/account/profile"
    # URL Страницы входа в аккаунт
    ACCOUNT_URL = f"https://stellarburgers.nomoreparties.site/login"
    # URL Регистрации нового аккаунта
    REGISTER_URL = f"https://stellarburgers.nomoreparties.site/register"
    # URL Страницы восстановления пароля
    FORGOT_PASSWORD_URL = f"https://stellarburgers.nomoreparties.site/forgot-password"
    # Логотип вверху страницы
    LOGO_MAIN_PAGE = f"//div[contains(@class,'AppHeader_header__logo')]"
    # Основной тайтл главного экрана
    MAIN_PAGE_TITLE = f"//h1[contains(text(),'Соберите бургер')]"
    # Кнопка регистрации
    REGISTER_BUTTON = f"//button[.='Зарегистрироваться']"
    # Кнопка войти
    LOGIN_BUTTON = f"//*[contains(text(),'Войти')]"
    # Кнопка входа в аккаунт на главной странице
    LOGIN_INTO_ACCOUNT_BUTTON = f"//button[contains(text(),'Войти в аккаунт')]"
    # Тайтл "вход" на экране логина.
    LOGIN_TITLE = f"//h2[contains(text(),'Вход')]"
    # Тайтл "регистрация" на экране регистрации
    REGISTER_TITLE = f"//h2[contains(text(),'Регистрация')]"
    # Тайтл "восстановление пароля" на экране регистрации
    RESTORE_PASSWORD_TITLE = f"//h2[contains(text(),'Восстановление пароля')]"
    # Кнопка восстановление пароля на экране логина.
    RESTORE_PASSWORD_BUTTON = f"//a[contains(text(),'Восстановить пароль')]"
    # Поле ввода имени пользователя
    NAME_FIELD = f"//input[@name='name']"
    # Поле ввода пароля пользователя
    PASSWORD_FIELD = f"//input[@name='Пароль']"
    # Кнопка перехода в личный кабинет
    ACCOUNT_PAGE_BUTTON = f"//p[contains(text(),'Личный Кабинет')]"
    # Кнопка "Конструктор"
    BUILDER_BUTTON = f"//p[contains(text(),'Конструктор')]"
    # Имя в аккаунте
    LOGIN_FILL_IN_ACCOUNT = f"(//input[contains(@class,'text input__textfield')])[2]"
    # Хэдер страницы
    PAGE_HEADER = f"//header[contains(@class,'AppHeader_header')]"
    # Секция конструктора с доступными ингридиентами
    INGRIDIENTS_SECTION = f"//section[contains(@class,'BurgerIngredients_ingredients_')]"
    # Кнопка "выход"
    LOGOUT_BUTTON = f"//button[text()='Выход']"
    # Кнопка "Булки"
    BUNS_BUTTON = f"//span[.='Булки']"
    # Кнопка "Соусы"
    SAUCES_BUTTON = f"//span[.='Соусы']"
    # Кнопка "Начинки"
    FILLINGS_BUTTON = f"//span[.='Начинки']"
    # Выбранный ингридиент
    SELECTED_INGRIDIENT = f"//div[contains(@class,'tab_tab_type_current')]"
    # Поле регистрации "Имя"
    REG_FIELD_NAME = f"//label[.='Имя']/following-sibling::input"
    # Поле регистрации "Email"
    REG_FIELD_EMAIL = f"//label[.='Email']/following-sibling::input"
    # Поле регистрации "Пароль"
    REG_FIELD_PASSWORD = f"//label[.='Пароль']/following-sibling::input"
    # Уведомление некорректных данных при регистрации или попытке повторной регистрации
    ALERT_POPUP = f"//p[.='Такой пользователь уже существует']"
    # Уведомление некорректного пароля при регистрации
    ALERT_INCORRECT_PASSWORD = f"//p[.='Некорректный пароль']"


class StaticData:
    # Имя пользователя статика
    LOGIN_NAME = f"alexandervolobuev12000@yandex.ru"
    # Пароль пользователя статика
    LOGIN_PASSWORD = f"etopassword12345"
    # Статика текст "булки"
    BUNS = f"Булки"
    # Статика текст "начинки"
    FILLINGS = f"Начинки"
    # Статика текст "соусы"
    SAUCES = f"Соусы"
