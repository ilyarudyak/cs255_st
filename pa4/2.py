import urllib.request
import urllib.error
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------


# create iv and c_i
c = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
iv = c[:32]
c1 = c[32:64]
c2 = c[64:96]
c3 = c[96:128]

m1 = []
m1_ascii = []
for i in range(1, 17):

    # create pad
    pad = ( "0" + hex(i)[2:]) * i
       
    for g in range(32, 127):
        
        
        # create url
        gg = int(iv, 16)^int(pad, 16)^int((hex(g)[2:] + "".join(m1)),16)
        
        

        target = TARGET + hex(gg)[2:] + c1
        

        # Send HTTP request to server
        req = urllib.request.Request(target)

        try:
            f = urllib.request.urlopen(req) # Send HTTP request to server           
        except urllib.error.HTTPError as e:
            # Print response code
            #print ("We got: %d" % e.code)
            if e.code == 404:
                print (g)
                m1.insert(0, hex(g)[2:])
                m1_ascii.insert(0, chr(g))
                break

print ("".join(m1_ascii))









