N = int(input())
        
h = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]

n=len(h)
nova=[]

o = len(m)
velha=[]

maior=[]
menor=[]
for j in range(N):
  menor=m[0]
  for i in range(1, len(m)):
    if m[i] < menor:
      menor=m[i]
    
  velha.append(menor) 
  m.remove(menor)


for j in range(N):
  maior=h[0]
  for i in range(1, len(h)):
    if h[i] > maior:
      maior=h[i]
      
  nova.append(maior)
  h.remove(maior)

for j in range(N):
  maior=nova[0]
  menor=velha[0]
  for i in range(1, N):
    if nova[i] < maior:
      maior = nova[i]
    if velha[i] > menor:
      menor= velha[i]
print(maior, " ", menor)
