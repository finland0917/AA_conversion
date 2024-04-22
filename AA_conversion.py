from PIL import Image
import sys

# 濃い色から薄い色へと階調を表現するために、複数の文字を使用
ascii_chars = '@%#*+=-:. '

def image_to_ascii(image_path, output_width):
    
    # 画像を開く
    img = Image.open(image_path)
    
    # 画像のアスペクト比を維持してリサイズ
    aspect_ratio = img.width / img.heightｃ

    # 高さを計算
    output_height = int(output_width / aspect_ratio)

    # 画像を指定したサイズにリサイズ
    img = img.resize((output_width, output_height))
    
    # 画像をグレースケールに変換
    img = img.convert('L')
    
    # ピクセルの値をAA文字列に変換
    ascii_str = ''
    for y in range(output_height):
        for x in range(output_width):
            pixel_value = img.getpixel((x, y))
            # ピクセルの輝度値に基づいて適切な文字を選択
            ascii_str += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        ascii_str += '\n'  # 行の終わりで改行を追加
    
    return ascii_str

def main():
    # コマンドライン引数から入力ファイルのパスと出力の横幅を入力
    if len(sys.argv) != 3:
        print("例:python script.py input_image_path output_width")
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
