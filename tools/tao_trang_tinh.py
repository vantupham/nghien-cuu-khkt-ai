# Tạo lại các trang tĩnh SEO từ dữ liệu trong index.html.
# Cách chạy (từ thư mục gốc):  node tools/trich_du_lieu.js  &&  python tools/tao_trang_tinh.py  &&  python tools/tao_anh_chia_se.py
import json, os, html, datetime, shutil
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
D = json.load(open(HERE / "data.json"))
SITE = str(HERE.parent)
U = "__SITE_URL__"            # GitHub Actions thay bằng địa chỉ thật, ví dụ https://ten.github.io/so-nghien-cuu-ai
REPO = "__REPO__"             # GitHub Actions thay bằng ten-tai-khoan/ten-repo
BRAND = "Sổ Nghiên Cứu AI"
TODAY = datetime.date.today().isoformat()
e = html.escape
CODE_VI = {"ROBO": "Rô bốt và máy thông minh", "SFTD": "Phần mềm"}

CSS = """
:root{--paper:#F2F5F9;--grid:#DDE5F0;--ink:#1E3A9E;--ink-soft:#4A63B8;--text:#0F1B33;--muted:#52607A;--hl:#F7E14B;--red:#C8303B;--line:#C9D4E5;
--hand:'Patrick Hand','Segoe Print','Bradley Hand','Chalkboard SE','Comic Sans MS',cursive;--sans:'Be Vietnam Pro',system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);font-size:17px;line-height:1.65;background-color:var(--paper);
background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:24px 24px}
a{color:var(--ink)}:focus-visible{outline:3px solid var(--ink);outline-offset:2px}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header{background:rgba(242,245,249,.95);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
header .wrap{display:flex;align-items:center;gap:16px;min-height:60px;flex-wrap:wrap}
.brand{display:flex;gap:10px;align-items:center;font-weight:800;text-decoration:none;color:var(--text)}
header nav{display:flex;gap:2px;flex-wrap:wrap;margin-left:auto}
header nav a{text-decoration:none;color:var(--muted);font-weight:600;font-size:14.5px;padding:6px 9px;border-radius:8px}
header nav a:hover,header nav a[aria-current]{color:var(--ink);background:#E3E9F7}
@media(max-width:700px){header{position:static}header nav{flex-wrap:nowrap;overflow-x:auto;width:100%;margin-left:0;padding-bottom:6px}header nav a{white-space:nowrap}}
main{padding:28px 0 64px}
.crumb{font-size:14px;color:var(--muted);margin-bottom:14px}.crumb a{color:var(--muted)}
h1{font-size:clamp(30px,4.6vw,48px);line-height:1.15;letter-spacing:-.02em;margin:0 0 .4em;font-weight:800}
h2{font-size:clamp(23px,3vw,30px);line-height:1.25;letter-spacing:-.01em;margin:1.8em 0 .5em;font-weight:800}
h3{font-size:19px;margin:1.2em 0 .3em}
.lead{font-size:19px;color:var(--muted);max-width:66ch}
.sheet{background:#fff;border:1px solid var(--line);border-radius:6px;padding:22px 24px;margin:16px 0}
.page{position:relative;background:#fff;border:1px solid var(--line);border-radius:4px;padding:20px 22px 20px 58px;background-image:linear-gradient(transparent 31px,#E4EAF4 32px);background-size:100% 32px;background-position:0 14px}
.page::before{content:"";position:absolute;left:40px;top:0;bottom:0;width:2px;background:var(--ink-soft);opacity:.35}
.q{font-family:var(--hand);color:var(--ink);font-size:25px;line-height:32px}
.meta{font-family:var(--hand);color:var(--muted);font-size:19px;line-height:32px}
.note{font-family:var(--hand);color:var(--ink);font-size:20px;line-height:1.35}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}
.chip{font-size:13.5px;font-weight:600;padding:2px 11px;border-radius:999px;border:1px solid var(--line);background:#F7F9FC;color:var(--muted)}
.chip.code{border-color:var(--ink-soft);color:var(--ink);background:#EEF2FC}
dl.kv{display:grid;grid-template-columns:180px 1fr;margin:0;border-top:1px solid var(--line)}
dl.kv dt,dl.kv dd{margin:0;padding:12px 0;border-bottom:1px solid var(--line)}dl.kv dt{font-weight:700;padding-right:16px}
@media(max-width:640px){dl.kv{grid-template-columns:1fr}dl.kv dt{border-bottom:0;padding-bottom:0}}
ol.steps{padding-left:0;list-style:none;counter-reset:s}ol.steps li{counter-increment:s;display:grid;grid-template-columns:44px 1fr;padding:10px 0;border-bottom:1px dashed var(--line)}
ol.steps li::before{content:counter(s);font-size:24px;font-weight:800;color:var(--ink)}
.btn{display:inline-flex;align-items:center;border:2px solid var(--ink);background:var(--ink);color:#fff;font-weight:700;padding:9px 18px;border-radius:999px;text-decoration:none;font-size:15px}
.btn.ghost{background:transparent;color:var(--ink)}.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.cta{border:2px solid var(--ink);background:#F6F8FD;border-radius:6px;padding:18px 20px;margin:24px 0;display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between;align-items:center}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px;margin-top:14px}
.card{display:block;background:#fff;border:1px solid var(--line);border-left:4px solid var(--ink);border-radius:4px;padding:16px 18px;text-decoration:none;color:var(--text)}
.card:hover{border-color:var(--ink)}.card strong{display:block;font-size:17px;margin-bottom:4px}.card span{color:var(--muted);font-size:15px}
.faq details{background:#fff;border:1px solid var(--line);border-radius:6px;padding:14px 18px;margin:10px 0}.faq summary{font-weight:700;cursor:pointer}
.mark{background:linear-gradient(transparent 55%,var(--hl) 55%,var(--hl) 92%,transparent 92%)}
table{border-collapse:collapse;width:100%;font-size:15px;background:#fff}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{background:#F1F4FA}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--muted);font-size:14.5px;background:var(--paper)}
footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}footer h2{font-size:15px;margin:0 0 6px;color:var(--text)}
footer ul{list-style:none;padding:0;margin:0}footer li{margin:3px 0}footer a{color:var(--muted)}
"""

