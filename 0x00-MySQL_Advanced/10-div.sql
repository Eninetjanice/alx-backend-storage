--  creates a function SafeDiv that divides (& returns) the 1st by the 2nd num
--- or returns 0 if the 2nd numb == 0.
-- DELIMITTER $$
DELIMITER //

-- DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION IF NOT EXISTS SafeDiv (
	a INT,
	b INT
)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER;
-- BEGIN
--	DECLARE result INT;
--	IF B = 0 THEN
--		SET result = 0;
--	ELSE
--		SET result = a / b;
--	END IF;
--	
--	RETURN result;
-- END$$
-- DELIMITER;
