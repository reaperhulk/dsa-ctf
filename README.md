# Breakin' DSA

### Welcome To Innitech

From: HR <hr@innitech.local>

Subject: Welcome to Innitech

To: Faceless Employee <femployee@innitech.local>

Congratulations Faceless! We're pleased to welcome you to the Innitech family.
As a new employee we have granted you access to our secure signing application.
This service is used to sign messages and authenticate they came from an
Innitech employee. For security purposes the key resides solely on this secure
server and all employees must make a `GET` request to `/sign/<data>` where
`<data>` is the payload you wish to sign. You will receive a JSON structure
containing `r` and `s`, the two components of a DSA signature, in response.
You may also make a `GET` request to `/public_key` to obtain a JSON structure
containing `p`, `q`, `g`, and `y`. These are the public components of the DSA
key.

As a developer you may also be interested in the source code to this service,
which can be obtained from our [repository](https://github.com/reaperhulk/dsa-ctf).
All commits to this repo follow our standard secure SDLC policies, which you
may access on our corporate intranet. If you'd like to run your own local copy
of the signing server please see [SETUP](SETUP.md).

You have been automatically logged into the system via our SSO, but you can
request a password reset link by making a `GET` request to `/forgotpass`. This
will supply a link that you can use to change the password. The actual password
reset functionality is not yet implemented, but password reset code generation
is production quality.

===============================================================

From: Ostensibly White Hat <hat@anonymous.local>

Subject: Earn Millions In A Few Steps

To: Faceless Employee <femployee@personalemail.local>

Faceless,

I am a former Innitech client, but after a disagreement about the disbursement
of $30M I recently received I terminated the relationship.  Unfortunately, the
only way to access the funds is by signing some sensitive data with Innitech's
key and they are refusing to allow me access. If you are willing to help me
resolve this issue I'd be happy to give you 20% of the $30M I need to transfer.
I know it's a lot to ask, but could you somehow obtain the private key and
send it to me?

If you don't know where to start, feel free to email me back and we can discuss.

#### Inbox
[Re: Where do I start?](emails/where_do_i_start.md)

[Re: Do you have more DSA details?](emails/dsa_details.md)

[Re: How would you solve for x?](emails/solve_for_x.md)

[Re: Predictable k?](emails/predictable_k.md)

[Re: randrange issues](emails/randrange_issues.md)

[Re: putting it all together](emails/putting_it_all_together.md)
