import requests
import threading

user_id = input('에스크 아이디를 입력해주세요.')
message = input('메세지를 입력해주세요.')
trying = input('반복 횟수를 입력해주세요.')


def on():
    sess = requests.Session()
    r = sess.get(f'https://asked.kr/query.php?query=4&id={user_id}', headers={
        'X-Requested-With': 'XMLHttpRequest'}).json()
    print(
        f'{user_id}\n답변 완료 질문 갯수: {list(r)[0]}\n새질문 갯수: {list(r)[1]}\n거절질문 갯수: {list(r)[2]}')
    r = sess.get(f'https://asked.kr/{user_id}')
    r = sess.post('https://asked.kr/query.php?query=0', headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}, data={
        'id': user_id,
        'content': message,
        'makarong_bat': -1,
        'show_user': 0
    })
    print(r.text.lstrip().rstrip())


for i in range(int(trying)):
    threading.Thread(target=on, args=()).start()
