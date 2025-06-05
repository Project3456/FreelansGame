Freelancer Status Tracker / Трекер статуса фрилансера
Description / Описание

A simple Python script to track a freelancer's status including budget, available time and current orders.
Простой Python-скрипт для отслеживания статуса фрилансера, включая бюджет, доступное время и текущие заказы.
Features / Функционал

    Create freelancer profile with:
    Создание профиля фрилансера с указанием:

        Name / Имени

        Budget (in dollars) / Бюджета (в долларах)

        Available time (in hours) / Доступного времени (в часах)

        Current orders list / Списка текущих заказов

    Display current freelancer status in readable format
    Отображение текущего статуса в удобном формате

Installation / Установка

    Make sure you have Python (3.x) installed
    Убедитесь, что у вас установлен Python (версии 3.x)

    Clone repository or download freelancer.py file
    Клонируйте репозиторий или скачайте файл freelancer.py

    Run the script: python freelancer.py
    Запустите скрипт: python freelancer.py

Usage Example / Пример использования
python

# Create freelancer instance / Создание экземпляра фрилансера
freelancer = Freelancer("Ivan", 1000, 40, {"webdev": 5})
print(freelancer.show_status())

Contributing / Участие

Pull requests are welcome. For major changes, please open an issue first.
Приветствуются pull requests. Для существенных изменений сначала откройте issue.
