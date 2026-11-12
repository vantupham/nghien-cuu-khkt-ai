# Sổ Nghiên Cứu AI

**Trang web:** https://vantupham.github.io/nghien-cuu-khkt-ai/

Website mở giúp học sinh trung học (lớp 8–12) luyện làm nghiên cứu khoa học kỹ thuật về trí tuệ nhân tạo, chuẩn bị cho cuộc thi KHKT cấp trường, cấp tỉnh/thành phố, cấp quốc gia và quốc tế (Regeneron ISEF). Dùng được cho học sinh toàn quốc và qua nhiều năm học.

## Có gì trong trang

- **Kỹ năng nghiên cứu**: bánh xe 10 kỹ năng của nhà khoa học để tự đánh giá, bài luyện cho từng kỹ năng, 8 tình huống thử thách tư duy khoa học.
- **Luyện viết báo cáo**: bố cục theo số trang, xưởng viết từng phần có kiểm tra tự động, chọn câu viết tốt hơn, tóm tắt 250 từ, tạo trích dẫn APA.
- **Vòng tròn nghiên cứu**: 8 bước tương tác ở trang chủ.
- **Công cụ kiểm tra kết quả**: ma trận nhầm lẫn và khoảng tin cậy, kéo ngưỡng phân loại, so sánh nhiều lần chạy bằng kiểm định t Welch.
- **Giám khảo AI**: tạo câu lệnh để chatbot đóng vai giám khảo hỏi vặn, tự ghi vào nhật ký prompt.
- **Tìm tài liệu**: chuyển từ khóa tiếng Việt sang tiếng Anh, mở sẵn Google Scholar, arXiv, Semantic Scholar, kho dữ liệu.
- **Tiếng Anh cho ISEF**: 40 thuật ngữ và mẫu câu cho tóm tắt, phỏng vấn.
- **Mẫu giấy tờ in được**: kế hoạch nghiên cứu, giấy đồng ý tham gia, trang sổ nghiên cứu, phiếu góp ý.
- **Hồ sơ của em**: hành trình 12 huy hiệu, thống kê tiến độ, sao lưu và khôi phục bằng file hoặc mã.
- **Notebook Colab cho 10 dự án**: nút *Mở trên Colab* trên trang từng dự án.
- **10 dự án mẫu** (lĩnh vực Rô bốt và máy thông minh, Phần mềm): câu hỏi nghiên cứu, giả thuyết, dữ liệu, phương pháp, chỉ số đo, đạo đức, hướng tạo tính mới, lộ trình theo tuần có đánh dấu tiến độ.
- **Đèn giao thông AI**: tra nhanh việc nhờ AI được phép, được phép có điều kiện hay bị cấm theo các nguyên tắc dùng AI phổ biến trong cuộc thi KHKT học sinh.
- **Nhật ký prompt**: ghi lại từng lần dùng AI, sao chép thành bảng hoặc tải file CSV.
- **Xưởng đề tài**: ghép vấn đề, dữ liệu, kỹ thuật thành khung câu hỏi nghiên cứu.
- **Giám khảo thử**: tự chấm theo khung 100 điểm, biểu đồ radar, câu hỏi phỏng vấn, bấm giờ 3 phút.
- **Lịch thi và kế hoạch ngược**: chu kỳ thi trong một năm học (tự nhận biết giai đoạn hiện tại theo tháng), tự chia giai đoạn theo hạn nộp.
- **Phòng thí nghiệm mini**: thuật toán k láng giềng gần nhất chạy trên trình duyệt.

Trang web là một file `index.html`, không cần máy chủ. Thư mục `notebooks/` chứa 10 notebook Colab, mỗi dự án một notebook. Dữ liệu học sinh nhập chỉ lưu trong trình duyệt (localStorage).

## Cấu trúc thư mục

```
index.html                 công cụ tương tác (trang chủ)
du-an/, ky-nang/, viet-bao-cao/, dung-ai-dung-cach/,
phuong-phap/, lich-thi/, hoi-dap/   trang tĩnh cho SEO
notebooks/                 10 notebook Colab
assets/                    ảnh chia sẻ, biểu tượng
.github/workflows/pages.yml  tự đưa trang lên GitHub Pages
sitemap.xml, robots.txt, 404.html, favicon.svg, manifest.webmanifest, .nojekyll
tools/dien_dia_chi.py      dùng khi không chạy GitHub Actions
```

