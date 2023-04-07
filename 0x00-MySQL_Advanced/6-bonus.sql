-- SQL script that creates a stored procedure AddBonus
-- That adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
    INSERT INTO projects(name)
    SELECT project_name FROM DUAL
    -- Check if the project exists
    WHERE NOT EXISTS(SELECT * FROM projects WHERE name = project_name LIMIT 1);
    -- add correction to the database
    INSERT INTO corrections(user_id, project_id, score) 
    VALUES (
    user_id,
    (SELECT id FROM projects WHERE name = project_name),
    score); 
END $$
DELIMITER ;
