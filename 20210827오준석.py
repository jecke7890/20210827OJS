# -*- coding: utf-8 -*-
import random

# 학생 성적 관리 시스템

## 학생 정보 생성

def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        age = random.randint(18, 22)
        grade = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": grade})
    return students

## 정렬 알고리즘 구현

### 선택 정렬

def selection_sort(students, key):
    n = len(students)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][key] < students[min_idx][key]:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]
    return students

### 삽입 정렬

def insertion_sort(students, key):
    for i in range(1, len(students)):
        key_item = students[i]
        j = i - 1
        while j >= 0 and key_item[key] < students[j][key]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_item
    return students

### 퀵 정렬

def quick_sort(students, key):
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2]
    left = [x for x in students if x[key] < pivot[key]]
    middle = [x for x in students if x[key] == pivot[key]]
    right = [x for x in students if x[key] > pivot[key]]
    return quick_sort(left, key) + middle + quick_sort(right, key)

### 기수 정렬 (성적 기준)

def radix_sort(students):
    max_grade = max(student["성적"] for student in students)
    exp = 1
    while max_grade // exp > 0:
        students = counting_sort(students, exp)
        exp *= 10
    return students

def counting_sort(students, exp):
    n = len(students)
    output = [0] * n
    count = [0] * 10

    for student in students:
        index = (student["성적"] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (students[i]["성적"] // exp) % 10
        output[count[index] - 1] = students[i]
        count[index] -= 1

    for i in range(n):
        students[i] = output[i]

    return students

## 유틸리티 함수

def print_students(students):
    for student in students:
        print(student)

## 메인 함수

def main():
    students = generate_students()
    print("\n생성된 학생 목록:")
    print_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        choice = input("선택: ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        print("\n정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적만 가능)")

        algo_choice = input("선택: ")

        if choice == "1":
            key = "이름"
        elif choice == "2":
            key = "나이"
        elif choice == "3":
            key = "성적"
        else:
            print("잘못된 입력입니다.")
            continue

        if algo_choice == "1":
            students = selection_sort(students, key)
        elif algo_choice == "2":
            students = insertion_sort(students, key)
        elif algo_choice == "3":
            students = quick_sort(students, key)
        elif algo_choice == "4" and key == "성적":
            students = radix_sort(students)
        else:
            print("잘못된 입력입니다.")
            continue

        print("\n정렬된 결과:")
        print_students(students)

if __name__ == "__main__":
    main()
