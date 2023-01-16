#include<iostream>
#include<string>

class client {
public:
	client() = default;
	void interact();
	~client() = default;
private:
	std::string menu = "Выберите действие:\n\t1.Выбрать способ сортировки.\n\t2.Задать период обновления данных.\n\t3.Получить данные.\n";
	std::string sorts = "Выберите сортировку:\n\t1.По цене.\n\t2.По скидке.\n\t3.Вернуться в главное меню.\n";
	std::string periods_ = "Введите время в минутах или введите 0 для возврата в главное меню.\n";

	std::string sort = "";
	uint8_t period = 0;

	void show_data();
};
