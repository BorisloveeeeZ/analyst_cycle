#В списке emails содержатся E-mail адреса пользователей,которые они указали при регистрации на сайте
#Одни адреса содержат символы только в нижнем регистре, другие нет
#Oднако в системе администрирования сайта все адреса должны выводится только маленькими буквами.

emails = ["Anton.Ivanov@example.com", "dima@example.com", "Tema.LeveDEV@example.com"]
lower_emails = map(lambda x: x.lower(), emails )
print(*lower_emails)
