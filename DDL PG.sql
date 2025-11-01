-- docker run --name pg_highload  -e POSTGRES_PASSWORD=mysecretpassword   -e POSTGRES_USER=myuser  -e POSTGRES_DB=mydatabase  -p 5432:5432   -v C:\pg_highload  -d postgres

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  firstname VARCHAR(100) NOT NULL,
  secondname VARCHAR(100) NOT NULL,
  birthdate DATE NOT NULL,
  biography TEXT,
  city VARCHAR(100),
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT now()
);

