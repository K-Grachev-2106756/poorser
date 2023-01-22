#include<iostream>
#include<string>


/**
 * �����, ������������� �������������
 * ��� �������������� � �������������
 * ����������� ���������, ��� ������
 * ���� ������������� ������ � � �����
 * �������������� ��� ������ ����������
 * � �������
 */
class client {
public:
	/**
	 * ������������� �����������
	 */
	client() = default;
	/**
	 * ����� ������ Client, ������� ������������
	 * ���������������� �������������� � �������������
	 * � ������������� ��� ������ � ��� ����, �
	 * ������� �� ����� �� ������.
	 */
	void interact();
	/**
	 * ������������� ����������
	 */
	~client() = default;

private:
	std::string menu_ = "�������� ��������:\n\t1.������� ������ ����������.\n\t2.������ ������ ���������� ������.\n\t3.�������� ������.\n";
	std::string sorts_ = "�������� ����������:\n\t1.�� ����.\n\t2.�� ������.\n\t3.��������� � ������� ����.\n";
	std::string periods_ = "������� ����� � ������� ��� ������� 0 ��� �������� � ������� ����.\n";
	std::string error_ = "������� ���������� ������\n";
	std::string sort = "";
	uint8_t period = 0;
	/**
	 * ����� ������ Client, ������� ���������� ��� ��������� ���������� ������
	 */
	void show_data();
};
