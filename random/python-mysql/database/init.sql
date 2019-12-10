DROP TABLE IF EXISTS `Users`;
CREATE TABLE Users (
    emp_id int,
    employee_name varchar(255)
);

INSERT INTO Users (emp_id, employee_name) 
VALUES (1, "Keith White"),
       (2, "Emma Mullen");