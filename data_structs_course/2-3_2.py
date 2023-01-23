import heapq

def main():
    n, m = map(int, input().split())
    
    tasks = list(map(int, input().split()))
    heap = list([[0, i] for i in range(n)])
    heapq.heapify(heap)
    time = 0
    
    while len(tasks) > 0:
        while heap[0][0] == time:
            if len(tasks) == 0:
                break
                
            core = heapq.heappop(heap)
            core[0] += tasks.pop(0)
            print(core[1], time)
            heapq.heappush(heap, core)
            
        time = heap[0][0]
    
if __name__ == '__main__': main()