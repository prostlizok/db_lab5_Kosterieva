--CREATE TABLE match_copy AS SELECT * FROM Match;
DELETE FROM match_copy;

DO $$
DECLARE
	v_id int := 20; 
 BEGIN
 	FOR i IN 1..20
		LOOP
			INSERT INTO match_copy
			 VALUES (v_id, (RANDOM() * (2100-1400) + 1400)::int, 'EUW1', 8);
			 v_id := v_id + 1; 
		END LOOP;
 END;
 $$;

SELECT * FROM match_copy;