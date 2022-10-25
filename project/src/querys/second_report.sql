create or replace view report2 as(
    with tabla_x as(
        select count(he.id) / count(distinct he.department_id)  avg_count --138
        from hired_employees he 
        where extract(year from cast(he.datetime as date ) ) =2021

    )
    select d.id , d.department , count(*) hired
    from hired_employees he 
    inner join departments d 
        on he.department_id = d.id 
    group by d.id , d.department 
    having   count(*) > (select avg_count from tabla_x)
    order by hired desc
);