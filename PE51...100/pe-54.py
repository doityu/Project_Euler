# poker.txtには1000個のランダムな手札の組が含まれている. 
# 各行は10枚のカードからなる (スペースで区切られている): 最初の5枚がプレイヤー1の手札であり, 残りの5枚がプレイヤー2の手札である.
# 以下のことを仮定してよい
# ・全ての手札は正しい (使われない文字が出現しない. 同じカードは繰り返されない)
# ・各プレイヤーの手札は特に決まった順に並んでいるわけではない
# ・各勝負で勝敗は必ず決まる

# 1000回中プレイヤー1が勝つのは何回か? (訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい)
import sys
from enum import Enum
import collections

# 比較結果の種類
class COMPARIOSN_RESULT_KIND(Enum):
    HIGH = 0
    LOW  = 1
    SAME = 2

# カードの役の種類
class CARD_RANK(Enum):
    HIGH_CARD      = 0
    ONE_PAIR       = 1
    TWO_PAIRS      = 2
    THREE_KIND     = 3
    STRAIGHT       = 4
    FLUSH          = 5
    FULL_HOUSE     = 6
    FOUR_KIND      = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH    = 9
# カードの値
CARD_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
# カードのスーツ
CARD_SUIT = ['S', 'D', 'H', 'C']

# 何かしらエラーが起こった際に呼ぶ
def error(p1_card, p2_card):
    print("勝敗を決められません", p1_card, p2_card)
    sys.exit(1)

# 辞書の値からキーを取得
def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

# 値を比較しp1が大きいか返す
def compariosn_value(p1_counter, p2_counter, count):
    p1_value = get_keys_from_value(p1_counter, count)
    p2_value = get_keys_from_value(p2_counter, count)
    if(p1_value > p2_value):
        return COMPARIOSN_RESULT_KIND.HIGH
    elif(p1_value == p2_value):
        return COMPARIOSN_RESULT_KIND.SAME
    else:
        return COMPARIOSN_RESULT_KIND.LOW

# poker.txtからプレイヤー1と2の手札のリストを返す
def preparation():
    f = open("./pe-54_poker.txt", "r")
    data = f.read()
    f.close

    data_list = data.split("\n")
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(" ")

    p1_card_list = [[] for i in range(len(data_list))]
    p2_card_list = [[] for i in range(len(data_list))]

    for i in range(len(data_list)):
        for j in range(5):
            p1_card_list[i].append(data_list[i][j])
            p2_card_list[i].append(data_list[i][j + 5])
    return p1_card_list, p2_card_list

# 一番値が大きいカードを比べる。同じ場合は次に大きいカードを比べる。
# 以下同様に行い、プレイヤー1が値が大きいカードを持つ場合True
def is_max_value(p1_card, p2_card):
    p1_card_num = []
    p2_card_num = []

    # カードの値のみ摘出
    for i in range(len(p1_card)):
        p1_key = p1_card[i][:1]
        p1_card_num.append(CARD_VALUES[p1_key])
        p2_key = p2_card[i][:1]
        p2_card_num.append(CARD_VALUES[p2_key])
    # 降順にソート
    p1_card_num = sorted(p1_card_num, reverse=True)
    p2_card_num = sorted(p2_card_num, reverse=True)
    # 値の比較を行い、同じ場合は次の値をチェックする
    for i in range(len(p1_card_num)):
        if(p1_card_num[i] > p2_card_num[i]):
            return True
        elif(p1_card_num[i] < p2_card_num[i]):
            return False
    else:
        error(p1_card, p2_card)

