import requests
import pandas as pd

URL: str = "https://api.pjsek.ai/database/master/musics?$limit=2048"
hiragana_gyou: dict = {
    "あ": "あ",
    "い": "い",
    "う": "う",
    "え": "え",
    "お": "お",
    "か": "か",
    "が": "か",
    "き": "き",
    "ぎ": "き",
    "く": "く",
    "ぐ": "く",
    "け": "け",
    "げ": "け",
    "こ": "こ",
    "ご": "こ",
    "さ": "さ",
    "ざ": "さ",
    "し": "し",
    "じ": "し",
    "す": "す",
    "ず": "す",
    "せ": "せ",
    "ぜ": "せ",
    "そ": "そ",
    "ぞ": "そ",
    "た": "た",
    "だ": "た",
    "ち": "ち",
    "ぢ": "ち",
    "つ": "つ",
    "づ": "つ",
    "て": "て",
    "で": "て",
    "と": "と",
    "ど": "と",
    "な": "な",
    "に": "に",
    "ぬ": "ぬ",
    "ね": "ね",
    "の": "の",
    "は": "は",
    "ば": "は",
    "ぱ": "は",
    "ひ": "ひ",
    "び": "ひ",
    "ぴ": "ひ",
    "ふ": "ふ",
    "ぶ": "ふ",
    "ぷ": "ふ",
    "へ": "へ",
    "べ": "へ",
    "ぺ": "へ",
    "ほ": "ほ",
    "ぼ": "ほ",
    "ぽ": "ほ",
    "ま": "ま",
    "み": "み",
    "む": "む",
    "め": "め",
    "も": "も",
    "や": "や",
    "ゆ": "ゆ",
    "よ": "よ",
    "ら": "ら",
    "り": "り",
    "る": "る",
    "れ": "れ",
    "ろ": "ろ",
    "わ": "わ",
    "ヴ": "う",
}


def main():
    r = requests.get(URL)
    data = r.json()["data"]
    df = pd.DataFrame(data)[["id", "title", "pronunciation"]]
    sorted_df = df.sort_values("pronunciation")
    sorted_df["label"] = sorted_df.pronunciation.map(lambda x: hiragana_gyou.get(x[0]))
    labeled_df = sorted_df.sort_values(["label", "pronunciation"])
    labeled_df["index"] = list(range(1, len(labeled_df) + 1))
    output_df = labeled_df[["id", "index", "title", "pronunciation", "label"]]
    output_df.to_csv("music_list.csv", index=False)


if __name__ == "__main__":
    main()
