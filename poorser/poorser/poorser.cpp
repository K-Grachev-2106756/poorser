#include<poorser/poorser.hpp>
#include<windows.h>


void client::interact() {
	std::cout << "====poorser_demo ver.01.22====\n" << menu_;
	std::string interaction = "";
	std::cin >> interaction;
	while (interaction != "3") {
		if (interaction != "1" && interaction != "2") {
			std::cout << error_;
		}
		else {
			if (interaction == "1") {
				std::cout << sorts_;
				std::cin >> interaction;
				while (interaction != "1" && interaction != "2" && interaction != "3") {
					std::cout << error_;
					std::cin >> interaction;
				}
				if (interaction == "3") {
					std::cout << "Без изменений.\n";
				}
				else {
					this->sort = interaction;
					std::cout << "Установлено.\n";
				}
			}
			else {
				std::cout << periods_;
				std::cin >> interaction;
				while ([&interaction]()->bool
					{auto it = interaction.begin();
					while (it != interaction.end() && std::isdigit(*it)) it++;
					return interaction.empty() || it != interaction.end(); }() || interaction[0] == '0') {
					std::cout << error_;
					std::cin >> interaction;
				}
				int per = std::atoi(interaction.c_str());
				if (per == 0) {
					std::cout << "Без изменений.\n";
				}
				else {
					this->period = per;
					std::cout << "Установлено.\n";
				}
			}
		}
		std::cout << menu_;
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