N = int(input())

"""
1234
버림 : 1 3 2
1 버림 / 234 -> 342 -> 3 버림 / 42 -> 24 -> 2 버림 / 4

123456
246
2
버림 : 1 3 5 2 6
1 버림 / 23456 -> 34562 -> 3 버림 / 4562 -> 
5624 -> 5 버림 / 624 -> 246 -> 2 버림 / 46 -> 64 -> 6 버림 / 4

12345678
2468
48
8
버림 : 1 3 5 7 2 6 4
1 버림 / 2345678 -> 3456782 -> 3 버림 / 456782 -> 567824 ->
5 버림 / 67824 -> 78246 -> 7 버림 / 8246 -> 2468 ->
2 버림 / 468 -> 684 -> 6 버림 / 84 -> 48 -> 4 버림 / 8

12345678910111213 -> 홀수 삭제
24681012 -> 4 배수 삭제
2610 -> 6 배수 삭제
210 -> 10 배수 삭제
10

1234567891011121314151617181920
2468101214161820
28101418
21018
218
"""