## Đưa lên GitHub Pages (khuyên dùng: GitHub Actions)

1. Tạo repository mới, ví dụ `so-nghien-cuu-ai`, chọn **Public**.
2. Tải lên **toàn bộ** nội dung thư mục, kể cả thư mục ẩn `.github/` và file `.nojekyll`. Trên máy Mac, nhấn `Cmd + Shift + .` để hiện thư mục ẩn trước khi kéo thả. Nếu không tải được `.github/`, vào **Add file → Create new file**, gõ tên `.github/workflows/pages.yml` rồi dán nội dung file đó.
3. Vào **Settings → Pages**, mục **Source** chọn **GitHub Actions**.
4. Mở tab **Actions**, đợi quy trình "Dua trang len GitHub Pages" chạy xong (khoảng 1 phút). Trang có địa chỉ `https://<tài-khoản>.github.io/so-nghien-cuu-ai/`.

Bản này đã được điền sẵn địa chỉ `https://vantupham.github.io/nghien-cuu-khkt-ai` và repo `vantupham/nghien-cuu-khkt-ai`. Nếu sau này tạo lại trang tĩnh bằng thư mục `tools/`, các cụm `__SITE_URL__` và `__REPO__` sẽ xuất hiện lại và quy trình GitHub Actions tự điền chúng khi đưa lên.

**Nếu không dùng GitHub Actions** (chọn Deploy from a branch): chạy trên máy  
`python tools/dien_dia_chi.py https://<tài-khoản>.github.io/so-nghien-cuu-ai <tài-khoản>/so-nghien-cuu-ai`  
rồi tải các file đã đổi lên.

## SEO và lan tỏa

Đã có sẵn:
- **18 trang có địa chỉ riêng** để Google lập chỉ mục: trang chủ, danh sách và 10 trang đề tài, kỹ năng, viết báo cáo, dùng AI đúng cách, phương pháp, lịch thi, hỏi đáp. Mỗi trang có tiêu đề, mô tả, đường dẫn chuẩn (canonical) riêng.
- **Thẻ chia sẻ** Open Graph và Twitter, ảnh xem trước 1200 × 630 riêng cho từng trang (thư mục `assets/og/`), hiển thị đẹp khi dán link vào Facebook, Zalo, Messenger.
- **Dữ liệu có cấu trúc** (JSON-LD): WebSite, ItemList, LearningResource cho từng đề tài, FAQPage, BreadcrumbList.
- `sitemap.xml`, `robots.txt`, `404.html`, favicon, biểu tượng điện thoại, `manifest.webmanifest`.
- Liên kết nội bộ ở chân trang, nội dung đọc được cả khi tắt JavaScript.

Việc bạn cần làm sau khi trang lên mạng:
1. **Google Search Console** (search.google.com/search-console): thêm trang theo kiểu *URL prefix* với địa chỉ GitHub Pages; xác minh bằng thẻ HTML (dán thẻ `<meta name="google-site-verification" ...>` vào `<head>` của `index.html`). Sau đó vào **Sơ đồ trang web**, gửi `sitemap.xml`.
2. **Bing Webmaster Tools**: nhập luôn từ Search Console để Bing (và các trợ lý AI dùng Bing) biết trang.
3. **Kiểm tra thẻ chia sẻ**: dán link vào công cụ Sharing Debugger của Facebook để xóa bộ nhớ đệm khi ảnh xem trước chưa đúng.
4. **Kiểm tra dữ liệu có cấu trúc**: dùng Rich Results Test của Google với vài trang đề tài.
5. **Lan tỏa**: chia sẻ link từng trang đề tài (không chỉ trang chủ) vào nhóm giáo viên, câu lạc bộ KHKT, trang của trường; mỗi link có ảnh xem trước riêng. Liên kết từ website trường hoặc Sở về trang là tín hiệu rất tốt cho Google.

Khi sửa dữ liệu dự án trong `index.html`, cần tạo lại các trang tĩnh để nội dung khớp nhau (nhờ người quản trị chạy lại công cụ tạo trang, hoặc sửa trực tiếp file trong `du-an/<tên>/index.html`).

