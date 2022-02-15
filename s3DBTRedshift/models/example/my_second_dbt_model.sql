
-- Use the `ref` function to select from other models

select *
from {{ ref('sample_customer_data') }}
where city == "Orleans"
