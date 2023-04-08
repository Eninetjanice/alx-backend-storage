--  creates a function SafeDiv that divides (& returns) the 1st by the 2nd num
-- Or returns 0 if the 2nd numb == 0.
-- DELIMITTER $$
DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (
	a INT,
	b INT
)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = (a * 1.0) / b;
	END IF;
    RETURN (result);
END //

DELIMITER ;