## Notebook Colab

Khi trang chạy trên `https://<tài-khoản>.github.io/<repo>/`, nút *Mở trên Colab* tự trỏ tới `notebooks/` trong repo đó, nhánh `main`. Nếu dùng tên miền riêng hoặc nhánh khác, sửa hai dòng `GITHUB_REPO` và `GITHUB_BRANCH` ở đầu phần cấu hình trong `index.html`.

| Notebook | Dữ liệu luyện tập | Nội dung chính |
|---|---|---|
| 01 Bệnh lá | beans (Hugging Face) | Đối chứng logistic trên màu, học chuyển giao MobileNetV3, ma trận nhầm lẫn, thử ảnh thực địa, xuất ONNX |
| 02 Ngập | Mưa Open-Meteo; triều, nhãn giả lập | Dự báo trước 3 giờ, chia theo thời gian, recall ở mức báo giả 5%, tầm quan trọng đặc trưng |
| 03 Lừa đảo | SMS Spam Collection (UCI) | TF-IDF từ và ký tự, bộ biến đổi đối kháng, khung tiếng Việt, tinh chỉnh PhoBERT |
| 04 Ký hiệu | Video của em; giả lập | MediaPipe Hands, MLP một khung so với LSTM, kiểm tra trên người chưa gặp |
| 05 Ngủ gật | Video của em; mô phỏng | Tỉ lệ khung mắt, ngưỡng cố định, cá nhân hóa, kết hợp ngáp, báo động giả mỗi giờ |
| 06 Rác | TrashNet (Hugging Face) | Như 01, thêm mã Raspberry Pi điều khiển servo |
| 07 PM2.5 | Open-Meteo | Lặp lại, trung bình 24 giờ, Ridge, LSTM, đúng mức cảnh báo |
| 08 Tư thế | Ảnh của em; giả lập | MediaPipe Pose, chọn ngưỡng theo kappa, kiểm định hai nhóm |
| 09 Ôn tập RAG | 12 đoạn Sinh học mẫu | TF-IDF và vector đa ngôn ngữ, ngưỡng từ chối, phiếu chấm mù |
| 10 Thích ứng | Mô phỏng | BKT tự cài đặt, DKT, AUC theo lượng dữ liệu |

Mỗi notebook có đường dự phòng: nếu không tải được dữ liệu công khai, notebook dùng dữ liệu giả lập để quy trình vẫn chạy, và in rõ chữ **GIẢ LẬP**. Kết quả trên dữ liệu giả lập không được dùng trong báo cáo dự thi.

## Sửa nội dung

Mọi nội dung nằm trong phần `<script>` của `index.html`:

| Muốn sửa | Tìm biến |
|---|---|
| Dự án mẫu | `PROJECTS` |
| Quy định dùng AI | `AI_RULES` |
| Vấn đề, dữ liệu, kỹ thuật của Xưởng đề tài | `PROBLEMS`, `DATAS`, `TECHS` |
| Tiêu chí tự chấm | `CRITS` |
| Câu hỏi phỏng vấn | `QUESTIONS` |
| Lịch thi | `STAGES` |
| Huy hiệu | `BADGES` |
| Thuật ngữ, mẫu câu tiếng Anh | `GLOSS`, `FRAMES` |
| Từ khóa tìm tài liệu | `KW` |
| Mẫu giấy tờ | `TPLS` |
| Kỹ năng, thử thách | `SKILLS`, `THINK` |
| Báo cáo, câu mẫu | `SECTIONS`, `PAIRS` |
| Hồ sơ dự thi | `DOSSIER` |

Thêm dự án: sao chép một khối `{ id:..., ... }` trong `PROJECTS`, đổi `id` (chữ thường, không dấu, nối bằng gạch ngang) và nội dung.

## Lưu ý

Nội dung về cuộc thi là thông lệ chung, không gắn với địa phương hay năm học cụ thể. Luôn đối chiếu với văn bản gốc mới nhất. Dự án mẫu chỉ dùng để luyện tập; dự án dự thi phải là kết quả nghiên cứu của chính học sinh.

## Giấy phép

Nội dung: CC BY 4.0. Mã nguồn: MIT.
