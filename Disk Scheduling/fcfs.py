thm = int(0)
print("Enter the Number of Requests : ")
req = int(input())
print("Enter the Initial Head Position : ")
head = int(input())
print("Enter the Seek Rate : ")
srate = int(input())
print("Enter the Requests : ")
arr = [ int(input()) for i in range(req)]
thm = thm + abs(head - arr[0])
print(str(head)+" -> "+str(arr[0]), end='')
for i in range(1, req):
    thm = thm + abs(arr[i] - arr[i-1])
    print(" -> "+str(arr[i]), end='')
stime = srate * thm
print("\nThe Total Head Movement is",thm)
print("The Seek Time is",stime)