LOGO = '<svg width="28" height="28" viewBox="0 0 30 30" aria-hidden="true"><rect x="4" y="3" width="21" height="24" rx="2" fill="#fff" stroke="#1E3A9E" stroke-width="2"/><path d="M9 3v24" stroke="#1E3A9E" stroke-width="1.5" opacity=".5"/><circle cx="17" cy="12" r="2.2" fill="#1E3A9E"/><circle cx="13" cy="19" r="2.2" fill="#1E3A9E"/><circle cx="21" cy="19" r="2.2" fill="#F7E14B" stroke="#1E3A9E" stroke-width="1.2"/><path d="M17 12l-4 7M17 12l4 7M13 19h8" stroke="#1E3A9E" stroke-width="1.3"/></svg>'

NAV = [("du-an/", "10 dự án"), ("ky-nang/", "Kỹ năng"), ("viet-bao-cao/", "Viết báo cáo"), ("dung-ai-dung-cach/", "Dùng AI đúng cách"),
       ("phuong-phap/", "Phương pháp"), ("lich-thi/", "Lịch thi"), ("hoi-dap/", "Hỏi đáp")]

def jsonld(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>"

def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": U + "/" + p} for i, (n, p) in enumerate(items)]}

def page(path, title, desc, body, og, ld=(), crumbs=(), current=None):
    depth = path.count("/")
    r = "../" * depth
    canon = U + "/" + path
    nav = "".join(f'<a href="{r}{p}"{" aria-current=\"page\"" if p == current else ""}>{t}</a>' for p, t in NAV)
    cr = ""
    if crumbs:
        cr = '<nav class="crumb" aria-label="Đường dẫn"><a href="' + r + '">Trang chủ</a>' + "".join(
            f' › <a href="{r}{p}">{e(n)}</a>' if i < len(crumbs) - 1 else f' › <span>{e(n)}</span>' for i, (n, p) in enumerate(crumbs)) + "</nav>"
        ld = list(ld) + [breadcrumb([("Trang chủ", "")] + list(crumbs))]
    proj_links = "".join(f'<li><a href="{r}du-an/{p["id"]}/">{e(p["title"])}</a></li>' for p in D["PROJECTS"])
    sec_links = "".join(f'<li><a href="{r}{p}">{t}</a></li>' for p, t in NAV)
    doc = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#1E3A9E">
<meta property="og:type" content="{'article' if path.startswith('du-an/') and depth == 2 else 'website'}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{U}/assets/og/{og}.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{U}/assets/og/{og}.png">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}assets/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&family=Patrick+Hand&display=swap&subset=vietnamese" rel="stylesheet">
<style>{CSS}</style>
{"".join(jsonld(x) for x in ld)}
</head>
<body>
<header><div class="wrap"><a class="brand" href="{r}">{LOGO}{BRAND}</a><nav aria-label="Mục chính">{nav}</nav></div></header>
<main class="wrap">
{cr}
{body}
</main>
<footer><div class="wrap">
<div class="cols"><div><h2>{BRAND}</h2><p>Tài nguyên học tập mở giúp học sinh THCS, THPT trên cả nước luyện làm nghiên cứu khoa học kỹ thuật về trí tuệ nhân tạo.</p><p><a href="{r}">Mở công cụ tương tác</a></p></div>
<div><h2>Hướng dẫn</h2><ul>{sec_links}</ul></div><div><h2>Dự án mẫu</h2><ul>{proj_links}</ul></div></div>
<p style="margin-top:18px">Nội dung về cuộc thi được tổng hợp theo thông lệ chung; quy định cụ thể thay đổi theo từng năm và địa phương, hãy đối chiếu văn bản mới nhất của trường, Sở GD&amp;ĐT và Bộ GD&amp;ĐT. Dự án mẫu chỉ để luyện tập.</p>
</div></footer>
</body>
</html>
"""
    out = os.path.join(SITE, path, "index.html") if path else os.path.join(SITE, "index.html")
    if path.endswith(".html"): out = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(doc)
    return canon

PAGES = []   # (path, og) cho sitemap
def add(path, og, *a, **k):
    page(path, *a, og=og, **k); PAGES.append(path)

P = D["PROJECTS"]
def nbf(p): return f"{P.index(p)+1:02d}-{p['id']}.ipynb"
LV = {1: "dễ bắt đầu", 2: "trung bình", 3: "nâng cao"}

# ---------- trang từng dự án ----------
for i, p in enumerate(P):
    path = f"du-an/{p['id']}/"
    r = "../../"
    rel = [q for q in P if q["id"] != p["id"] and (q["code"] == p["code"])][:3]
    title = f"{p['title']} | Đề tài KHKT AI" if len(p['title']) <= 48 else f"{p['title']} | KHKT AI"
    desc = f"Đề tài KHKT mẫu: {p['short']} Có giả thuyết, lộ trình {p['weeks']} tuần, notebook Colab."
    if len(desc) > 160: desc = f"{p['short']} Có giả thuyết, lộ trình {p['weeks']} tuần, notebook Colab."
    if len(desc) > 160: desc = f"{p['short']} Kèm lộ trình và notebook Colab."
    body = f"""
