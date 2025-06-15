# Write your MySQL query statement below
SELECT
	name
FROM
	SalesPerson
WHERE
	sales_id NOT IN (
	SELECT
		sales_id
	FROM
		Company com,
		orders ord
	WHERE
		com.com_id = ord.com_id
		AND com.name = 'RED')