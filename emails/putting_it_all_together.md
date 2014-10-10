From: Hat <hat@anonymous.local>

Subject: Re: putting it all together

To: Faceless Employee <femployee@personalemail.local>

You're clearly on the right track. If you've confirmed that your cloned
Mersenne Twister instance is outputting the same values as calls to `/random`
then you just need to implement the same logic that Python uses for `randrange`.

At that point the process looks like:

* Make calls to `/random` to obtain internal state of RNG and build local clone
* Make a call to `/sign` with some data you want to sign and get back r, s.
* Use r, s, p, q, g, and the value you get from your cloned RNG (which is the
  k you predict the server will use) to solve for x.
* To confirm the x you've calculated is correct you can do `pow(g, x, p)`, the
  result of which will be equal to y.
