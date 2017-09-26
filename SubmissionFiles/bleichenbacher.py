from roots import *
import hashlib

import sys

message = sys.argv[1]



if __name__ == "__main__":
	#message = sys.argv[1]
	
	m = hashlib.sha256()
	m.update(message)
	magic_bytes = 0x3031300d060960864801650304020105000420
	#print m.hexdigest()
	
	n = 0x00b06004b3528bfd2d187f48e6cb9f3fe79afade6cc3c428dd0577b8bb3e752824b632d100d28b396726a887c5189ded3fe9717d959730dadbf468b2bc76eea3c15091a38b61fdfa46b1510ef885ea3105ae7d7f3007e97c6761bc47e715ba32464c77f7d0cfd2c88c0f53d45404a110d6951d3f4255edc3523921237a86f35fed200c7e45870b822d7652dc896d0de064617dbb48eb9b1d47103f12911b0dab3d91e0fdb847f0b87cf2b20b19d3b951cae86cab611893f6f4cd016c68607e970fc2db800f981d9bb4441fe5d70299693a8ae51f2e9b2656f0c279bf87ecb96a753f231739eb1f9a9d7dd01f15f283dd2da2887e7fdef6aedd61c4ca7b3be1b1cd
	# This is the modulus I calculated from the public key
	e = 3
	#size of public key is 2048 bits
	
	forged_signature = "0x0001FF003031300d060960864801650304020105000420" # Hoping to concatenate to make life easier
	forged_signature = forged_signature + str(m.hexdigest())
	
	#print forged_signature;
	end = ""
	for by in range(0,402):
		end += "0"
	
	#print '\n'
	forged_signature = forged_signature + end
	forged_signature = int(forged_signature, 16)
	cube_root = integer_nthroot(forged_signature, 3)
	if cube_root[1]:
		print integer_to_base64(cube_root[0])
	else:
		print integer_to_base64(cube_root[0]+ 1)
