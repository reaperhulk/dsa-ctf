From: Hat <hat@anonymous.local>

Subject: Re: randrange issues

To: Faceless Employee <femployee@personalemail.local>

`randrange` appears to call `_randbelow`, which calls `getrandombits`. That
last function uses MT19937 (Mersenne Twister). You can see pseudocode for
implementing MT19937 here: https://en.wikipedia.org/wiki/Mersenne_twister.

When returning a new random integer MT picks one of the 624 elements in its
state vector and then tempers it with a series of bitwise operations. Those
operations are invertible, so given enough outputs you should be able to derive
the complete state of the RNG and predict all future outputs.

The `/random` source on the secure server also uses MT, and due to the way
Python works it appears there's only one global instance of MT. So, you should
be able to query that endpoint and then invert the output to derive the state
of the server's RNG.

We're getting close, I can feel it. Email me if you need help putting it all
together.

-Hat
