library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

use IEEE.NUMERIC_STD.ALL;

entity Nibble2ASCII is
    Port ( Nibble : in  STD_LOGIC_VECTOR (3 downto 0);
           Byte : out  STD_LOGIC_VECTOR (7 downto 0));
end Nibble2ASCII;

architecture WithAdder of Nibble2ASCII is
	signal letter : boolean;
	signal base : unsigned(3 downto 0);
begin
	letter <= unsigned(Nibble) > 9;
	base <= "0111" when letter else "0000";
	Byte(3 downto 0) <= std_logic_vector(base + unsigned(Nibble));
	Byte(7 downto 4) <= "0100" when letter else "0011"; -- "0110" when letter else "0011"; -- if you want lowercase letters
end WithAdder;

architecture WithLookup of Nibble2ASCII is
begin
	with Nibble select Byte(3 downto 0) <=
		"0000" WHEN "0000",
		"0001" WHEN "0001",
		"0010" WHEN "0010",
		"0011" WHEN "0011",
		"0100" WHEN "0100",
		"0101" WHEN "0101",
		"0110" WHEN "0110",
		"0111" WHEN "0111",
		"1000" WHEN "1000",
		"1001" WHEN "1001",
		"0001" WHEN "1010",
		"0010" WHEN "1011",
		"0011" WHEN "1100",
		"0100" WHEN "1101",
		"0101" WHEN "1110",
		"0110" WHEN "1111";
	with Nibble select Byte(7 downto 4) <=
		"0100" WHEN "1010",
		"0100" WHEN "1011",
		"0100" WHEN "1100",
		"0100" WHEN "1101",
		"0100" WHEN "1110",
		"0100" WHEN "1111",
		"0011" WHEN others;
end WithLookup;
