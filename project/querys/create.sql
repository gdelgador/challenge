
DROP TABLE IF EXISTS departments cascade;
DROP TABLE IF EXISTS jobs cascade;
DROP TABLE IF EXISTS hired_employees cascade;


CREATE TABLE departments(
    id int GENERATED BY DEFAULT AS identity primary key,
    department varchar(40) NOT NULL
);

CREATE TABLE jobs(
    id int GENERATED BY DEFAULT AS identity primary key,
    job varchar(40) NOT NULL
);

CREATE TABLE hired_employees (
    id int GENERATED BY DEFAULT AS identity primary key,
    name varchar(40),
    datetime varchar(40),
    department_id integer,
    job_id integer,
    CONSTRAINT fk_departments
      FOREIGN KEY(department_id) 
	  REFERENCES departments(id)
      ON DELETE SET NULL,
    CONSTRAINT fk_jobs
      FOREIGN KEY(job_id) 
	  REFERENCES jobs(id)
      ON DELETE SET NULL
);


