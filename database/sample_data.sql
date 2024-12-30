USE sales_data_pipeline;

INSERT INTO products (product_name, category) VALUES 
    ('Laptop', 'Electronics'), 
    ('Mouse', 'Accessories'),
    ('Keyboard', 'Accessories');

INSERT INTO regions (region_name) VALUES 
    ('North'), 
    ('South'), 
    ('East'), 
    ('West');

INSERT INTO sales (sale_date, product_id, region_id, quantity, price, total)
VALUES 
    ('2024-12-01 10:00:00', 1, 1, 2, 50000.00, 100000.00),
    ('2024-12-01 11:00:00', 2, 2, 10, 500.00, 5000.00),
    ('2024-12-01 12:00:00', 3, 3, 5, 1000.00, 5000.00);
