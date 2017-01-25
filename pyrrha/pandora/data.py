client_keys = {
    'android-generic':{
        'deviceModel': 'android-generic',
        'username': 'android',
        'password': 'AC7IBG09A3DTSYM4R41UJWL07VLN8JI7',
        'rpcUrl': '://tuner.pandora.com/services/json/?',
        'encryptKey': '6#26FRL$ZWD',
        'decryptKey': 'R=U!LH$O2B#',
        'version' : '5',
    },
    'pandora-one':{
        'deviceModel': 'D01',
        'username': 'pandora one',
        'password': 'TVCKIBGS9AO9TSYLNNFUML0743LH82D',
        'rpcUrl': '://internal-tuner.pandora.com/services/json/?',
        'encryptKey': '2%3WCL*JU$MP]4',
        'decryptKey': 'U#IO$RZPAB%VX2',
        'version' : '5',
    }
}
default_client_id = "android-generic"
default_one_client_id = "pandora-one"

# See http://pan-do-ra-api.wikia.com/wiki/Json/5/station.getPlaylist
valid_audio_formats = [
    ('highQuality', 'High'),
    ('mediumQuality', 'Medium'),
    ('lowQuality', 'Low'),
]
default_audio_quality = 'mediumQuality'

# The CA used by internal-tuner.pandora.com is untrusted by most machines so we will just directly
# trust it.

# VeriSign Class 3 International Server CA - G3:
#    https://knowledge.symantec.com/support/ssl-certificates-support/index?page=content&id=SO26896
internal_cert = '''-----BEGIN CERTIFICATE-----
MIIGKTCCBRGgAwIBAgIQZBvoIM4CCBPzLU0tldZ+ZzANBgkqhkiG9w0BAQUFADCB
yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL
ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp
U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW
ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0
aG9yaXR5IC0gRzUwHhcNMTAwMjA4MDAwMDAwWhcNMjAwMjA3MjM1OTU5WjCBvDEL
MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW
ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2UgYXQg
aHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykxMDE2MDQGA1UEAxMtVmVy
aVNpZ24gQ2xhc3MgMyBJbnRlcm5hdGlvbmFsIFNlcnZlciBDQSAtIEczMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmdacYvAV9IGaQQhZjxOdF8mfUdza
sVLv/+NB3eDfxCjG4615HycQmLi7IJfBKERBD+qpqFLPTU4bi7u1xHbZzFYG7rNV
ICreFY1xy1TIbxfNiQDk3P/hwB9ocenHKS5+vDv85burJlSLZpDN9pK5MSSAvJ5s
1fx+0uFLjNxC+kRLX/gYtS4w9D0SmNNiBXNUppyiHb5SgzoHRsQ7AlYhv/JRT9Cm
mTnprqU/iZucff5NYAclIPe712mDK4KTQzfZg0EbawurSmaET0qO3n40mY5o1so5
BptMs5pITRNGtFghBMT7oE2sLktiEuP7TfbJUQABH/weaoEqOOC5T9YtRQIDAQAB
o4ICFTCCAhEwEgYDVR0TAQH/BAgwBgEB/wIBADBwBgNVHSAEaTBnMGUGC2CGSAGG
+EUBBxcDMFYwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LnZlcmlzaWduLmNvbS9j
cHMwKgYIKwYBBQUHAgIwHhocaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYTAO
BgNVHQ8BAf8EBAMCAQYwbQYIKwYBBQUHAQwEYTBfoV2gWzBZMFcwVRYJaW1hZ2Uv
Z2lmMCEwHzAHBgUrDgMCGgQUj+XTGoasjY5rw8+AatRIGCx7GS4wJRYjaHR0cDov
L2xvZ28udmVyaXNpZ24uY29tL3ZzbG9nby5naWYwNAYDVR0lBC0wKwYIKwYBBQUH
AwEGCCsGAQUFBwMCBglghkgBhvhCBAEGCmCGSAGG+EUBCAEwNAYIKwYBBQUHAQEE
KDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC52ZXJpc2lnbi5jb20wNAYDVR0f
BC0wKzApoCegJYYjaHR0cDovL2NybC52ZXJpc2lnbi5jb20vcGNhMy1nNS5jcmww
KAYDVR0RBCEwH6QdMBsxGTAXBgNVBAMTEFZlcmlTaWduTVBLSS0yLTcwHQYDVR0O
BBYEFNebfNgioBX33a1fzimbWMO8RgC1MB8GA1UdIwQYMBaAFH/TZafC3ey78DAJ
80M5+gKvMzEzMA0GCSqGSIb3DQEBBQUAA4IBAQBxtX1zUkrd1000Ky6vlEalSVAC
T/gvF3DyE9wfIYaqwk98NzzURniuXXhv0bpavBCrWDbFjGIVRWAXIeLVQqh3oVXY
QwRR9m66SOZdTLdE0z6k1dYzmp8N5tdOlkSVWmzWoxZTDphDzqS4w2Z6BVxiEOgb
Ett9LnZQ/9/XaxvMisxx+rNAVnwzeneUW/ULU/sOX7xo+68q7jA3eRaTJX9NEP9X
+79uOzMh3nnchhdZLUNkt6Zmh+q8lkYZGoaLb9e3SQBb26O/KZru99MzrqP0nkzK
XmnUG623kHdq2FlveasB+lXwiiFm5WVu/XzT3x7rfj8GkPsZC9MGAht4Q5mo
-----END CERTIFICATE-----
'''