<div class="chips"><span class="chip code">{p['code']}, {e(p['sub'])}</span><span class="chip">{CODE_VI[p['code']]}</span><span class="chip">Độ khó {p['level']}/3, {LV[p['level']]}</span><span class="chip">Khoảng {p['weeks']} tuần</span><span class="chip">{'Cần phần cứng' if p['hw'] else 'Chỉ cần máy tính'}</span></div>
<h1>{e(p['title'])}</h1>
<p class="lead">{e(p['short'])}</p>
<div class="page"><div class="meta">Câu hỏi nghiên cứu:</div><p class="q" style="margin:0">{e(p['q'])}</p><div class="meta">Giả thuyết: {e(p['hyp'])}</div></div>
<h2>Thiết kế nghiên cứu</h2>
<dl class="kv"><dt>Dữ liệu</dt><dd>{e(p['data'])}</dd><dt>Phương pháp</dt><dd>{e(p['method'])}</dd><dt>Cách đo kết quả</dt><dd>{e(p['metric'])}</dd><dt>Công cụ</dt><dd>{e(p['tools'])}</dd><dt>Đạo đức và an toàn</dt><dd>{e(p['ethics'])}</dd></dl>
<div class="cta"><div style="flex:1 1 320px"><h2 style="margin:0 0 4px;font-size:22px">Notebook Colab chạy được</h2><p style="margin:0;color:var(--muted)">{e(p['nbData'])} Có mô hình đối chứng, cách chia dữ liệu đúng, phần đánh giá và bài tập tự làm.</p></div>
<div class="row"><a class="btn" href="https://colab.research.google.com/github/{REPO}/blob/main/notebooks/{nbf(p)}" rel="noopener">Mở trên Google Colab</a><a class="btn ghost" href="{r}notebooks/{nbf(p)}" download>Tải notebook</a></div></div>
<h2>Lộ trình thực hiện</h2>
<ol class="steps">{''.join(f'<li><span>{e(m)}</span></li>' for m in p['ms'])}</ol>
<h2>Hướng tạo tính mới</h2>
{''.join(f'<p class="note">{e(n)}</p>' for n in p['novelty'])}
<p>Đây là dự án mẫu để luyện tập. Dự án dự thi phải là kết quả nghiên cứu của chính em, chưa công bố ở cuộc thi nào, và điểm mới phải là của em.</p>
<div class="cta"><p style="margin:0;flex:1 1 300px">Theo dõi tiến độ từng tuần, tự chấm theo tiêu chí giám khảo và luyện phỏng vấn cho dự án này bằng công cụ tương tác.</p><a class="btn" href="{r}#da-{p['id']}">Mở công cụ cho dự án này</a></div>
<h2>Dự án cùng lĩnh vực</h2>
<div class="cards">{''.join(f'<a class="card" href="{r}du-an/{q["id"]}/"><strong>{e(q["title"])}</strong><span>{e(q["short"])}</span></a>' for q in rel)}</div>
"""
    ld = [{"@context": "https://schema.org", "@type": "LearningResource", "name": p["title"], "description": desc, "url": U + "/" + path,
           "image": f"{U}/assets/og/du-an-{p['id']}.png", "inLanguage": "vi", "isAccessibleForFree": True,
           "learningResourceType": "Dự án nghiên cứu mẫu", "educationalLevel": "Trung học cơ sở, Trung học phổ thông",
           "timeRequired": f"P{p['weeks']}W", "teaches": [p["sub"], "Thiết kế thí nghiệm", "Đánh giá mô hình học máy"],
           "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
           "about": CODE_VI[p["code"]], "dateModified": TODAY,
           "isPartOf": {"@type": "WebSite", "name": BRAND, "url": U + "/"}}]
    add(path, f"du-an-{p['id']}", title, desc, body, ld=ld, crumbs=[("10 dự án", "du-an/"), (p["title"], path)], current="du-an/")

# ---------- danh sách dự án ----------
body = f"""<h1>10 đề tài nghiên cứu khoa học về trí tuệ nhân tạo cho học sinh</h1>
<p class="lead">Mỗi đề tài là một khung luyện tập đầy đủ: câu hỏi nghiên cứu, giả thuyết, dữ liệu, phương pháp, cách đo, lộ trình theo tuần và notebook Google Colab chạy được. Phù hợp học sinh lớp 8 đến 12 chuẩn bị thi khoa học kỹ thuật các cấp.</p>
{''.join(f'<h2 style="font-size:24px">{CODE_VI[c]}</h2><div class="cards">' + ''.join(f'<a class="card" href="{q["id"]}/"><strong>{e(q["title"])}</strong><span>{e(q["short"])} Độ khó {q["level"]}/3, khoảng {q["weeks"]} tuần.</span></a>' for q in P if q["code"] == c) + '</div>' for c in ["ROBO", "SFTD"])}
<div class="cta"><p style="margin:0;flex:1 1 300px">Chưa chọn được đề tài? Xưởng đề tài ghép một vấn đề ở địa phương em với một kỹ thuật AI để ra câu hỏi nghiên cứu.</p><a class="btn" href="../#cong-cu">Mở Xưởng đề tài</a></div>"""
ld = [{"@context": "https://schema.org", "@type": "ItemList", "name": "10 đề tài KHKT về AI cho học sinh",
       "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{U}/du-an/{q['id']}/", "name": q["title"]} for i, q in enumerate(P)]}]
add("du-an/", "du-an", "10 đề tài nghiên cứu khoa học AI cho học sinh, có mã nguồn Colab",
    "10 ý tưởng đề tài KHKT về trí tuệ nhân tạo cho học sinh THCS, THPT: nhận diện bệnh lá, dự báo ngập, lừa đảo, ngôn ngữ ký hiệu... kèm lộ trình và notebook Colab.",
    body, ld=ld, crumbs=[("10 dự án", "du-an/")], current="du-an/")

# ---------- kỹ năng ----------
S = D["SKILLS"]
body = f"""<h1>10 kỹ năng nghiên cứu khoa học của một nhà khoa học thực thụ</h1>
<p class="lead">Những kỹ năng người làm nghiên cứu dùng hằng ngày, tóm tắt cho học sinh chuẩn bị thi khoa học kỹ thuật. Mỗi kỹ năng có thói quen cần rèn, một bài luyện ngay và bốn mức để tự đánh giá.</p>
{''.join(f'''<section class="sheet"><h2 style="margin-top:0;font-size:24px">{k+1}. {e(s['n'])}</h2><p>{e(s['sum'])}</p>
<h3>Nhà khoa học thực thụ thường</h3><ul>{''.join(f"<li>{e(h)}</li>" for h in s['habits'])}</ul>
<p class="note">Luyện ngay: {e(s['drill'])}</p>
<table><thead><tr>{''.join(f"<th>{k2+1}. {e(n)}</th>" for k2, n in enumerate(D['LV_NAMES']))}</tr></thead><tbody><tr>{''.join(f"<td>{e(x)}</td>" for x in s['lv'])}</tr></tbody></table></section>''' for k, s in enumerate(S))}
<h2>Thử thách tư duy khoa học</h2>
<p>Tám tình huống có lỗi hay gặp trong dự án AI của học sinh: rò rỉ dữ liệu, dữ liệu mất cân bằng, nhầm tương quan với nhân quả, chọn mô hình trên tập kiểm tra, kết luận từ một lần chạy, thiên lệch dữ liệu, thiếu đối chứng và trích dẫn sai cách.</p>
<div class="cta"><p style="margin:0;flex:1 1 300px">Tự đánh giá trên bánh xe kỹ năng và làm thử thách có chấm điểm.</p><a class="btn" href="../#ky-nang">Mở bánh xe kỹ năng</a></div>"""
add("ky-nang/", "ky-nang", "10 kỹ năng nghiên cứu khoa học học sinh cần có khi thi KHKT",
    "Tóm tắt 10 kỹ năng của nhà khoa học: đặt câu hỏi, đọc tài liệu, tư duy phản biện, thiết kế thí nghiệm, thống kê, lập trình, ghi chép, trình bày, liêm chính, hợp tác.",
    body, crumbs=[("Kỹ năng nghiên cứu", "ky-nang/")], current="ky-nang/")

# ---------- viết báo cáo ----------
SE = D["SECTIONS"]
body = f"""<h1>Cách viết báo cáo dự án khoa học kỹ thuật</h1>
<p class="lead">Bố cục chuẩn của một báo cáo nghiên cứu, số trang nên dành cho từng phần, cách mở đầu và các lỗi giám khảo hay bắt. Áp dụng được cho báo cáo dự thi KHKT cấp trường, cấp tỉnh, cấp quốc gia.</p>
<h2>Phân bổ trang gợi ý cho báo cáo 15 trang</h2>
<table><thead><tr><th>Phần</th><th>Số trang</th><th>Mục đích</th></tr></thead><tbody>{''.join(f"<tr><td><strong>{e(s['n'])}</strong></td><td>{s['f']*15:.1f}</td><td>{e(s['purpose'])}</td></tr>" for s in SE)}</tbody></table>
<p style="color:var(--muted);font-size:15px">Hãy theo giới hạn số trang trong quy định của cuộc thi em tham dự; bảng chỉ là tỉ lệ gợi ý.</p>
{''.join(f'''<section class="sheet"><h2 style="margin-top:0;font-size:22px">{e(s['n'])}</h2><p>{e(s['purpose'])}</p><p class="note">{e(s['starter'])}</p><p style="color:var(--red)">{e(s['pit'])}</p><p style="color:var(--muted);font-size:15px">Độ dài gợi ý: {s['w'][0]} đến {s['w'][1]} từ.</p></section>''' for s in SE)}
<h2>Tóm tắt 250 từ theo năm phần</h2>
<ol class="steps"><li><span><strong>Bối cảnh và vấn đề:</strong> vấn đề gì, ở đâu, nghiêm trọng thế nào.</span></li><li><span><strong>Mục tiêu:</strong> dự án trả lời câu hỏi gì.</span></li><li><span><strong>Phương pháp:</strong> dữ liệu, mô hình, đối chứng, cách đo.</span></li><li><span><strong>Kết quả:</strong> các con số chính, so với đối chứng.</span></li><li><span><strong>Kết luận:</strong> ý nghĩa và ứng dụng.</span></li></ol>
<div class="cta"><p style="margin:0;flex:1 1 300px">Viết nháp từng phần và được kiểm tra ngay những gì còn thiếu, luyện văn phong khoa học, tạo trích dẫn APA.</p><a class="btn" href="../#bao-cao">Mở xưởng viết báo cáo</a></div>"""
add("viet-bao-cao/", "viet-bao-cao", "Cách viết báo cáo dự án KHKT: bố cục, số trang, lỗi thường gặp",
    "Hướng dẫn viết báo cáo nghiên cứu khoa học kỹ thuật cho học sinh: bố cục 9 phần, phân bổ trang, câu mở đầu, lỗi hay gặp, cách viết tóm tắt 250 từ.",
    body, crumbs=[("Viết báo cáo", "viet-bao-cao/")], current="viet-bao-cao/")

# ---------- dùng AI đúng cách ----------
A = D["AI_RULES"]
grp = {"y": "Được làm, có điều kiện (ghi câu lệnh vào sổ)", "r": "Không nên làm, thường bị cấm", "g": "Được làm"}
body = f"""<h1>Dùng AI trong dự án KHKT: được làm gì, không được làm gì</h1>
<p class="lead">Nhiều Sở GD&amp;ĐT đã đưa hướng dẫn sử dụng AI tạo sinh vào cuộc thi khoa học kỹ thuật. Nguyên tắc chung: AI là công cụ hỗ trợ có kiểm soát, không làm thay học sinh, và mọi câu lệnh đã dùng phải được ghi lại. Dưới đây là tổng hợp các nguyên tắc phổ biến; hãy đối chiếu văn bản của nơi em dự thi.</p>
{''.join(f'<h2>{grp[v]}</h2><table><tbody>' + ''.join(f"<tr><td style='width:45%'><strong>{e(x['s'])}</strong></td><td>{e(x['why'])}</td></tr>" for x in A if x['v'] == v) + '</tbody></table>' for v in ['y', 'r', 'g'])}
<h2>Ghi nhật ký câu lệnh thế nào?</h2>
<p>Mỗi lần dùng AI, ghi: ngày, công cụ, mục đích, câu lệnh nguyên văn, em dùng kết quả vào đâu, và em đã kiểm chứng hoặc sửa gì. Với mã nguồn do AI gợi ý, đánh dấu rõ đoạn mã đó trong chương trình.</p>
<div class="cta"><p style="margin:0;flex:1 1 300px">Tra nhanh tình huống bằng đèn giao thông AI và ghi nhật ký câu lệnh ngay trên trình duyệt.</p><a class="btn" href="../#cong-cu">Mở đèn giao thông AI</a></div>"""
add("dung-ai-dung-cach/", "dung-ai-dung-cach", "Dùng ChatGPT, AI trong dự án KHKT: được và không được làm gì",
    "Tổng hợp nguyên tắc dùng AI tạo sinh trong cuộc thi khoa học kỹ thuật học sinh: việc được phép có điều kiện, việc thường bị cấm, cách ghi nhật ký câu lệnh.",
    body, crumbs=[("Dùng AI đúng cách", "dung-ai-dung-cach/")], current="dung-ai-dung-cach/")

# ---------- phương pháp ----------
body = f"""<h1>Quy trình 8 bước làm dự án nghiên cứu khoa học về AI</h1>
<p class="lead">Từ quan sát vấn đề đến trình bày kết quả: quy trình áp dụng cho mọi dự án trí tuệ nhân tạo của học sinh, cùng các thành phần hồ sơ dự thi thường gặp.</p>
<ol class="steps">{''.join(f"<li><span><strong>{e(m[0])}.</strong> {e(m[1])}</span></li>" for m in D['METHOD'])}</ol>
<h2>Hồ sơ dự thi thường gồm</h2><ul>{''.join(f"<li>{e(x)}</li>" for x in D['DOSSIER'])}</ul>
<h2>Tiêu chí chấm tham khảo</h2>
<table><thead><tr><th>Tiêu chí</th><th>Điểm</th><th>Giám khảo xem</th></tr></thead><tbody>{''.join(f"<tr><td><strong>{e(c['n'])}</strong></td><td>{c['max']}</td><td>{'; '.join(e(x) for x in c['items'])}</td></tr>" for c in D['CRITS'])}</tbody></table>
<p style="color:var(--muted);font-size:15px">Khung theo tiêu chí chấm của ISEF; thang điểm từng cuộc thi có thể khác.</p>
<h2>Mẫu giấy tờ in được</h2><p>Kế hoạch nghiên cứu để giáo viên duyệt, phiếu đồng ý tham gia nghiên cứu, trang sổ nghiên cứu, phiếu góp ý. Điền thông tin một lần và in trực tiếp từ công cụ.</p>
<div class="cta"><p style="margin:0;flex:1 1 300px">Xem vòng tròn nghiên cứu tương tác, tự chấm theo tiêu chí và in mẫu giấy tờ.</p><a class="btn" href="../#phuong-phap">Mở công cụ phương pháp</a></div>"""
add("phuong-phap/", "phuong-phap", "Quy trình 8 bước làm dự án nghiên cứu khoa học AI cho học sinh",
    "Các bước làm dự án KHKT về trí tuệ nhân tạo: đặt vấn đề, đọc tài liệu, giả thuyết, thiết kế thí nghiệm, dữ liệu, mô hình, đánh giá, trình bày; hồ sơ và tiêu chí chấm.",
    body, crumbs=[("Phương pháp", "phuong-phap/")], current="phuong-phap/")

# ---------- lịch thi ----------
def ml(m): return f"Tháng {m[0]}" if len(m) == 1 else f"Tháng {m[0]} đến tháng {m[-1]}"
body = f"""<h1>Lịch thi khoa học kỹ thuật trong một năm học</h1>
<p class="lead">Chu kỳ cuộc thi KHKT dành cho học sinh lặp lại mỗi năm: cấp trường, cấp tỉnh hoặc thành phố, cấp quốc gia và quốc tế. Thời gian dưới đây là thông lệ; ngày cụ thể do Bộ GD&amp;ĐT và Sở GD&amp;ĐT từng địa phương công bố.</p>
<ol class="steps">{''.join(f"<li><span><strong>{ml(s['m'])}: {e(s['t'])}.</strong> {e(s['s'])}</span></li>" for s in D['STAGES'])}</ol>
<h2>Lập kế hoạch ngược từ hạn nộp</h2><p>Một dự án AI vừa sức học sinh thường cần 8 đến 14 tuần. Hãy chia thời gian: đọc tài liệu và đặt câu hỏi khoảng 15%, kế hoạch 8%, thu thập dữ liệu 20%, xây mô hình 20%, đánh giá 15%, viết báo cáo 10%, poster và luyện phỏng vấn 12%.</p>
<div class="cta"><p style="margin:0;flex:1 1 300px">Nhập hạn nộp hồ sơ, công cụ chia sẵn các giai đoạn theo ngày.</p><a class="btn" href="../#lo-trinh">Lập kế hoạch ngược</a></div>"""
add("lich-thi/", "lich-thi", "Lịch thi KHKT học sinh trong năm: cấp trường, tỉnh, quốc gia, ISEF",
    "Chu kỳ cuộc thi khoa học kỹ thuật dành cho học sinh THCS, THPT trong một năm học, từ cấp trường đến Regeneron ISEF, và cách lập kế hoạch ngược từ hạn nộp.",
    body, crumbs=[("Lịch thi", "lich-thi/")], current="lich-thi/")

# ---------- hỏi đáp ----------
FAQ = [
 ("Cuộc thi khoa học kỹ thuật dành cho học sinh lớp mấy?", "Cuộc thi nghiên cứu khoa học, kỹ thuật cấp quốc gia do Bộ GD&ĐT tổ chức dành cho học sinh trung học cơ sở và trung học phổ thông. Ở nhiều địa phương, học sinh từ lớp 8 đến lớp 12 được tham gia. Điều kiện cụ thể như kết quả học tập do quy chế và văn bản hằng năm quy định."),
 ("Dự án về AI thường thi ở lĩnh vực nào?", "Phần lớn dự án AI thuộc lĩnh vực Rô bốt và máy thông minh (học máy, hệ thống nhận thức) hoặc lĩnh vực Phần mềm (thuật toán, an ninh mạng, giao diện người máy, học trực tuyến). Các lĩnh vực của cuộc thi trong nước tương ứng với 22 lĩnh vực của ISEF. Nếu AI chỉ là công cụ cho một câu hỏi y sinh hay môi trường, có thể chọn lĩnh vực đó."),
 ("Một dự án có bao nhiêu học sinh?", "Thường là dự án cá nhân hoặc dự án nhóm 2 học sinh, mỗi dự án có giáo viên hướng dẫn. Với dự án nhóm, sổ nghiên cứu cần thể hiện đóng góp riêng của từng thành viên."),
 ("Có được dùng ChatGPT hay AI tạo sinh khi làm dự án không?", "Thường được dùng có điều kiện cho một số việc như gợi ý ý tưởng, sửa ngữ pháp, gợi ý công cụ thống kê, viết mã ban đầu, và phải ghi lại mọi câu lệnh. Không được để AI viết báo cáo, poster, kết luận, thu thập dữ liệu hay tìm trích dẫn thay em. Xem trang Dùng AI đúng cách."),
 ("Làm một dự án AI mất bao lâu?", "Một dự án vừa sức học sinh thường mất 8 đến 14 tuần làm việc đều đặn, chưa kể thời gian hoàn thiện hồ sơ và luyện trình bày. Nên bắt đầu từ cuối năm học trước hoặc đầu năm học."),
 ("Chưa biết lập trình có làm dự án AI được không?", "Được. Em có thể bắt đầu bằng công cụ không cần lập trình như Teachable Machine để thử ý tưởng, sau đó chạy các notebook Google Colab mẫu, sửa dần từng phần. Dự án mức độ khó 1 trên trang là điểm khởi đầu phù hợp."),
 ("Có cần máy tính mạnh không?", "Không bắt buộc. Google Colab cho dùng miễn phí GPU trong giới hạn nhất định, đủ để huấn luyện các mô hình nhỏ trong dự án học sinh. Các dự án phần cứng cần thêm Raspberry Pi hoặc vi điều khiển giá rẻ."),
 ("Sổ nghiên cứu là gì và ghi thế nào?", "Sổ nghiên cứu ghi lại toàn bộ quá trình từ ý tưởng đến sản phẩm theo thứ tự thời gian: mục tiêu mỗi buổi, cách làm, số liệu thô, cả những lần thất bại, và các lần dùng AI. Ghi ngay trong ngày, không tẩy xóa, không chép lại cho đẹp."),
 ("Tính mới của dự án là gì?", "Là điều dự án của em làm được mà các nghiên cứu đã có chưa làm: dữ liệu mới ở bối cảnh Việt Nam, cách đánh giá mới, ứng dụng cho nhóm người dùng chưa được quan tâm, hay cải tiến đo được so với đối chứng. Em phải nói được tính mới đó trong một câu."),
 ("Có được nộp dự án mẫu trên trang này đi thi không?", "Không. Dự án mẫu chỉ để luyện tập. Dự án dự thi phải là kết quả nghiên cứu của chính em, chưa công bố ở cuộc thi nào; nếu kế thừa kết quả trước đó phải ghi rõ. Trang gợi ý hướng tạo tính mới để em phát triển đề tài của riêng mình."),
 ("ISEF là gì?", "Regeneron ISEF là cuộc thi khoa học kỹ thuật quốc tế lớn nhất thế giới dành cho học sinh trước đại học, tổ chức vào tháng 5 hằng năm tại Hoa Kỳ với 22 lĩnh vực. Học sinh không đăng ký trực tiếp mà được chọn qua các cuộc thi liên kết; toàn bộ hồ sơ và phỏng vấn bằng tiếng Anh."),
 ("Giám khảo hay hỏi gì nhất về dự án AI?", "Mô hình đối chứng là gì và em hơn nó bao nhiêu; dữ liệu chia thế nào, có rò rỉ không; kết quả có ổn định qua nhiều lần chạy không; mô hình sai ở những ca nào; giới hạn của nghiên cứu; và em đã dùng AI tạo sinh ở bước nào."),
]
body = f"""<h1>Hỏi đáp về cuộc thi KHKT và dự án AI cho học sinh</h1>
<p class="lead">Những câu hỏi học sinh, phụ huynh và giáo viên hay hỏi khi bắt đầu làm dự án nghiên cứu khoa học kỹ thuật về trí tuệ nhân tạo.</p>
<div class="faq">{''.join(f'<details{" open" if i < 2 else ""}><summary><h2 style="display:inline;font-size:18px;margin:0">{e(q)}</h2></summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(FAQ))}</div>"""
ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
add("hoi-dap/", "hoi-dap", "Hỏi đáp về cuộc thi KHKT và dự án AI cho học sinh",
    "Giải đáp: thi KHKT lớp mấy, dự án AI thi lĩnh vực nào, có được dùng ChatGPT, làm mất bao lâu, chưa biết lập trình có làm được không, sổ nghiên cứu, tính mới, ISEF.",
    body, ld=ld, crumbs=[("Hỏi đáp", "hoi-dap/")], current="hoi-dap/")

# ---------- 404 ----------
html404 = page("404.html", "Không tìm thấy trang | " + BRAND, "Trang bạn tìm không tồn tại.",
  '<h1>Không tìm thấy trang này</h1><p class="lead">Đường dẫn có thể đã thay đổi. Hãy bắt đầu lại từ một trong các mục dưới đây.</p><div class="cards">' +
  "".join(f'<a class="card" href="{U}/{p}"><strong>{t}</strong></a>' for p, t in NAV) + "</div>", og="trang-chu")
s404 = open(os.path.join(SITE, "404.html")).read()
s404 = s404.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
# 404 có thể nằm ở bất kỳ đường dẫn nào: đổi liên kết tương đối thành tuyệt đối
s404 = s404.replace('href="favicon.svg"', f'href="{U}/favicon.svg"').replace('href="assets/', f'href="{U}/assets/').replace('href="manifest', f'href="{U}/manifest')
for p, _ in NAV: s404 = s404.replace(f'href="{p}"', f'href="{U}/{p}"')
s404 = s404.replace('href="du-an/', f'href="{U}/du-an/').replace('<a class="brand" href="">', f'<a class="brand" href="{U}/">').replace('<a href="">Mở công cụ', f'<a href="{U}/">Mở công cụ')
open(os.path.join(SITE, "404.html"), "w").write(s404)

# ---------- sitemap, robots ----------
urls = [("", "1.0", "weekly")] + [(p, "0.9" if p == "du-an/" else ("0.8" if p.startswith("du-an/") else "0.7"), "monthly") for p in PAGES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{U}/{p}</loc><lastmod>{TODAY}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n" for p, pr, c in urls) + "</urlset>\n"
open(os.path.join(SITE, "sitemap.xml"), "w").write(sm)
open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {U}/sitemap.xml\n")
open(os.path.join(SITE, ".nojekyll"), "w").write("")
pass
print(len(PAGES), "trang tĩnh +", "404, sitemap, robots")
