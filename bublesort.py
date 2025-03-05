import time 

def buble_sort_interactive(arr):
    n = len(arr)
    for i in range(n):
        print(f"\nIterasiya{i+1}:")
        swapped = False 

        for j in range(0, n-i-1):
            print(f"Müqayisə: {arr[j]} və {arr[j+1]}")
            time.sleep(1)


            if arr[j] > arr[j + 1]:
                print(f"Dəyişdiririk: {arr[j]} və {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 

            print(f" Hal - Hazırda list: {arr}")

            if not swapped:
                print("Array artıq sıralanıb, prosesi dayandırırıq")



numbers = [5,2,8,56,34,23,6,3]
buble_sort_interactive(numbers)
print("\n Sıralanmış list:", numbers)