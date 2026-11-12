import json, os
from PIL import Image, ImageDraw, ImageFont
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
D = json.load(open(HERE / "data.json"))
OUT = str(HERE.parent / "assets" / "og") + "/"; os.makedirs(OUT, exist_ok=True)
F = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
f = lambda w, s: ImageFont.truetype(F % w, s)
INK, NAVY, MUTED, HL, PAPER, GRID = (30, 58, 158), (15, 27, 51), (82, 96, 122), (247, 225, 75), (242, 245, 249), (221, 229, 240)

def logo(d, x, y, s=1.6):
    k = lambda v: v * s
    d.rounded_rectangle([x + k(4), y + k(3), x + k(25), y + k(27)], radius=k(2), fill="white", outline=INK, width=int(k(2)))
    d.line([x + k(9), y + k(3), x + k(9), y + k(27)], fill=(140, 155, 210), width=int(k(1.5)))
    for (a, b), c in [((17, 12), INK), ((13, 19), INK), ((21, 19), HL)]:
        d.ellipse([x + k(a - 2.2), y + k(b - 2.2), x + k(a + 2.2), y + k(b + 2.2)], fill=c, outline=INK)
    for p in [(17, 12, 13, 19), (17, 12, 21, 19), (13, 19, 21, 19)]:
        d.line([x + k(p[0]), y + k(p[1]), x + k(p[2]), y + k(p[3])], fill=INK, width=2)

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def make(name, title, sub, tags):
    im = Image.new("RGB", (1200, 630), PAPER); d = ImageDraw.Draw(im)
    for x in range(0, 1200, 30): d.line([x, 0, x, 630], fill=GRID)
    for y in range(0, 630, 30): d.line([0, y, 1200, y], fill=GRID)
    d.rectangle([0, 0, 1200, 10], fill=INK)
    d.line([92, 10, 92, 630], fill=(150, 165, 215), width=3)
    logo(d, 120, 44); d.text((178, 52), "Sổ Nghiên Cứu AI", font=f("Bold", 30), fill=INK)
    size = 68
    while True:
        ft = f("ExtraBold", size); lines = wrap(d, title, ft, 960)
        if len(lines) <= 3 or size <= 44: break
        size -= 4
    y = 150
    for ln in lines:
        d.text((120, y), ln, font=ft, fill=NAVY); y += int(size * 1.18)
    d.rectangle([120, y + 16, 300, y + 28], fill=HL)
    y += 44
    fs = f("Medium", 28)
    for ln in wrap(d, sub, fs, 960)[:2]:
        d.text((120, y), ln, font=fs, fill=MUTED); y += 40
    x = 120; ftag = f("SemiBold", 24)
    for t in tags:
        w = d.textlength(t, font=ftag) + 36
        d.rounded_rectangle([x, 540, x + w, 584], radius=22, fill="white", outline=INK, width=2)
        d.text((x + 18, 548), t, font=ftag, fill=INK); x += w + 14
    im = im.quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    im.save(OUT + name + ".png", optimize=True)

CODE = {"ROBO": "Rô bốt và máy thông minh", "SFTD": "Phần mềm"}
make("trang-chu", "Học làm nghiên cứu AI như một nhà khoa học thật", "10 dự án mẫu, notebook Colab và công cụ luyện thi KHKT cho học sinh THCS, THPT", ["Miễn phí", "10 dự án", "Colab"])
for p in D["PROJECTS"]:
    make("du-an-" + p["id"], p["title"], p["short"], [p["code"], f"Độ khó {p['level']}/3", f"{p['weeks']} tuần", "Notebook Colab"])
make("du-an", "10 đề tài nghiên cứu khoa học về trí tuệ nhân tạo", "Câu hỏi, giả thuyết, dữ liệu, lộ trình và mã nguồn chạy được cho học sinh", ["Rô bốt, máy thông minh", "Phần mềm"])
make("ky-nang", "10 kỹ năng của một nhà khoa học thực thụ", "Tự đánh giá, bài luyện ngay và thử thách tư duy khoa học", ["Tự đánh giá", "Thử thách"])
make("viet-bao-cao", "Cách viết báo cáo dự án khoa học kỹ thuật", "Bố cục, số trang, câu mở đầu, lỗi hay gặp và tóm tắt 250 từ", ["Báo cáo", "Tóm tắt", "APA"])
make("dung-ai-dung-cach", "Dùng AI trong dự án KHKT: được và không được", "Nguyên tắc dùng AI tạo sinh có kiểm soát và cách ghi nhật ký câu lệnh", ["Liêm chính", "Nhật ký prompt"])
make("phuong-phap", "Quy trình 8 bước làm dự án nghiên cứu AI", "Từ quan sát vấn đề đến trình bày kết quả, kèm hồ sơ và tiêu chí chấm", ["8 bước", "Tiêu chí chấm"])
make("lich-thi", "Lịch thi khoa học kỹ thuật trong một năm học", "Cấp trường, cấp tỉnh, cấp quốc gia và Regeneron ISEF", ["Chu kỳ năm", "Kế hoạch ngược"])
make("hoi-dap", "Hỏi đáp về cuộc thi KHKT và dự án AI", "Lớp mấy được thi, lĩnh vực nào, có được dùng ChatGPT, làm mất bao lâu", ["12 câu hỏi"])

# biểu tượng
ic = str(HERE.parent / "assets") + "/"
for size, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    im = Image.new("RGB", (size, size), PAPER); d = ImageDraw.Draw(im)
    s = size / 30 * 0.9; off = (size - 30 * s) / 2
    logo(d, off, off, s); im.save(ic + name, optimize=True)
print("ok", len(os.listdir(OUT)))
