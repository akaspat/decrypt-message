# 1. У вас уже есть ответ на почте в виде:
Необходимо поместить в файл encAesKey
В файл помещается только часть после `Encrypted Aes Key on Base64:`
т.е. все кракозябры с `CQnSd ... по PGIQ==` включительно.
```
Aes BlockSize: 128, Mode:CBC, Padding:PKCS7
Encrypted Aes Key on Base64:
CQnSdUCWlg8MA3NcNASM81q0UsK5mEayN4gnhQeEvbCIFmtcwZWr80pt5pxn8tYTlsVbr5uMAho9z5p4BoB802Cy864TqwWEe9ltym4Ktik7R52xKfqGrd+WMZv1VYZoifmfRZKyukRP3RHQ2N0f1baLGsm7dA6CU5NqdTLfnNbt+5AkW1oeb0fWDQSjbOaB2DAOIwGyAa6QovlifVO21GlgSKbCOp3pyWUmzlAwQpLeVg4mTzT3zunULHT4Scl/SpzAPxOS40eV4kdPg+3VbNLMikiuhW9Sb/BGxYS5k2DGUdy9yPfHH8N3JC+VR/QxJ86uJJCV8aZM3xWn0pPGIQ==
```

Необходимо поместить в файл encAesIV
В файл помещается только часть после `Encrypted Aes IV on Base64:`
т.е. все кракозябры с `rFlDJ ... по GghiMIw==` включительно.
```
Encrypted Aes IV on Base64:
rFlDJmtyFAse7YGf/gCOMrLu7TMMqeMzAG44BGI0gIO7WkM2VxBBd60D7MdDZ2wM3dpXBZzBUqvRUdGt7opD75cM3/uyVk6+uIysW51H60LiubY0Gai5tMOhPmgx+bZ2g3O537EUi/bX2j79jGNbWCHIQ/m6NU5UqmJ8DaRiswRvdj74HJbdrhJyZpzKyjf6YViqRdiDiwrnAy6McGRzoVU5qcTT4sqE+me0qZ9/Vw5zgrnKU4rksp5IZjGEjYpTM2StXk+Fi6k/WK9zjAR9mXw1nCfl0LXBGfyP2BE2z+sKXWmdYQYC7fB1ShZ1qFV5wUWp1B8cxlhBKnyGghiMIw==
```

Необходимо поместить в файл encMessage
В файл помещается только часть после `Encrypted Message on Base64:`
т.е. все кракозябры с `99ogQ ... по A1DEYc=` включительно.
```
Encrypted Message on Base64:
99ogQ3lILz/6IrjHSqU6aZ8WyeJ7WZ/GhOITU5YQgalp2pp05/xFR+s7nbijmYpiwRrw1dYpUCySvDM/rC+JiOECrS9VpWhjhrWGw04Uf5UDK0emUPjhZA1zTJOkW4JBHJcJiVK8aTsCBl2AD4m/o3GFlTQNKvN11lAPwA1DEYc=
```

# 2. У вас есть приватный ключ
_Была сгенерирована пара ключей: публичный и приватный.  
Публичный вы отправили преподавателю  
Приватный хранили в секрете._  
#### Поместите ваш приватный ключ в файле privat.pem
Ключ записывается в файл вместе с строками `-----BEGIN RSA PRIVATE KEY-----` и `-----END RSA PRIVATE KEY-----`  
В моем случае файл privat.pem выглядел примерно так:
```
-----BEGIN RSA PRIVATE KEY-----
B/hUWZEaSthDN5JGI
...
3oKXUYq1nwPzk
-----END RSA PRIVATE KEY-----
```

_Если ваш приватный ключ начинается с слов   
`-----BEGIN PRIVATE KEY-----`  
то воспользуйтесь [конвертером](https://decoder.link/rsa_converter)  
чтобы получить `-----BEGIN RSA PRIVATE KEY-----`_  
