# Big-O for Common Patterns
## Hash Maps (Python dict)

**Access/Insert/Delete:** O(1) average case, O(n) worst case
The worst case occurs when many keys hash to the same bucket, creating long collision chains
Python uses open addressing with random probing to minimize clustering
**Space complexity:** O(n)

## Heaps (Python heapq)

**Insert (heappush):** O(log n)
**Extract min (heappop):** O(log n)
**Peek min (heap[0]):** O(1)
**Build heap (heapify):** O(n)
**Push then pop (heappushpop):** O(log n)
**Replace root (heapreplace):** O(log n)
The logarithmic operations come from the need to maintain the heap property by "bubbling up" or "bubbling down" through the tree levels.