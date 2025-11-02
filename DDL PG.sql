-- docker run --name pg_highload  -e POSTGRES_PASSWORD=mysecretpassword   -e POSTGRES_USER=myuser  -e POSTGRES_DB=mydatabase  -p 5432:5432   -v C:\pg_highload  -d postgres

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  firstname VARCHAR(100) NOT NULL,
  secondname VARCHAR(100) NOT NULL,
  birthdate DATE NOT NULL,
  biography TEXT,
  interests TEXT,
  city VARCHAR(100),
  email VARCHAR(150),
  phone VARCHAR(20),
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION update_users_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_users_updated_at();
