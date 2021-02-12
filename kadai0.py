# Python基本構文の学習用
#この課題は初学者さん用に基礎文法の理解度チェックするためのものです。
#ある程度理解している方は飛ばしてもかまいません。

## １ 変数の使い方
#変数を使って、「ねずこ」と「ぜんいつ」 は仲間ですとprint文を使って表示させてみよう
#なお、ねずこをname1、ぜんいつをname2として定義してください。
print("課題1")
name1 = 'ねずこ'
name2 = 'ぜんいつ'
print (name1 + 'と' + name2 + 'は仲間です')


## ２ if文の使い方
#１のソースを改造して、name2が敵キャラの「むざん」だった場合に
#仲間ではありませんと表示させてみよう。
print("\r\n課題2")
name1 = 'ねずこ'
name2 = 'むざん'
if name2 == 'むざん' :
    print('仲間ではありません')
else:
    print (name1 + 'と' + name2 + 'は仲間です')

## ３ 配列の使い方
#以下の配列に対して、キャラクター「ぜんいつ」を追加してみよう。
#appendを使うことで追加できます。
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append('ぜんいつ')


## ４ for文の使い方
#３のソースコードで使用したnameのキャラクターをfor文を使って
#１行に１キャラクター表示してみよう
print("\r\n課題4")
for character in name:
    print(character)


## ５　関数の使い方
#いままで作ったソースコードを全て関数化してみよう。
#関数化したら、関数を呼び出して結果が表示されることを確認してみよう。
def test1():
    if name2 == 'むざん' :
        print('仲間ではありません')
    else:
        print (name1 + 'と' + name2 + 'は仲間です')

def test2():
    name.append('ぜんいつ')

def test3():
    for character in name:
        print(character)

name1 = 'ねずこ'
name2 = 'むざん'
name=["たんじろう","ぎゆう","ねずこ","むざん"]

print("\r\n課題5")
test1()
test2()
test3()


## ６ 引数を使う関数の使い方
#以下のようにhikisuuの部分が引数です。引数は関数の外から変数を関数内に渡すことができます。
#このような引数を使う関数を作成してみよう。

#def test(hikisuu):

#【仕様】
#関数名：なんでも良い 【testにします】
#引数：キャラクターの名前を格納する変数　【characterにします】
#関数で行う処理：キャラクターのリスト（３、４で使ったもの）の中に、
#引数で入力されたキャラクター名が存在するか確認して結果をprint文で表示させる
#例）引数が「ぎゆう」→nmaeにぎゆうが存在する→ぎゆうは含まれますと表示
print("\r\n課題6")
def test(character):
    if character_name == 'ぎゆう':
        X = 1
    else:
        X = 0
    return X

character=["たんじろう","ぎゆう","ねずこ","むざん"]
character.append('ぜんいつ')
character.append('煉獄')
character.append('胡蝶')

for character_name in character:
    A = test(character)
    #print(str(A))
    if int(A) == 1:
        print('ぎゆうは含まれます')