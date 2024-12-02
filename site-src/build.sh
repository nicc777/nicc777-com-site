#!/bin/sh

mkdocs build

#cp -vf site/404.html site/error.html

cat << EOF > site/error.html
<html>
<head>
<meta http-equiv="refresh" content="2;url=http://www.nicc777.com/" />
<title>Page Moved</title>
</head>
<body>
This page has moved. Click <a href="http://www.nicc777.com/">here</a> to go to the new page.
</body>
</html>
EOF

cat << EOF > site/keybase.txt
==================================================================
https://keybase.io/nicc777
--------------------------------------------------------------------

I hereby claim:

  * I am an admin of http://nicc777.com
  * I am nicc777 (https://keybase.io/nicc777) on keybase.
  * I have a public key ASCw2KEtFioxkgSyfTkWNcXnjyg0xm2tNkOSqpbno20BOAo

To do so, I am signing this object:

{
  "body": {
    "key": {
      "eldest_kid": "0120b0d8a12d162a319204b27d391635c5e78f2834c66dad364392aa96e7a36d01380a",
      "host": "keybase.io",
      "kid": "0120b0d8a12d162a319204b27d391635c5e78f2834c66dad364392aa96e7a36d01380a",
      "uid": "366d086a2f1c076bea8f6187ef5d9819",
      "username": "nicc777"
    },
    "merkle_root": {
      "ctime": 1667718859,
      "hash": "4e41dbdd03db598ef50e38c1dbb76003f30276d1b631dc75680ff0e312204a6fbac1fc888e3e558b220badac857de44a2f12da38c16dec95638642dce96d35e2",
      "hash_meta": "69f9ad5cc2ab9835dd728feae2d03162b79da678089a4aa1386e49160f3c2e5b",
      "seqno": 23497044
    },
    "service": {
      "entropy": "wT1ohnDPM2Oy7xNHSs8r58wx",
      "hostname": "nicc777.com",
      "protocol": "http:"
    },
    "type": "web_service_binding",
    "version": 2
  },
  "client": {
    "name": "keybase.io go client",
    "version": "6.0.2"
  },
  "ctime": 1667718970,
  "expire_in": 504576000,
  "prev": "b8e93f55ca6a5dfdd8bbc1a70ae1883fd5d7ec756e498b7e58df0df329a05f5d",
  "seqno": 5,
  "tag": "signature"
}

which yields the signature:

hKRib2R5hqhkZXRhY2hlZMOpaGFzaF90eXBlCqNrZXnEIwEgsNihLRYqMZIEsn05FjXF548oNMZtrTZDkqqW56NtATgKp3BheWxvYWTESpcCBcQguOk/VcpqXf3Yu8GnCuGIP9XX7HVuSYt+WN8N8ymgX13EIMnpFEo01App+l0LxeWIyxu3rs81ATt18x802oF14tRCAgHCo3NpZ8RA0P141c8zH9wyAaAEumesYoSiZfQLzlx52m5H9cvTm/Vw4nFSJd4Ry8qhiSv5uV8E9/hEyoDdFpfz1RrqE3vBDKhzaWdfdHlwZSCkaGFzaIKkdHlwZQildmFsdWXEIOoCWug8cQiw0V6AtzmQ51HMfaZMUz2k3Ws1/CXuTBqxo3RhZ80CAqd2ZXJzaW9uAQ==

And finally, I am proving ownership of this host by posting or
appending to this document.

View my publicly-auditable identity here: https://keybase.io/nicc777

==================================================================
EOF

mkdir site/.well-known
cat << EOF > site/.well-known/keybase.txt
==================================================================
https://keybase.io/nicc777
--------------------------------------------------------------------

I hereby claim:

  * I am an admin of http://nicc777.com
  * I am nicc777 (https://keybase.io/nicc777) on keybase.
  * I have a public key ASCw2KEtFioxkgSyfTkWNcXnjyg0xm2tNkOSqpbno20BOAo

To do so, I am signing this object:

{
  "body": {
    "key": {
      "eldest_kid": "0120b0d8a12d162a319204b27d391635c5e78f2834c66dad364392aa96e7a36d01380a",
      "host": "keybase.io",
      "kid": "0120b0d8a12d162a319204b27d391635c5e78f2834c66dad364392aa96e7a36d01380a",
      "uid": "366d086a2f1c076bea8f6187ef5d9819",
      "username": "nicc777"
    },
    "merkle_root": {
      "ctime": 1667718859,
      "hash": "4e41dbdd03db598ef50e38c1dbb76003f30276d1b631dc75680ff0e312204a6fbac1fc888e3e558b220badac857de44a2f12da38c16dec95638642dce96d35e2",
      "hash_meta": "69f9ad5cc2ab9835dd728feae2d03162b79da678089a4aa1386e49160f3c2e5b",
      "seqno": 23497044
    },
    "service": {
      "entropy": "wT1ohnDPM2Oy7xNHSs8r58wx",
      "hostname": "nicc777.com",
      "protocol": "http:"
    },
    "type": "web_service_binding",
    "version": 2
  },
  "client": {
    "name": "keybase.io go client",
    "version": "6.0.2"
  },
  "ctime": 1667718970,
  "expire_in": 504576000,
  "prev": "b8e93f55ca6a5dfdd8bbc1a70ae1883fd5d7ec756e498b7e58df0df329a05f5d",
  "seqno": 5,
  "tag": "signature"
}

which yields the signature:

hKRib2R5hqhkZXRhY2hlZMOpaGFzaF90eXBlCqNrZXnEIwEgsNihLRYqMZIEsn05FjXF548oNMZtrTZDkqqW56NtATgKp3BheWxvYWTESpcCBcQguOk/VcpqXf3Yu8GnCuGIP9XX7HVuSYt+WN8N8ymgX13EIMnpFEo01App+l0LxeWIyxu3rs81ATt18x802oF14tRCAgHCo3NpZ8RA0P141c8zH9wyAaAEumesYoSiZfQLzlx52m5H9cvTm/Vw4nFSJd4Ry8qhiSv5uV8E9/hEyoDdFpfz1RrqE3vBDKhzaWdfdHlwZSCkaGFzaIKkdHlwZQildmFsdWXEIOoCWug8cQiw0V6AtzmQ51HMfaZMUz2k3Ws1/CXuTBqxo3RhZ80CAqd2ZXJzaW9uAQ==

And finally, I am proving ownership of this host by posting or
appending to this document.

View my publicly-auditable identity here: https://keybase.io/nicc777

==================================================================
EOF


cat << EOF > site/.well-known/security.txt
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Contact: https://github.com/nicc777
Expires: 2026-12-30T23:00:00.000Z
Encryption: https://keybase.io/nicc777/pgp_keys.asc
Preferred-Languages: en, nl, af
Canonical: https://www.nicc777.com/.well-known/security.txt
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEEEyWbjRMZ7xwAvl9KdYZXLGxHG3oFAmdMtpUACgkQdYZXLGxH
G3oIghAA1LSFhMWNH066bSLHuUSw56pR3ODzCOhjGD/fuRszN0VIbx5XfkEEX1VK
ZUkRjZJbCt0NSfiqrPrh869P3UgbNCB5fcmerUJAV418nMhJPlreXtgfPvEkwmEN
eIjFOqqL/6/jNs8ZNMeHtPDjpHX/ww4xs8FGEPbURTjqBqorcGS3xnUe7FVqepLm
hFHPFprZpTli8L8+X4qvyzP6brxKGlE6kDGN5easuce+FQ4hb0lJdHvhMOWuC3Ut
SHwxBqYQRnrL9MzIK+FT27BoqCYiZvbaQRWqZe6n9v72hwfovdoZbiyqxIDic7aG
n1dAc5QsCDBVTOJcBXLL5EhEg7WIWPnyprY9Oq5fubpqqBC+CuzYgNPx/QeL/v9r
aPSl/NlJbvSppMQrjAHeHlyuZDHPVv45SECTi9T2BMq4hShsdRTdroNejyIVDdHo
kgjUTWvCLeGGNw6QgvtCq9xQYy5fRL0Wctgs1meXcue2MhZiwpnS09ERZDbBRif+
a9VolpO3fMrXQ7mC+YwuIRrjSsrnG5stU8306UVz6VC1o+YX5YcSW6lS3B8UPPub
uVS2pfXMH4/mxreVEeCCCvSqvF2y3zVinkHgTxZ7uUYJmpyHV3PuHJrXVvP1TNdK
z7106DN46H9rGt6/HTOlJSnn9bkPOBK0hOram3v3WcR1j4jW294=
=cMtA
-----END PGP SIGNATURE-----
EOF

# cd site
# aws s3 sync ./ s3://www.nicc777.com/ --profile nicc777
# cd ../

python3 prepare_deployment.py --bucket-name="www.nicc777.com" --debug
