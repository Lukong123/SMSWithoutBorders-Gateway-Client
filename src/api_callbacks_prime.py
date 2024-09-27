from smswithoutborders_libsig.keypairs import x25519

alice = x25519()
alice_public_key_original = alice.init()

bob = x25519("db_keys/bobs_keys.db")
bob_public_key_original = bob.init() # not an encryption key, won't work unless for AD

SK = alice.agree(bob_public_key_original)
SK1 = bob.agree(alice_public_key_original)

# store the following
alice_pnt_keystore = alice.pnt_keystore
alice_secret_key = alice.secret_key # used to decrypt the keystore sql file

# reinitializing would be...
alice = x25519(pnt_keystore=alice_pnt_keystore, keystore_path=alice_keystore_path, secret_key=alice_secret_key)

assert(SK)
assert(SK1)
assert(SK == SK1)