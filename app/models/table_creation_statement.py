tables = (
    "CREATE TYPE roles_type  AS ENUM('user', 'admin', 'superadmin')",

    """
    CREATE TABLE IF NOT EXISTS credentials  (
    credential_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(50) UNIQUE NOT NULL,
    hashed_password TEXT
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS users(
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50),
    role roles_type DEFAULT 'user',
    credential_id UUID NOT NULL UNIQUE,
    FOREIGN KEY (credential_id) REFERENCES credentials(credential_id)
    )
    """,

    "CREATE TYPE category_type AS ENUM('personal', 'school', 'leisure', 'Job')",
    "CREATE TYPE status_type AS ENUM('pending', 'completed', 'canceled')",

    """
    CREATE TABLE IF NOT EXISTS tasks(
    task_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50),
    category category_type NOT NULL, 
    user_id UUID,
    status status_type DEFAULT 'pending',
    time_created TIMESTAMPTZ DEFAULT NOW(),
    time_to_be_completed VARCHAR(50),
    time_completed TIMESTAMPTZ,
    
    FOREIGN KEY (user_id) REFERENCES users(user_id)

    );
    """,

)