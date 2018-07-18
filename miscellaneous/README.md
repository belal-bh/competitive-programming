# Miscellaneous

### Split a string
link - [http://www.cplusplus.com/reference/cstring/strtok/](http://www.cplusplus.com/reference/cstring/strtok/)
```
    /* strtok example */
    #include <stdio.h>
    #include <string.h>

    int main ()
    {
      char str[] ="- This, a sample string.";
      char * pch;
      printf ("Splitting string \"%s\" into tokens:\n",str);
      pch = strtok (str," ,.-");
      while (pch != NULL)
      {
        printf ("%s\n",pch);
        pch = strtok (NULL, " ,.-");
      }
      return 0;
    }
```

### Bitwise Operation
Oprerators:
```
    & (and),
    | (or),
    ^ (xor),
    ~ (1's complement),
    << (shift left),
    >> (shift right).
```
Example:
```
    5*8 same as 5<<3
    5/2 same as 5>>1

    i-th bit on or off : (x & (1 << i)) is not 0 or 0.

    i-th bit will be _on_ : (x | (1 << i)).
    i-th toggle : (x ^ (1 << i))
    i-th bit will be _off_ : if((x & (1 << i))){ (x ^ (1 << i)); } // if on then toggle

    last _k_ bit will remain unchenged and other bits will be _off_ : (x & ((1 << k)-1))

```

