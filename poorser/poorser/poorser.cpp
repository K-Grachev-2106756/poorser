#include<poorser/poorser.hpp>
#include<windows.h>


void client::interact() {

	std::cout << "Приветствуем.\n"<<menu;
	std::string interaction = "";
	while (std::cin >> interaction) {
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