-- Write your query below
with sales_table as (
    select
        s.seller_name,
        s.seller_id
    from
        seller s
    left join orders o on s.seller_id = o.seller_id
    where extract(year from o.sale_date) = 2020
)


select 
    s.seller_name
from
    seller s
where s.seller_id not in (select seller_id from sales_table)
order by s.seller_name asc