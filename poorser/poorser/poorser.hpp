#include<iostream>
#include<string>

class client {
public:
	client() = default;
	void interact();
	~client() = default;
private:
	std::string menu = "�������� ��������:\n\t1.������� ������ ����������.\n\t2.������ ������ ���������� ������.\n\t3.�������� ������.\n";
	std::string sorts = "�������� ����������:\n\t1.�� ����.\n\t2.�� ������.\n\t3.��������� � ������� ����.\n";
	std::string periods_ = "������� ����� � ������� ��� ������� 0 ��� �������� � ������� ����.\n";

	std::string sort = "";
	uint8_t period = 0;

	void show_data();
};
