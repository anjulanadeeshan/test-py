def highestValuePalindrome(s, n, k):
    s = list(s)
    i, j = 0, n - 1
    required = 0

    # Pass 1: count total forced mismatches
    while i < j:
        if s[i] != s[j]:
            required += 1
        i += 1
        j -= 1

    if required > k:
        return "-1"

    # Pass 2: single pass — minimal fix vs '9' upgrade per pair
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            larger = max(s[i], s[j])
            if larger != '9' and k > required:
                s[i] = s[j] = '9'
                k -= 2
            else:
                s[i] = s[j] = larger
                k -= 1
            required -= 1
        else:
            if s[i] != '9' and k - required >= 2:
                s[i] = s[j] = '9'
                k -= 2
        i += 1
        j -= 1

    # Middle character (odd-length string, no mirror pair)
    if n % 2 == 1:
        mid = n // 2
        if s[mid] != '9' and k > 0:
            s[mid] = '9'
            k -= 1

    return ''.join(s)


inp = list(map(int, input().rstrip().split()))
n = inp[0]
k = inp[1]
s = input().rstrip()

print(highestValuePalindrome(s, n, k))