library ieee;
use ieee.std_logic_1164.all;

use ieee.numeric_std.all;

use work.all;

entity TopLevel is
   port (
		SW2 : in std_logic;
		LED1 : out std_logic;
		CLK : in std_logic;
		H1P5 : out std_logic
	);
end TopLevel;

architecture Behavioral of TopLevel is
	signal SClkDouble, SClk: std_logic;
	signal LowFClk: std_logic;
begin
	
	-- Divider 7*31 then 2 to have 50% DC 115200

	SClk_Div_7_31: entity ClkDivN generic map(N => 7*31) port map(
		ClkIn => CLK,
		ClkOut => SClkDouble
	);
	SClk_Div_2: entity ClkDiv2N generic map(N => 1) port map(
		ClkIn => SClkDouble,
		ClkInt => open,
		ClkOut => SClk
	);

	H1P5 <= SClk;

	-- Led visualization

	SClk_Div_2N16: entity ClkDiv2N generic map(N => 16) port map(
		ClkIn => SClk,
		ClkInt => open,
		ClkOut => LowFClk
	);
	LED1 <= LowFClk when SW2 = '0' else '1';

end Behavioral;

