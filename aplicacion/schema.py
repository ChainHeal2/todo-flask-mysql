"""DOC"""
instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    """
    CREATE TABLE user(
        id int PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )

    """,
    """
    CREATE TABLE todo (
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_by int NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL,
        FOREIGN KEY (created_by) REFERENCES user(id)
    );

    """
]
