import heapq

heap = []
data = [(5, 0), (3, 1), (6, 2), (1, 3)]
HCArray = [None] * 51

for item in data:
    heapq.heappush(heap, item)

def HC(heap, m):
    if( len(heap) == 1):
        if m < 27:
            HCArray[heapq.heappop(heap)[1]] = '1'
        else:
            HCArray[heapq.heappop(heap)[1]] = ''
        return
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    N = (a[0]+b[0], m+1)
    heapq.heappush(heap, N)
    HC(heap, m+1)
    print("This is value at m:")
    print(HCArray[m+1])
    HCArray[a[1]] = HCArray[m+1] + '0'
    HCArray[b[1]] = HCArray[m+1] + '1'
    
HC(heap, 26)

print(HCArray)