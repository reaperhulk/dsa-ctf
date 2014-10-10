From: Hat <hat@anonymous.local>

Subject: Re: Predictable k?

To: Faceless Employee <femployee@personalemail.local>

From what you're telling me it sounds like it might be worth looking at what
Python uses for `randrange` in the random module. Maybe that can be predicted?
Do these links help?

* https://github.com/python/cpython/blob/c7688b44387d116522ff53c0927169db45969f0e/Lib/random.py#L170
* https://github.com/python/cpython/blob/c7688b44387d116522ff53c0927169db45969f0e/Modules/_randommodule.c#L350

This might be a little dense, but we can work through it together. If you get
lost just email me!
