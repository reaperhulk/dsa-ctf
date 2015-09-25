From: Light Grey Hat <hat@anonymous.local>

Subject: Re: Do you have more DSA details?

To: Faceless Employee <femployee@personalemail.local>

Okay, I spent some time researching DSA and here's some more information for
you. A complete DSA key is made up of 5 values: `p`, `q`, `g`, `x`, and `y`.
`p`, `q`, `g`, and `y` are all public values. The `/public_key` endpoint on the
server gives these values and can be used to verify that a given signature is
valid. The private value, x, is what we need to unlock the funds at my bank.
A DSA signature is normally computed as follows:

* First pick a `k` where 0 < `k` < `q`
* Compute the value `r`. Conceptually this is g<sup>k</sup> mod p mod q.
  However, as `g` and `k` are both large numbers it is very slow to compute this
  value directly. Fortunately [modular exponentiation](http://en.wikipedia.org/wiki/Modular_exponentiation)
  allows us to do the calculation very quickly. In Python you can calculate
  this via the built-in `pow` method: `pow(g, k, p) % q`.
* Calculate the modular multiplicative inverse of `k` modulo `q`. That is,
  `kinv` such that `(k * kinv) % q = 1`
* Compute the hash of the message you want to sign. Based on what you told me
  they're using SHA1 and converting it into an integer assuming big endian byte
  order. To do this in Python: `int.from_bytes(hashlib.sha1(data).digest(), 'big')` (Python 3 required!)
* Finally, calculate `s` using `kinv * (h + r * x) % q`

From what you've told me, the [main.py](https://github.com/reaperhulk/dsa-ctf/blob/master/main.py#L55)
in the secure signer code base may already have a signature implementation?
Take a look !

To confirm that `r` and `s` are correct you can also perform a DSA verification.

* Compute `w`, the modular inverse of `s` modulo `q`
* Calculate `u1 = (h * w) % q`
* Calculate `u2 = (r * w) % q`
* Calculate `v`, defined as `((g ** u1) * (y ** u2)) % p % q`. This will need to be done via modular exponentiation!

At this point `v` should be equal to `r`.

With a working DSA implementation, now we can look more closely at recovering
the private key.  Is there some way to solve for `x` given
`s = (kinv * (h + r * x)) % q`? That might be worth looking into.
