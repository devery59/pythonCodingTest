import sys
sys.stdin = open("in2.txt","rt")
N = int(input())
first_list = list(map(int, input().split()))
M = int(input())
second_list = list(map(int, input().split()))

print(sorted(first_list+second_list))
