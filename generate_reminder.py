import random
from datetime import datetime, timedelta
from ics import Calendar, Event

today = datetime.now()
weekday = today.weekday()
is_holiday = weekday in [2, 6]  # 三=2, 日=6

brush_times = ["08:00", "20:00"] if is_holiday else ["07:00", "20:00"]
exercise_times = ["09:30"] if is_holiday else ["18:45"]

reminders = {
    "brush": {
        "gentle": [
            "開始一天之前，先讓口氣也醒來 ✦",
            "出門之前的儀式：來～去刷個牙吧！",
            "讓嘴巴清爽一點，才有心情開始今天的事 ✧",
            "精神恢復之前，先把牙齒清乾淨 ♡",
            "睡飽飽後來點泡沫，感覺會很清新～",
            "早上清爽的第一步，就是刷牙",
            "牙齒清乾淨，心情也比較輕盈～",
            "幫自己開啟清潔模式吧 ✦",
            "別忘了幫口氣也準備好今天的冒險",
            "清潔的起點，是今天的第一個小照顧"
        ],
        "neutral": [
            "早晚刷牙，讓自己維持清新節奏 ✧",
            "不管今天怎麼樣，口氣乾淨先拿到",
            "去刷個牙再開始你要做的事吧！",
            "口腔清潔完就可以進入下一段行程 ✨",
            "花一點點時間清潔，也是在照顧自己",
            "穩穩的生活習慣，從牙刷開始 ♡",
            "給自己一點節奏，從牙齒開始清理",
            "這是一個讓自己回到軌道的小動作",
            "刷牙是一種整理，也是種重新出發"
        ],
        "concerned": [
            "情緒跟不上也沒關係，刷牙當作切換模式",
            "即使累也讓口腔舒服一點，自己會比較放鬆",
            "這時候先照顧好口腔，會幫助你慢慢醒來",
            "累的時候就從最小的行動開始，像是刷牙",
            "你可以照自己的節奏刷牙，不急",
            "刷牙是一個不需要決定太多的安靜小事",
            "把注意力放在泡沫和水流，給自己一點喘息",
            "這是屬於你自己的照顧時間",
            "讓這幾分鐘單純一點，只刷牙就好"
        ]
    },
    "exercise": {
        "gentle": [
            "今天不用多，三分鐘踏步也夠意思 ✦",
            "你不需要做太多，三分鐘的踏步機就好 ✧",
            "小步也能走出節奏，上踏步機動一下吧～",
            "就當幫自己啟動身體，只要三分鐘也好",
            "從踏步機慢慢踩起來，不用追求厲害 ✦",
            "簡單踩幾分鐘，身體會回應你 ✨",
            "當成活動小儀式也行～只要你願意站上去",
            "今天也給身體一點回應，踏步機上見 ♡",
            "走一小段，給身體一點提示也不錯",
            "輕輕踩一下，不用負擔，也能啟動一點能量"
        ],
        "neutral": [
            "今天是運動時間，記得上踏步機踩一下 ✦",
            "準備開始動一動囉～三分鐘就好沒壓力",
            "你可以做到的，來～走起來吧",
            "有踏步機在，不如利用一下踩一波 ✧",
            "每天一點點，也能累積出健康✨",
            "運動日到了～讓踏步機幫你出個力",
            "即使只有三分鐘，身體也會記得你的努力",
            "幫自己踩個節奏，輕鬆不費力 ♫",
            "你願意開始，就已經是好事"
        ],
        "concerned": [
            "三分鐘可以嗎？只是簡單讓身體動起來",
            "你狀況不一定好，但踏步機會陪你慢慢來",
            "連續不動會讓人更累，我們就從機器開始",
            "即使身體很重，踩幾下也算照顧自己",
            "你不需要拼，只要願意站上去，就是行動",
            "不是訓練，只是讓身體知道你還在乎他",
            "動不了也沒關係，我們只做這一小段就停",
            "三分鐘是你能掌握的小步伐",
            "願意開始動一下，就很值得肯定",
            "今天也能有屬於自己的節奏，從踏步機開始"
        ]
    }
}

def choose_tone():
    return random.choice(["gentle", "neutral", "concerned"])

cal = Calendar()

for t in brush_times:
    tone = choose_tone()
    msg = random.choice(reminders["brush"][tone])
    e = Event()
    e.name = msg
    e.begin = datetime.combine(today.date(), datetime.strptime(t, "%H:%M").time())
    e.duration = timedelta(minutes=5)
    e.description = f"刷牙提醒 ✧（{tone}）"
    cal.events.add(e)

for t in exercise_times:
    tone = choose_tone()
    msg = random.choice(reminders["exercise"][tone])
    e = Event()
    e.name = msg
    e.begin = datetime.combine(today.date(), datetime.strptime(t, "%H:%M").time())
    e.duration = timedelta(minutes=5)
    e.description = f"運動提醒 ✦（{tone}）"
    cal.events.add(e)

with open("public/reminder.ics", "w", encoding="utf-8") as f:
    f.writelines(cal.serialize_iter())
EOF

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
