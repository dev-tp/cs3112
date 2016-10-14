# Assignment Four

## 1. Implement Bruteforce Maximum Subarray

## 2. Implement Divide-and-Conquer Maximum Subarray

    FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
        left_sum := -INF
        sum := 0
        for i := mid downto low
            sum := sum + i
            if sum > left_sum
                left_sum := sum
                max_left := i

        right_sum := -INF
        sum := 0
        for j := mid + 1 to high
            sum := sum + j
            if sum > right_sum
                right_sum := sum
                max_right := j

        return (max_left, max_right, left_sum + right_sum)


    FIND_MAXIMUM_SUBARRAY(A, low, high)
        if high = low
            return (low, high, A[low])
        else
            mid := (low + high) / 2

        (left_low, left_high, left_sum) := FIND_MAXIMUM_SUBARRAY(A, low, mid)
        (right_low, right_high, right_sum) := FIND_MAXIMUM_SUBARRAY(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) := FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)

        if left_sum >= right_sum and left-sum >= cross_sum
            return (left_low, left_high, left-sum)
        else if right_sum >= left-sum and right_sum >= cross_sum
            return (right_low, right_high, right_sum)
        else
            return (cross_low, cross_high, cross_sum)