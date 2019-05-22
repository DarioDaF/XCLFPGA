library ieee;
use ieee.std_logic_1164.all;

use ieee.numeric_std.all;

library DFUtils;
use DFUtils.Math.all;

entity ClkDivN is
	generic ( N : positive );
   port (
		ClkIn : in  std_logic;
		ClkOut : out std_logic
	);
end ClkDivN;

architecture Behavioral of ClkDivN is
	constant NB : natural := nbits(N);
	signal ClkDiv_Cnt : unsigned(NB-1 downto 0);
	signal ClkDiv_Next : unsigned(NB-1 downto 0);
	signal ClkDiv_Rst : boolean;
begin

	-- -- Use this approch and reset to 0?
	-- ClkDiv_7_31_Rst <=
	-- 	'1' when ClkDiv_7_31_Next = (7*31) else
	-- 	'0' when ClkDiv_7_31_Next < (7*31) else
	-- 	'-';

	ClkDiv_Next <= ClkDiv_Cnt + 1;
	ClkDiv_Rst <= ClkDiv_Next = to_unsigned(0, NB);
	process(ClkIn)
	begin
		if(rising_edge(ClkIn))then
			if(ClkDiv_Rst)then
				ClkDiv_Cnt <= to_unsigned(2**NB - N, NB);
			else
				ClkDiv_Cnt <= ClkDiv_Next;
			end if;
		end if;
	end process;

	ClkOut <= '1' when ClkDiv_Rst else '0';
end Behavioral;
