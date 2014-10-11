From: Medium Grey Hat <hat@anonymous.local>

Subject: Re: How would you solve for x?

To: Faceless Employee <femployee@personalemail.local>

Using the equation for s we can use modular arithmetic to solve for x.

1. `s = (kinv * (h + r * x)) % q`
2. `s * k = (h + r * x) % q`
3. `(s * k) % q = (h + r * x) % q` **Note:** (s * k) will always be less than q, so adding `% q` is just for clarity.
4. `((s * k) - h) % q = (r * x) % q`
5. `(rinv * ((s * k) - h)) % q = x`

`rinv` is calculated just like `kinv` in the previous email. So since we know
every value with the exception of `k` all we need to learn is `k` to obtain `x`!

Once we have `x` we can confirm it's correct by computing `g**x % p`. The
result should be equal to `y`. Remember that you'll want to do that via
modular exponentiation!

Why don't you look at the source code to see how they derive `k` for signatures?
It must be predictable in some fashion. Email me if you're having trouble!
