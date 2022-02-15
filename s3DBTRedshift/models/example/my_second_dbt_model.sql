
-- Use the `ref` function to select from other models

select city
from {{ ref('sample_customer_data') }}
