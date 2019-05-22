library ieee;

use ieee.math_real.all;

package Math is

  pure function nbits(N : positive) return natural;

end Math;

package body Math is

-- Example 1
  pure function nbits(N : positive) return natural is
  begin
    return natural(ceil(log2(real(N))));
  end nbits;

end Math;