# お互いの手札の役が同じ場合に呼ばれる役の中身を比較する
def get_compariosn_rank(p1_card, p2_card, rank):
    # 以下のランクのときは中身の大きさだけ比較する
    # ・役無し(ハイカード)
    # ・ストレート
    # ・フラッシュ
    # ・ストレートフラッシュ
    if(rank == CARD_RANK.HIGH_CARD 
    or rank == CARD_RANK.STRAIGHT 
    or rank == CARD_RANK.FLUSH 
    or rank == CARD_RANK.STRAIGHT_FLUSH):
        return is_max_value(p1_card, p2_card)
    
    # カードを値に分割
    card1_value = []
    card2_value = []
    for i in range(len(p1_card)):
        p1_key = p1_card[i][:1]
        card1_value.append(CARD_VALUES[p1_key])
        p2_key = p2_card[i][:1]
        card2_value.append(CARD_VALUES[p2_key])
    # 出現回数取得
    counter1 = collections.Counter(card1_value)
    counter2 = collections.Counter(card2_value)

    if(rank == CARD_RANK.FOUR_KIND):
        # フォーカードときは回数順に並んだ値の大きさだけ比較する
        result = compariosn_value(counter1, counter2, 4)
        if(result == COMPARIOSN_RESULT_KIND.HIGH):
            return True
        elif(result == COMPARIOSN_RESULT_KIND.SAME):
            result = compariosn_value(counter1, counter2, 1)
            if(result == COMPARIOSN_RESULT_KIND.HIGH):
                return True
            elif(result == COMPARIOSN_RESULT_KIND.LOW):
                return False
        else:
            return False
        error(p1_card, p2_card)
    elif(rank == CARD_RANK.FULL_HOUSE):
        # フルハウスのときも回数順に並んだ値の大きさだけ比較する
        result = compariosn_value(counter1, counter2, 3)
        if(result == COMPARIOSN_RESULT_KIND.HIGH):
            return True
        elif(result == COMPARIOSN_RESULT_KIND.SAME):
            result = compariosn_value(counter1, counter2, 2)
            if(result == COMPARIOSN_RESULT_KIND.HIGH):
                return True
            elif(result == COMPARIOSN_RESULT_KIND.LOW):
                return False
        else:
            return False
        error(p1_card, p2_card)
    elif(rank == CARD_RANK.THREE_KIND):
        # スリーカードのときは3枚ペアの値だけを比較
        result = compariosn_value(counter1, counter2, 3)
        if(result == COMPARIOSN_RESULT_KIND.HIGH):
            return True
        elif(result == COMPARIOSN_RESULT_KIND.LOW):
            return False
        else:
            # 同じカードは4枚しかないので同じになることはない
            error(p1_card, p2_card)

    elif(rank == CARD_RANK.TWO_PAIRS):
        result = compariosn_value(counter1, counter2, 2)
        if(result == COMPARIOSN_RESULT_KIND.HIGH):
            return True
        elif(result == COMPARIOSN_RESULT_KIND.SAME):
            result = compariosn_value(counter1, counter2, 1)
            if(result == COMPARIOSN_RESULT_KIND.HIGH):
                return True
            elif(result == COMPARIOSN_RESULT_KIND.LOW):
                return False
        else:
            return False

    elif(rank == CARD_RANK.ONE_PAIR):
        result = compariosn_value(counter1, counter2, 2)
        if(result == COMPARIOSN_RESULT_KIND.HIGH):
            return True
        elif(result == COMPARIOSN_RESULT_KIND.SAME):
            return is_max_value(p1_card, p2_card)
        else:
            return False
    else:
        error(p1_card, p2_card)

# カードの役を返す
def get_card_rank_and_value(card):
    # カードを値と絵柄に分割
    card_value = []
    card_value_num = []
    card_suit = []
    for c in card:
        card_value.append(c[:1])
        key = c[:1]
        card_value_num.append(CARD_VALUES[key])
        card_suit.append(c[1:])
    card_value_num = sorted(card_value_num, reverse=True)

    # ストレートに並んでいるか
    is_straight = False
    for i in range(1, len(card_value_num)):
        if(card_value_num[i-1] - card_value_num[i] != 1):
            break
    else:
        is_straight = True

    # カードの絵柄がすべて同じか
    is_flash = False
    for i in range(1, len(card_suit)):
        if(card_suit[i] != card_suit[i-1]):
            break
    else:
        is_flash = True

    # 下記の役か判定
    # ・ロイヤルストレートフラッシュ 
    # ・ストレートフラッシュ 
    # ・ストレート 
    # ・フラッシュ 
    if(is_straight and is_flash):
        if('A' in card_value):
            # ロイヤルストレートフラッシュ
            return CARD_RANK.ROYAL_FLUSH
        else:
            # ストレートフラッシュ
            return CARD_RANK.STRAIGHT_FLUSH
    elif(is_straight):
        # ストレート
        return CARD_RANK.STRAIGHT
    elif(is_flash):
        # フラッシュ
        return CARD_RANK.FLUSH

    # カードの値の出現回数を取得、出現回数順に並べる
    counter_list = collections.Counter(card_value)
    value_count = sorted(counter_list.values(), reverse=True)
    # 下記の役か判定
    # ・フォーカード
    # ・フルハウス
    # ・スリーカード
    # ・ツー・ペア
    # ・ワン・ペア
    if(value_count[0] == 4):
        # フォーカード
        return CARD_RANK.FOUR_KIND
    elif(value_count[0] == 3):
        if(value_count[1] == 2):
            # フルハウス
            return CARD_RANK.FULL_HOUSE
        else:
            # スリーカード
            return CARD_RANK.THREE_KIND
    elif(value_count[0] == 2):
        if(value_count[1] == 2):
            # ツー・ペア
            return CARD_RANK.TWO_PAIRS
        else:
            # ワン・ペア
            return CARD_RANK.ONE_PAIR
    else:
        # 役無し(ハイカード)
        return CARD_RANK.HIGH_CARD

# プレイヤー１の手札がプレイヤー2の手札に勝っているか判定する
def is_win_player1(p1_card, p2_card):
    p1_rank = get_card_rank_and_value(p1_card)
    p2_rank = get_card_rank_and_value(p2_card)
    # カードの役が大きければ勝ち
    if(p1_rank.value > p2_rank.value):
        return True
    elif(p1_rank.value == p2_rank.value):
        # カードの役が同じ場合、役を構成する中で値が最も大きい方が勝ち
        return get_compariosn_rank(p1_card, p2_card, p1_rank)
    else:
        return False

if __name__ == "__main__":
    p1_card_list, p2_card_list = preparation()

    p1_win = 0
    for i in range(len(p1_card_list)):
        if(is_win_player1(p1_card_list[i], p2_card_list[i])):
            p1_win += 1
    print(p1_win)
