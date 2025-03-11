-- Create the main application database
CREATE DATABASE partner_dashboard_db;

-- Create the test database
CREATE DATABASE test_partner_dashboard_db;

-- Connect to test database and load test data
\c test_partner_dashboard_db;

-- Load the test data
\i /docker-entrypoint-initdb.d/reset_db.sql