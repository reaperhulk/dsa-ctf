From: Hat <hat@anonymous.local>

Subject: Re: Do you have more DSA details?

To: Faceless Employee <femployee@personalemail.local>

Okay, I spent some time researching DSA and here's some more information for
you. A complete DSA key is made up of p, q, g, x, and y. p, q, g, and y are all
considered public values. The public key you have to verify signatures
received from the server contains these values. The private value, x, is what
we need to unlock the funds at my bank. A DSA signature is normally computed as
follows:

* First pick a k where 0 < k < q
* Compute the value r via `pow(g, k, p) % q`
* Calculate the modular multiplicative inverse of k modulo q. That is, kinv
  such that `(k * kinv) % q = 1`
* Compute the hash of the message you want to sign. Based on what you told me
  they're using SHA1 and converting it into an integer assuming big endian byte
  order. `int.from_bytes(hashlib.sha1(data).digest(), 'big')`
* Finally, calculate s `kinv * (h + r * x) % q`

Using that last equation we can use modular arithmetic to solve for x.

* `s = kinv * (h + r * x) % q`
* `s * k = (h + r * x) % q`
* `rinv * ((s * k) - h) % q = x`

`rinv` is calculated just like `kinv` above. So since we know every value with
the exception of `k` all we need to learn is `k` to obtain `x`!
