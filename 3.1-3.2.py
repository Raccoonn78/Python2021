class C32:
     state = 'A'

     def etch(self):
          if self.state =='A':
               self.state='B'
               return 0
          elif self.state=='B':
               self.state='C'
               return 3
          elif self.state=='E':
               self.state='F'
               return 7
          elif self.state=='F':
               self.state='G'
               return 8
          else:
                 raise RuntimeError

    
     def hop(self):
          if self.state =='B':
               self.state='B'
               return 4
          elif self.state=='A':
               self.state='H'
               return 2
          elif self.state=='G':
               self.state='C'
               return 11
          elif self.state=='F':
               self.state='C'
               return 9
          else:
                 raise RuntimeError
                    
           
     def stay(self):
          if self.state =='A':
               self.state='C'
               return 1
          elif self.state=='C':
               self.state='D'
               return 5
          elif self.state=='D':
               self.state='E'
               return 6
          elif self.state=='G':
               self.state='H'
               return 10
          else:
               raise RuntimeError

      

print("First case: ")
a = C32()
print(f"o.etch()  = {a.etch()}")
print(f"o.stay()  = {a.stay()}")
print(f"o.hop()  = {a.hop()}")
print(f"o.stay()  = {a.stay()}")
print(f"o.hop() = {a.hop()}")
print(f"o.etch()  = {a.etch()}")
print(f"o.stay() = {a.stay()}")
print(f"o.stay() = {a.stay()}")
print(f"o.etch()  = {a.etch()}")
print(f"o.etch()  = {a.etch()}")
print(f"o.hop() = {a.hop()}")
print(f"o.stay()= {a.stay()}")
print(f"o.stay()= {a.stay()}")
print(f"o.etch() = {a.etch()}")
print(f"o.stay()= {a.stay()}")
print(f"o.hop()    = {a.hop()}")



b = C32()

print("\nSecond case:")
print(f"o.etch()  = {b.etch()}")
print(f"o.hop()  = {b.hop()}")
print(f"o.etch() = {b.etch()}")
print(f"o.etch()   = {b.etch()}")
print(f"o.stay()= {b.stay()}")
print(f"o.stay()= {b.stay()}")
print(f"o.etch() = {b.etch()}")
print(f"o.hop() = {b.hop()}")
print(f"o.stay() = {b.stay()}")
print(f"o.stay() = {b.stay()}")
print(f"o.etch()  = {b.etch()}")
print(f"o.stay() = {b.stay()}")
print(f"o.etch()  = {b.etch()}")
print(f"o.etch()  = {b.etch()}")
print(f"o.hop() = {b.hop()}")











                    
import struct

e_size=2+1+2*6+4+1*7+4+4+1
d_size=4+4+2
c_size=2+4+8
b_size = 4+4+d_size
def parse_e(offset, byte_string):
        e_bytes = byte_string[offset:offset+e_size]
        e_parsed= struct.unpack('HbHHHHHHibbbbbbbII',e_bytes)
        e6_bytes=byte_string[e_parsed[6]:e_parsed[6]+e_parsed[5]]
        e6_parsed= struct.unpack('I'* e_parsed[5],e6_bytes)
        return{'E1': e_parsed[0],
               'E2': e_parsed[1],
               'E3':list(e_parsed[2:7]),
               'E4':e_parsed[3],
               'E5':list(e_parsed[9:15]),
               'E6':list(e6_bytes)
        }
def parse_d(offset, byte_string):
    d_bytes=byte_string[offset:offset+d_size]
    d_parsed= struct.unpack('iIh', d_bytes)
    return{'D1': d_parsed[0],
           'D2': parse_e(d_parsed[1],byte_string),
           'D3':d_parsed[2]
               }
def parse_c(offset, byte_string):
       print('offset = ' + str(offset))     
       c_bytes = byte_string[offset:offset+c_size]
       print('bytes =' + str(c_bytes))
       print('bytes len = ' + str(len(c_bytes)))
       c_parsed= struct.unpack('>Hfq', c_bytes)
       return{'C1':c_parsed[0],
              'C2':c_parsed[1],
              'C3':c_parsed[2]
       }

def parse_b(offset, byte_string):
       print(offset)    
       b1_bytes = byte_string[offset:offset+8]
       b1_parsed= struct.unpack('II', b1_bytes) 
       print(b1_parsed) 
       b1_list = [parse_c(offset+8,byte_string) for addr in range(1, 2)] # b1_parsed[0] - 1)]
       b2_parsed=parse_d(offset+8,byte_string)     
       print(offset)    
       return{
           'B1':b1_list,
           'B2':b2_parsed
       }
def parse_a(offset, byte_string):
       a_bytes = byte_string[offset:offset+8]
       print('A bytes: ' + str(a_bytes))
       print('A bytes len: ' + str(len(a_bytes)))
       a_parsed = struct.unpack('Q', a_bytes)
       print('A1 = ' + str(a_parsed[0]))
       a2_parsed=parse_b(offset+8,byte_string)
       return{
           'A1':a_parsed[0],
           'A2':a2_parsed
       }


def f31(byte_string):
    return parse_a(3,byte_string)

print(f31(b'ZJO\xf5bI\xa1]\xc6\xb0Z\xc1\x05\x00\x00\x00\x1e\x00\x00\x00\xf0\xfbe\xa6'
b'f\x00\x00\x00\x07p\x19\xcb\xbd\x1eT\xbf\xf6;\x81\x81M\xb0\x8ewg\xe1(t'
b'\xca\xbd^\xee\xa0<Z\x10\x06g\x93\x89\xee\x82;?\xcd\x14\xaa\xb8[zr\x1a'
b'>\x05\xe6\xb8\xc0\xbd\x8d\xcd\xbb\xfcX\xf5\x17\xe3\n\xd7\xdf\xf14?{\xdaZO'
b'\x0b\xdb%\x07q4\x8by\xa6\xbbp\xb8\xe9\xe90\x82\xdbp\xed\x0bG\xad\xdc\xe9'
b'\xfc5\xce!\x11|\x8f4\x02\x00\x00\x00d\x00\x00\x00'))                    




