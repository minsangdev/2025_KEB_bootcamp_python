# Assignment
# while 안 쪽의 조건문을 줄이시오
# commit 수정
import random

drinks = ["위스키", "와인", "소주", "고량주"]
foods = ["초콜릿", "치즈", "삼겹살", "양꼬치"]

drinks.append("사케")
foods.append("광어회")
foods[0] = "낙곱새"
# drinks.append("데킬라")
# foods.append("소금")

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {foods[n]} 입니다')


menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i + 1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks) + 1}) 아무거나   {len(drinks) + 2}) 종료 : '


# f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : '
while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        print_menu(menu - 1)
    elif menu == 6:
        random_index = random.randint(0, len(drinks) - 1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]}입니다')
    elif menu == 7:
        print(f'다음에 또 오세요')
        break
