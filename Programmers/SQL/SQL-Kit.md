# SQL-Kit
>[모든 레코드 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/59034) 
```
SELECT * from ANIMAL_INS order by ANIMAL_ID
```
#
>[조건에 맞는 도서 리스트 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/144853) 

```
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
From Book
WHERE  YEAR(PUBLISHED_DATE) = "2021" And CATEGORY = "인문"
ORDER BY PUBLISHED_DATE asc
```
#
>[역순 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/59035) 
```
SELECT NAME, DATETIME from ANIMAL_INS  order by ANIMAL_ID desc
```
#
>[흉부외과 또는 일반외과 의사 목록 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/132203) 
```
SELECT DR_NAME, DR_ID, MCDP_CD,  date_format(HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
from DOCTOR
where MCDP_CD = 'CS' or MCDP_CD='GS'
order by HIRE_YMD desc, DR_NAME
```
#
>[과일로 만든 아이스크림 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/133025) 
```
SELECT F_H.FLAVOR
FROM FIRST_HALF as F_H INNER JOIN ICECREAM_INFO as I_I
on F_H.FLAVOR = I_I.FLAVOR
where F_H.TOTAL_ORDER > 3000 and I_I.INGREDIENT_TYPE = 'fruit_based'
order by F_H.TOTAL_ORDER desc
```
