class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []

        for row in matrix:
            array.extend(row)

        start = 0
        end = len(array) - 1

        if len(array) == 1 and array[0] == target:
            return True

        while start <= end:
            if array[start] == target:
                return True
            if array[end] == target:
                return True
            
            mid = (start + end) // 2

            if array[mid] == target:
                return True
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False