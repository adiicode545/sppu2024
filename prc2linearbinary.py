def linear_search(account_list, target):
    for account_id in account_list:
        if account_id == target:
            return True
            return False



def binary_search(account_list, target):
   
    account_list.sort()
    left, right = 0, len(account_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if account_list[mid] == target:
            return True
        elif account_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

if __name__ == "__main__":
    customer_accounts = [105, 203, 150, 98, 220, 333, 120]

    target_id = 150

    if linear_search(customer_accounts, target_id):
        print(f"Linear Search: Account ID {target_id} found.")
    else:
        print(f"Linear Search: Account ID {target_id} not found.")

    if binary_search(customer_accounts, target_id):
        print(f"Binary Search: Account ID {target_id} found.")
    else:
        print(f"Binary Search: Account ID {target_id} not found.")
