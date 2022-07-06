import requests
import json

"""
var bitcoin = require('bitcoinjs-lib')
var keyPair = bitcoin.ECPair.fromWIF('L4rK1yDtCWekvXuE6oXD9jCYfFNV2cWRpVuPLBcCU2z8TrisoyY1')
var privateKey = keyPair.privateKey
var message = '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV:1657030068:starRegistry'

var signature = bitcoinMessage.sign(message, privateKey, keyPair.compressed)
console.log(signature.toString('base64'))

var address = '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV'

console.log(bitcoinMessage.verify(message, address, signature))
const {addresss} = bitcoin.payments.p2pkh({ pubkey: keyPair.publicKey })
console.log(addresss)
"""


json_data = {
    'address': '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV',
    'signature': 'H/LDSQK7CNnskxRBshEHTnMNkYlLNFh6gB2PtWxpJJj4CX424CP4/M15OFJLLCer0IcJKohuUzA+ebrofO5ma8Q=',
    'message': '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV:1657069315:starRegistry',
    'star': {
        'dec': '68 52 56.9',
        'ra': '16h 29m 1.0s',
        'story': 'Testing submitStar 2',
    },
}

response = requests.post('http://localhost:8000/submitstar', json=json_data)

print(response.status_code)
print(json.dumps(response.json(), indent=4))



#
# from bitcoinlib.wallets import Wallet
# w = Wallet.create('Wallet3')
# key1 = w.get_key()
# print(key1.address)