library ieee;
use ieee.std_logic_1164.all;

use ieee.numeric_std.all;

entity ClkDiv2N is
	generic ( N : positive );
   port (
		ClkIn : in std_logic;
		ClkInt : out std_logic_vector(N-1 downto 0);
		ClkOut : out std_logic
	);
end ClkDiv2N;

architecture Behavioral of ClkDiv2N is
	signal ClkOutBuf : unsigned(N-1 downto 0);
begin
	process(ClkIn)
	begin
		if(rising_edge(ClkIn))then
			ClkOutBuf <= ClkOutBuf + 1;
		end if;
	end process;
	ClkInt <= std_logic_vector(ClkOutBuf);
	ClkOut <= ClkOutBuf(ClkOutBuf'high);
end Behavioral;
