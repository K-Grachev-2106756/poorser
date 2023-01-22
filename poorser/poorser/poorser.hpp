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
	std::string sort = "";
	uint8_t period = 0;
	/**
	 * ����� ������ Client, ������� ���������� ��� ��������� ���������� ������
	 */
	void show_data();
};
