# ded = int(input())
# m = list(map(int, input().split()))
# for i in range (1, max(m)+1):
#     sum = 0
#     for j in m:
#         sum += j // i + (j % i != 0)
#     if sum <= ded:
#         print(i)
#         break

def can_complete_projects(tasks, T, M):
    days_needed = 0
    for task_count in tasks:
        days_needed += (task_count + M - 1) // M  # Делим нацело, чтобы учитывать деление по дням
    return days_needed <= T

def min_tasks_per_day(tasks, T):
    left = 1
    right = max(tasks)
    while left < right:
        mid = (left + right) // 2
        if can_complete_projects(tasks, T, mid):
            right = mid
        else:
            left = mid + 1
    return left

# Считываем входные данные
T = int(input())
tasks = list(map(int, input().split()))

# Находим минимальное количество задач в день
min_tasks = min_tasks_per_day(tasks, T)

print(min_tasks)