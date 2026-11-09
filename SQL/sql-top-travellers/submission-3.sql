-- Write your query below
select
    u.name,
    sum(coalesce(r.distance,0)) as travelled_distance
from users u
left join rides r on r.user_id = u.id
group by r.user_id, u.name
order by travelled_distance desc, u.name asc