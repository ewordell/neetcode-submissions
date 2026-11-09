-- Write your query below
select
    p.first_name,
    p.last_name,
    case
        when a.address_id is not null then a.city
        else null
    end as city,
    case when a.address_id is not null then a.state
        else null
    end as state
from
    person p
left join address a on p.person_id = a.person_id
