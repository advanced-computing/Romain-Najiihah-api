-- film_permit_db.sql
-- Loads Film_Permits_20260213.csv into a persistent DuckDB database (film_permit.db)

-- Create the film_permits table from the CSV file
CREATE TABLE IF NOT EXISTS film_permits AS
    SELECT *
    FROM read_csv('Film_Permits_20260213.csv');

-- Verify the data was loaded
SELECT COUNT(*) AS total_records FROM film_permits;
