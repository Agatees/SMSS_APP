create database application_database; 
use application_database;


show tables;  
create table user_credentials
(
customer_id varchar(10),
username varchar(20),
password varchar(64),
phoneno varchar(10),
email_id varchar(50),
joindate varchar(20)
);
select * from user_credentials;
truncate table user_credentials;
drop table user_credentials;


create table user_data
(
customer_id varchar(10),
username varchar(30),
first_name varchar(20),
last_name varchar(20),
dob date,
email_id varchar(40),
phone varchar(10),
zip_code varchar(10),
timestamp varchar(20)
);
select * from user_data;
truncate table user_data;
drop table user_data;

create table user_address
(
customer_id varchar(10),
door_no varchar(5),
street varchar(50),
city varchar(30),
state varchar(20),
country varchar(30),
zip_code varchar(10),
timestamp varchar(20)
);
select * from user_address;
truncate table user_address;
drop table user_address;


create table bank
(
s_no integer,
bank_name varchar(30)
);
select * from bank;
truncate table bank;
drop table bank;

create table service_requests
(
customer_id varchar(10),
service_id varchar(10),
device_type varchar(50),
model varchar(40),
defect varchar(205),
usaage varchar (10),
repair_status varchar(11),
time varchar(20) ,
price int,
payment_status varchar(10)
);
select * from service_requests;
truncate table service_requests;
drop table service_requests;

create table services
(
service_id varchar(10) primary key,
serviced_by varchar (20),
service_date date, 
service_status varchar(12),
price int,
payment_status varchar(10),
time varchar(20) not null
);
select * from services;
truncate table services;
ALTER TABLE services
CHANGE servie_date service_date date;

drop table services;


-- "Service_Id, Device_category, Model_Name, Defect_description, Usage, Time "
-- Select user_data.customer_id, user_data.username, user_data.first_name, user_data.last_name, user_data.dob, user_data.email_id, user_data.phone, user_address.door_no, user_address.street, user_address.city, user_address.state, user_address.country, user_address.zip_code from user_data, user_address  where user_data.customer_id ='CUSAG90800' and user_address.customer_id = 'CUSAG90800' and user_data.customer_id = user_address.customer_id ;
select services.service_id, service_requests.device_type, service_requests.defect, services.service_date from services, service_requests where services.service_status = 'Initiated' and services.service_id = service_requests.service_id;
select service_id, device_type, model, defect, usaage, time from service_requests where  service_id = %s ;