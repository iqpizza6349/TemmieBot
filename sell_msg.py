import random

class sell():
    item = [
        "막대기", "장난감 칼", "튼튼한 장갑", "발레용 신발", "찢어진 공책", "그을린 팬", "빈 공책", "낡은 단검", "진짜 칼",
        "반창고", "빛바랜 리본", "남자다운 두건", "낡은 발레복", "흐린 안경", "테미 갑빠옷!!!", "얼룩진 치마", "카우보이 모자", "하트모양 로켓" , "로켓",
        "괴물 사탕", "거미 도넛", "거미 사이다", "버터스카치 파이", "달팽이 파이", "눈사람 조각", "나이스크림", "쌍고드름", "시나몬버니", "버려진 키슈", "멍멍샐러드", "우주식량", "크랩애플",
        "바다 홍차", "템플레이크", "컵라면", "핫도그...?", "핫캣", "정크푸드", "별 파르페", "글램버거", "전설의 영웅", "메타톤 얼굴 모양 스테이크", "허쉬퍼피", "감자칩", "나쁜 기억", "마지막 꿈",
        "펀치 카드", "짜증나는 개", "멍멍잔여물"
    ]
    result = ""

    def __init__(self):
        pass

    def msg(self):
        msg = random.randrange(49)
        self.result = self.item[msg]
        return self.result
