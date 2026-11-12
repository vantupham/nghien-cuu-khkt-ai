"""Dùng khi KHÔNG triển khai bằng GitHub Actions.
Chạy:  python tools/dien_dia_chi.py https://ten-tai-khoan.github.io/so-nghien-cuu-ai ten-tai-khoan/so-nghien-cuu-ai
Lệnh thay __SITE_URL__ và __REPO__ trong mọi trang bằng địa chỉ thật."""
import sys, pathlib
url, repo = sys.argv[1].rstrip("/"), sys.argv[2]
goc = pathlib.Path(__file__).resolve().parent.parent
n = 0
for f in goc.rglob("*"):
    if f.suffix in {".html", ".xml", ".txt", ".webmanifest"} and ".git" not in f.parts:
        s = f.read_text(encoding="utf-8"); t = s.replace("__SITE_URL__", url).replace("__REPO__", repo)
        if t != s: f.write_text(t, encoding="utf-8"); n += 1
print("Đã cập nhật", n, "file")
