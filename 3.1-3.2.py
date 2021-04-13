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
