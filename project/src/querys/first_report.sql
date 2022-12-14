
create or replace view report1 as(
    with table_x as(
    select d.department, j.job, cast(he.datetime as date) date_
    from postgres.public.hired_employees he
    inner join postgres.public.departments d 
        on he.department_id = d.id
    inner join postgres.public.jobs j 
        on he.job_id = j.id
    ), tabla_y as(
    select department
        , job
        , case when cast(to_char(date_, 'YYYYMM')as int) between 202101 and 202103 then 'Q1'
            when cast(to_char(date_, 'YYYYMM')as int) between 202104 and 202106 then 'Q2'
            when cast(to_char(date_, 'YYYYMM')as int) between 202107 and 202109 then 'Q3'
            when cast(to_char(date_, 'YYYYMM')as int) between 202110 and 202112 then 'Q4'
            end Q_
    from table_x
    where extract(year from date_)=2021
    )
    SELECT department, job,
        count((CASE WHEN Q_ = 'Q1' THEN Q_ END)) AS "Q1",
        count((CASE WHEN Q_ = 'Q2' THEN Q_ END)) AS "Q2",
        count((CASE WHEN Q_ = 'Q3' THEN Q_ END)) AS "Q3",
        count((CASE WHEN Q_ = 'Q4' THEN Q_ END)) AS "Q4"
    FROM tabla_y
    GROUP BY department, job
    order by 1,2
);




