-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(200),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(20) REFERENCES customers(customer_id),
	employe_id int REFERENCES employees(employee_id),
	order_date date,
	snipt_city varchar(20)

);