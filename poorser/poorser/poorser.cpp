#include<poorser/poorser.hpp>
#include<windows.h>

void client::interact() {
	std::wstring menu_ = L"Выберите действие:\n\t1.Выбрать способ сортировки.\n\t2.Задать период обновления данных.\n\t3.Получить данные.";
	std::wstring sorts_ = L"Выберите сортировку:\n\t1.По цене.\n\t2.По скидке.\n\t3.Вернуться в главное меню.";
	std::wstring periods_ = L"Введите время в минутах или введите 0 для возврата в главное меню.";
	std::wstring error_ = L"Введите корректные данные";
	std::wstring intro_ = L"====poorser_demo ver.01.22====\n";
	std::string interaction = "";

	std::wcout << intro_<< menu_<<std::endl;
	std::cin >> interaction;
	while (interaction != "3") {
		if (interaction != "1" && interaction != "2") {
			std::wcout << error_ << std::endl;
		}
		else {
			if (interaction == "1") {
				std::wcout << sorts_ << std::endl;
				std::cin >> interaction;
				while (interaction != "1" && interaction != "2" && interaction != "3") {
					std::wcout << error_ << std::endl;
					std::cin >> interaction;
				}
				if (interaction == "3") {
					std::wcout << L"Без изменений.\n" << std::endl;
				}
				else {
					this->sort = interaction;
					std::wcout << L"Установлено.\n" << std::endl;
				}
			}
			else {
				std::wcout << periods_ << std::endl;
				std::cin >> interaction;
				while ([&interaction]()->bool
					{auto it = interaction.begin();
					while (it != interaction.end() && std::isdigit(*it)) it++;
					return interaction.empty() || it != interaction.end(); }() || (interaction[0] == '0'&& interaction.length()!=1)) {
					std::wcout << error_ << std::endl;
					std::cin >> interaction;
				}
				int per = std::atoi(interaction.c_str());
				if (per == 0) {
					std::wcout << L"Без изменений.\n" << std::endl;
				}
				else {
					this->period = per;
					std::wcout << L"Установлено.\n" << std::endl;
				}
			}
		}
		std::wcout << menu_ << std::endl;
		std::cin >> interaction;
	}
	if (period == 0) {
		show_data();
	}
	else {
		while (true) {
			show_data();
			Sleep(period * 60 * 1000 + std::rand() % 20000);
		}
	}
}

void client::show_data() {
	std::system("python get_ids.py");
	std::system("python get_products.py");
	std::system("python get_prices.py");

	std::system("python sort.py");
	if (sort != "") {
		sort = "python sort" + sort + ".py";
		std::system(sort.c_str());
	}

	std::system("python show.py");
}


/*while (std::cin >> interaction) {
		if (interaction == "1") {
			std::cout << sorts;
			std::string interaction_sort;
			std::cin >> interaction_sort;
			if (interaction_sort == "3") {
				std::cout << "Без изменений.\n" << menu;
			}
			else {
				sort = interaction_sort;
				std::cout << "Установлено.\n" << menu;
			}
		}
		if (interaction == "2") {
			std::cout << periods_;
			int interaction_per;
			std::cin >> interaction_per;
			if (interaction_per == 0) {
				std::cout << "Без изменений.\n" << menu;
			}
			else {
				period = interaction_per;
				std::cout << "Установлено.\n" << menu;
			}
		}
		if (interaction == "3") {
			if (period == 0) {
				show_data();
				std::cout << menu;
			}
			else {
				while (true) {
					show_data();
					Sleep(period * 60 * 1000 + std::rand() % 20000);
				}
			}
		}
	}*/

/*
std::string menu_ = "Выберите действие:\n\t1.Выбрать способ сортировки.\n\t2.Задать период обновления данных.\n\t3.Получить данные.\n";
std::string sorts_ = "Выберите сортировку:\n\t1.По цене.\n\t2.По скидке.\n\t3.Вернуться в главное меню.\n";
std::string periods_ = "Введите время в минутах или введите 0 для возврата в главное меню.\n";
std::string error_ = "Введите корректные данные\n";
std::string intro_ = "====poorser_demo ver.01.22====\n";*/