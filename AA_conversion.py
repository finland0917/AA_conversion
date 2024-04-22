from PIL import Image
import sys

# グレースケールに変換する際に使用する文字列（濃い→薄いの順）
# 濃い色から薄い色へと階調を表現するために、複数の文字を使用
ascii_chars = '@%#*+=-:. '

def image_to_ascii(image_path, output_width):
    # 画像を開く
    img = Image.open(image_path)
    
    # 画像のアスペクト比を維持してリサイズ
    aspect_ratio = img.width / img.height
    output_height = int(output_width / aspect_ratio)
    img = img.resize((output_width, output_height))
    
    # 画像をグレースケールに変換
    img = img.convert('L')
    
    # ピクセルの値をAA文字列に変換
    ascii_str = ''
    for y in range(output_height):
        for x in range(output_width):
            pixel_value = img.getpixel((x, y))
            # ピクセルの輝度値に基づいて適切な文字を選択
            # 0から255の輝度値を、0から文字列の長さ-1の範囲に変換
            # そして、対応する文字を選択してAA文字列に追加
            ascii_str += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        ascii_str += '\n'  # 行の終わりで改行を追加
    
    return ascii_str

def main():
    # コマンドライン引数から入力ファイルのパスと出力の横幅を取得
    if len(sys.argv) != 3:
        print("Usage: python script.py input_image_path output_width")
        return
    input_image_path = sys.argv[1]
    output_width = int(sys.argv[2])
    
    # AAに変換
    output_ascii = image_to_ascii(input_image_path, output_width)
    
    # AAをコンソールに表示
    print(output_ascii)

    # AAをテキストファイルに保存
    with open('output_ascii.txt', 'w') as f:
        f.write(output_ascii)

if __name__ == "__main__":
    main()
