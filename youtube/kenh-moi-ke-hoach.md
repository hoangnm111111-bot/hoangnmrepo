# Kênh YouTube mới — ngách, chủ đề và kịch bản video đầu tiên

Ngày làm: 2026-11-23. Thị trường: khán giả nói tiếng Anh ở Mỹ.
Công cụ: bộ skill `youtube-agent-skill` (`/yt-viral`, `/yt-package`, `/yt-script`, `/yt-plan`).

---

## 1. Cách nghiên cứu

- **Lượt 1:** quét 20 ngách phổ biến với khán giả Mỹ. Mỗi ngách lấy 9 kênh có video đăng trong năm
  2026 trên kết quả tìm kiếm YouTube, rồi lấy 15 video gần nhất của mỗi kênh. Tổng cộng 161 kênh,
  khoảng 2.400 video.
- **Lượt 2:** quét kỹ 7 ngách tiếng Anh nổi bật nhất ở lượt 1, thêm 61 kênh.
- **Chỉ số chính:** `/yt-viral` xếp hạng mỗi video theo **mức vượt trung vị lượt xem của chính kênh
  đó**, không theo lượt xem tuyệt đối. Em đo thêm hai chỉ số:
  - **views/sub:** trung vị lượt xem chia cho số người đăng ký. Chỉ số càng cao, thuật toán càng
    đẩy video ra ngoài tập người đăng ký.
  - **Kênh nhỏ thắng:** số kênh dưới 100 nghìn người đăng ký có trung vị từ 20 nghìn lượt xem trở lên.
- Dữ liệu thô và script nằm trong `youtube/research/`.

**Giới hạn của dữ liệu:**
- Mỗi ngách chỉ có khoảng 9 kênh, nên đây là mẫu nhỏ.
- Lượt xem và số người đăng ký là con số làm tròn của YouTube tại thời điểm quét.
- Bộ lọc "năm nay" của YouTube không lọc theo quốc gia. Ngách "câu chuyện kinh doanh" ở lượt 1 bị
  lẫn nhiều kênh tiếng Hindi, nên em đã loại khỏi kết luận.

## 2. Kết quả

| Ngách (lượt 2) | Trung vị người đăng ký | Trung vị lượt xem | views/sub | Kênh nhỏ ≥20 nghìn |
|---|---:|---:|---:|---:|
| **Không gian — "Every X Explained"** | 2.330 | 12.000 | **2,28** | 2/7 |
| **Bí ẩn — "Explained"** | 100.000 | 188.000 | 0,75 | **3/4** |
| Iceberg (giải thích theo tầng) | 138.000 | 82.000 | 0,77 | 3/3 |
| Khoa học ru ngủ | 81.650 | 27.000 | 0,21 | 3/5 |
| Lịch sử "Every empire" | 20.200 | 901 | 0,42 | 0/7 |

Bằng chứng rõ nhất là các **kênh rất nhỏ nhưng có video vượt xa quy mô kênh**:

| Kênh | Người đăng ký | Trung vị lượt xem | Video tốt nhất |
|---|---:|---:|---|
| Karakulya Explains | 2.330 | 12.000 | *Every Type Of Solar System Explained in 11 Minutes*: 256 nghìn |
| ReadBeforeDark | 2.320 | 22.750 | *Creepiest Filipino Urban Legends Explained in 12 Minutes*: 266 nghìn |
| Space Time Narratives | 17.100 | 39.000 | *A Light-Year Is So Big Your Brain Can't Process It*: 585 nghìn |
| Around The World Explained | 21.200 | 51.000 | *The Creepiest Urban Legends Explained Around the World*: 546 nghìn |
| Bluntly Explained | 49.900 | 101.000 | *Every Black Hole That Shouldn't Exist Explained in 14 Minutes*: 1,6 triệu (15,8 lần trung vị) |
| M Simplified | 100.000 | 297.000 | *Creepiest Deep Sea Monsters Explained in 8 Minutes*: 1,7 triệu |

**Điểm chung của các video này:** tiêu đề dạng **"Every [nhóm sự vật] Explained in [N] Minutes"**,
dài 8–14 phút (bản kịch bản này khoảng 7–8 phút; có thể thêm mục để kéo lên 10 phút), hình minh họa 2D hoặc ảnh tư liệu, có giọng đọc, không cần lộ mặt. Lưu ý: bộ phân
loại công thức chỉ đánh giá câu chữ trong tiêu đề. Nó không chứng minh tiêu đề là lý do video nổi.

## 3. Đề xuất ngách

**Ngách chính: video giải thích về không gian và vũ trụ theo dạng "Every X Explained", có pha yếu tố
bí ẩn.** Lý do:

1. Có chỉ số views/sub cao nhất trong toàn bộ dữ liệu. Kênh dưới 3 nghìn người đăng ký đã có video
   hơn 250 nghìn lượt xem, tức là thuật toán đang đẩy dạng video này cho kênh mới.
2. Nội dung không lỗi thời: một video về lỗ đen vẫn có người xem sau nhiều năm.
3. Không cần lộ mặt, không cần tiếng Anh bản xứ hoàn hảo nếu kịch bản tốt và giọng đọc rõ. Phù hợp
   với việc anh làm từ Việt Nam cho khán giả Mỹ.
4. Ngách bí ẩn cũng mạnh. Ghép "vũ trụ + bí ẩn" (ví dụ tín hiệu lạ, vật thể khó giải thích) là lấy
   được lực kéo của cả hai.

**Rủi ro cần tránh:**
- **Chính sách "nội dung thiếu chân thực / sản xuất hàng loạt"** của YouTube. Kênh chỉ ghép giọng AI
  với ảnh stock lặp đi lặp lại có thể bị từ chối kiếm tiền. Cách tránh: kịch bản tự nghiên cứu, có
  nguồn, hình ảnh có chủ đích cho từng đoạn, giọng đọc nhất quán.
- **Không dùng giọng giả người thật.** Trong ngách "khoa học ru ngủ" có kênh đặt tên video theo
  Brian Cox hoặc Neil deGrasse Tyson. Làm vậy vi phạm chính sách mạo danh và dễ bị đánh gậy.
- **Không bịa số liệu.** Mọi số trong kịch bản phải có nguồn. Gắn nguồn vào phần mô tả video.

## 4. Mười chủ đề (đã kiểm tra bằng `title.py`)

| # | Tiêu đề | Điểm | Ghi chú |
|---|---|---:|---|
| 1 | **Every Strange Signal From Space Explained in 7 Minutes** | 98 | ← **video đầu tiên**, kết hợp vũ trụ và bí ẩn |
| 2 | The 1977 Signal Nobody Has Heard Again | 100 | Short hoặc video tiếp nối chỉ về tín hiệu Wow! |
| 3 | Every Dead Star Explained in 12 Minutes | 100 | |
| 4 | Every Way the Universe Could End Explained | 76 | Nên thêm con số, ví dụ "…in 5 Ways" |
| 5 | Every Planet That Shouldn't Exist Explained | 76 | Đi theo mẫu của Bluntly nhưng đổi đối tượng |
| 6 | Every Object We've Sent Out of the Solar System | 76 | |
| 7 | Every Moon That Could Hold Life Explained | 76 | |
| 8 | Every Size of Star Explained | 90 | |
| 9 | Every Mission That Landed on Another World | 76 | |
| 10 | Every Strange Signal From Space Explained in 7 Minutes, phần 2 | — | Chỉ làm nếu video 1 đạt từ 2 lần trung vị kênh trở lên |

Gợi ý chung từ `title.py`: thêm **một con số** (số phút, năm, số lượng) vào tiêu đề. Đây là cách sửa
đơn giản và chắc ăn nhất.

## 5. Kế hoạch tuần (theo `/yt-plan`)

Anh có nhiều thời gian, nhưng skill khuyên **3 lần đăng mỗi tuần, không đăng hằng ngày**:

| Ngày | Dạng | Tiêu đề làm việc | Lời hứa với người xem |
|---|---|---|---|
| Thứ Ba | **Video chính** (khoảng 7–8 phút) | Every Strange Signal From Space Explained in 7 Minutes | Mọi tín hiệu lạ nổi tiếng, xếp từ đã giải được đến chưa giải được |
| Thứ Năm | Short | The 1977 Signal Nobody Has Heard Again | 72 giây và một chữ "Wow!" |
| Thứ Bảy | Short | It Was a Microwave Oven | Tín hiệu "ngoài hành tinh" hóa ra đến từ lò vi sóng |
| Chủ Nhật | Short | Something Pulses Every 44 Minutes | Vật thể chưa ai giải thích được |

Các Short đều cắt từ video chính bằng `/yt-shorts`. Thời gian thật sự dành cho kịch bản, giọng đọc,
hình ảnh và dựng nên ghi lại từ tuần 1 để tuần sau điều chỉnh. **Nếu tuần bị trễ, bỏ Short thứ ba
trước.** Ngày đăng là tạm đặt: sau khi có khoảng 10 video, chọn lại ngày theo phần Analytics của kênh.

---

## 6. Kịch bản video đầu tiên

**Tiêu đề:** Every Strange Signal From Space Explained in 7 Minutes
**Chữ trên thumbnail:** `STILL UNSOLVED` (`title.py`: 98/100; chữ trên ảnh không trùng tiêu đề)

**Brief thumbnail:**
- Nền vũ trụ tối.
- Ở giữa là một đường sóng radio màu xanh neon, vọt lên một đỉnh nhọn.
- Bên cạnh là mảnh giấy in liên tục có chữ "Wow!" khoanh đỏ, vẽ lại theo phong cách riêng, không
  dùng ảnh có bản quyền.
- Hai chữ `STILL UNSOLVED` màu trắng viền đen, ở góc trên trái.
- Tương phản cao để vẫn đọc được ở cỡ ảnh nhỏ trên bảng tin.

### Hai hook tốt nhất (`hookscore.py`)

**Hook A: 73, STRONG, công thức *The Question*** ← chọn
> "In 1977, a telescope you've never heard of caught a 72-second signal from space. Nobody has
> caught it again. Why?"

```
SPECIFICITY 90 | ADDRESS 76 | STAKES 62 | CURIOSITY 76 | BREVITY 100
```

**Hook B: 58, WORKABLE, công thức *The Question***
> "Every signal you're about to see was called aliens. One was a microwave oven. Which ones never
> died?"

```
SPECIFICITY 46 | ADDRESS 76 | STAKES 48 | CURIOSITY 59 | BREVITY 100
```

**Vì sao chọn A:** công thức *The Question* đặt ra một câu hỏi người xem không thể tự trả lời ngay
("tại sao không ai bắt lại được?"). Câu hỏi này kéo đúng đến phần trả lời ở cuối video, nên giữ
người xem đến hết. Hai con số cụ thể 1977 và 72 giây cho thấy câu chuyện có thật.

Ghi chú về điểm số: lượt hook đầu tiên chỉ được 28–44 điểm (WEAK), vì `hookscore.py` chấm theo từ
khóa và ưu tiên câu có "you", con số, từ chỉ rủi ro, độ dài 9–24 từ. Hook A đạt điểm cao sau khi sửa
theo đúng các tiêu chí đó. Tác giả skill cũng nói rõ: **điểm cao không đảm bảo video thắng.**

### Kịch bản (khoảng 1.060 từ, tức khoảng 7 phút ở tốc độ đọc 150 từ/phút; đọc chậm kiểu phim tài liệu khoảng 130 từ/phút thì ra khoảng 8 phút. **Sửa con số trong tiêu đề cho khớp thời lượng thật sau khi dựng.**)

> Mọi sự kiện và số liệu bên dưới là thông tin khoa học đã công bố, nhưng em viết từ kiến thức sẵn
> có. **Anh cần đối chiếu lại từng điểm với nguồn gốc (NASA, Nature, ADS, thông cáo của các trường)
> trước khi thu âm**, rồi dán nguồn vào phần mô tả.

---

**[0:00–0:08] HOOK**
[ON SCREEN: ảnh tư liệu kính thiên văn Big Ear (Ohio State) tiến lại gần; đường tín hiệu nhấp nháy rồi tắt]

In 1977, a telescope you've never heard of caught a 72-second signal from space. Nobody has caught it again. Why?

**[0:08–0:28] THE TURN**
[ON SCREEN: thang dọc 10 nấc, trên cùng ghi "SOLVED", dưới cùng ghi "STILL UNSOLVED"; con trỏ đặt ở nấc đầu]

To answer that, you need to see every strange signal astronomers have ever chased. Here they are, ranked from the ones we solved, to the ones we didn't. Some turned out to be stars. One turned out to be lunch. And the last few? Still open. Let's start at the top.

**[0:28–1:10] #1 — LGM-1 (1967) · SOLVED**
[ON SCREEN: bản ghi giấy có các nhịp đều đặn; nhãn "LGM-1 = Little Green Men"; minh họa sao neutron quay, chùm sáng quét qua như hải đăng]

In 1967, a graduate student named Jocelyn Bell Burnell noticed something on a chart recorder that shouldn't have been there: pulses, perfectly regular, about once every second and a third. Nothing natural was supposed to keep time like that. The team half-jokingly labeled it LGM-1 — "Little Green Men."
It wasn't aliens. It was a pulsar: a collapsed star, a city-sized ball of neutrons, spinning and sweeping a beam across Earth like a lighthouse. It was a discovery big enough to win a Nobel Prize — though famously, not for her.
Lesson one: "too regular to be natural" is how nature fools us first.

**[1:10–1:44] #2 — Perytons · SOLVED (and embarrassing)**
[ON SCREEN: đĩa radio Parkes ở Úc; các vạch tín hiệu "peryton"; cắt sang lò vi sóng trong phòng nghỉ, cửa bật mở giữa chừng]

For years, the Parkes radio telescope in Australia kept catching short bursts that astronomers called perytons. They looked a little like signals from deep space, but they kept showing up around midday.
In 2015, a team finally caught the culprit. It was a microwave oven in the observatory's own kitchen. Open the door before the timer finishes, and the oven leaks a burst at just the right frequency.
That's the bar every signal on this list has to clear: prove you're not the lunch.

**[1:44–2:11] #3 — SHGb02+14a (2003) · PROBABLY NOISE**
[ON SCREEN: màn hình bảo vệ SETI@home kiểu cũ; bản đồ trời giữa chòm Song Ngư và Bạch Dương]

In 2003, a home-computing project called SETI@home — millions of volunteers lending their PCs to search for aliens — flagged a candidate that appeared three times at the Arecibo telescope. Its name is a mouthful: SHGb02+14a.
Exciting? For a moment. But there was no star system at the spot, and the signal drifted in a way that pointed to noise or coincidence. Most researchers filed it under "probably nothing."

**[2:11–2:34] #4 — Ross 128 (2017) · SOLVED**
[ON SCREEN: sao lùn đỏ Ross 128; các vệt vệ tinh địa tĩnh bay ngang khung hình]

In 2017, Arecibo picked up odd signals while pointing at Ross 128, a quiet red dwarf only about eleven light-years away. The team even nicknamed it the "Weird!" signal.
The answer was closer than eleven light-years. The best explanation turned out to be geostationary satellites sitting in the same patch of sky. Our own technology, again.

**[2:34–3:08] #5 — BLC1 (2019) · SOLVED**
[ON SCREEN: Proxima Centauri; nhãn "982 MHz"; thanh tần số bị nhiễu tách ra từng mảnh]

This one made headlines. Breakthrough Listen, the biggest alien-hunting project ever funded, found a narrow signal while pointing Parkes at Proxima Centauri — the closest star to the Sun. Narrow signals are exactly what technology makes. They named it BLC1: Breakthrough Listen Candidate One.
Two years of checking later, the verdict: interference from equipment here on Earth. It's the strongest alien candidate we've ever had, and it was still us.
So far: a star, a kitchen, noise, satellites, and our own gear. Now the list gets harder.

**[3:08–3:50] #6 — The Lorimer Burst · PARTLY SOLVED**
[ON SCREEN: biểu đồ một chớp sáng cực ngắn; đồng hồ đếm mili giây; ảnh minh họa sao từ (magnetar)]

In 2007, Duncan Lorimer and his student went back through old Parkes data from 2001 and found a single flash of radio energy that lasted only milliseconds — and came from far outside our galaxy. It was the first fast radio burst, or FRB.
Since then, we've found many more. And in 2020, we finally caught one coming from inside the Milky Way, from a magnetar called SGR 1935+2154 — a dead star with a magnetic field so strong it's hard to picture.
So we know at least some FRBs come from magnetars. "Some" is doing a lot of work in that sentence.

**[3:50–4:16] #7 — FRB 121102 · OPEN**
[ON SCREEN: các vạch tín hiệu chớp lặp đi lặp lại; thu nhỏ dần về một thiên hà lùn xa xôi]

Most fast radio bursts flash once and vanish. FRB 121102, first found at Arecibo, didn't. It repeated — again and again. Astronomers traced it to a small dwarf galaxy billions of light-years away.
A one-time flash can be a catastrophe. A repeat means whatever made it survived. What can do that across billions of light-years, over and over? We still don't have a full answer.

**[4:16–4:39] #8 — FRB 20180916B · OPEN**
[ON SCREEN: lịch có các cụm ngày tô sáng, lặp theo chu kỳ khoảng 16 ngày]

Then it got stranger. A burst source found by the CHIME telescope in Canada doesn't just repeat — it keeps a schedule. Roughly four days of activity, then silence, on a cycle of about sixteen days.
An orbit? A wobbling star? A companion blocking the view? Each idea fits some of the data. None fits all of it.

**[4:39–5:06] #9 — GLEAM-X J162759 · OPEN**
[ON SCREEN: thời gian chạy; một nguồn sáng bật lên rồi tắt; nhãn "every ~18 min"]

Now come the ones that break the rules. In 2022, astronomers in Australia reported an object in our own galaxy that switched on about every eighteen minutes, glowed for up to a minute, and then went dark.
Here's the problem: we know objects that spin in seconds, and we know objects that cycle over hours. Something that takes eighteen minutes and stays this bright isn't supposed to exist.

**[5:06–5:30] #10 — ASKAP J1832-0911 · OPEN**
[ON SCREEN: hai bảng song song "RADIO" và "X-RAY" cùng nhấp nháy; đồng hồ đếm 44 phút]

And in 2025, astronomers announced one more: an object in our galaxy that pulses about every forty-four minutes. This one gives off X-rays as well as radio waves, which gives scientists a second way to study it. Even so, nobody can say what it is. A strange white dwarf? An unusual magnetar? Something we haven't named yet? It's still open.

**[5:30–6:55] THE PAYOFF — the Wow! signal**
[ON SCREEN: quay lại bản in giấy; vòng đỏ quanh "6EQUJ5"; chữ "Wow!" viết tay xuất hiện; cuối cùng là chòm Nhân Mã]

Which brings us back to the start, and to the answer I promised.
August 15th, 1977. The Big Ear telescope at Ohio State was sweeping the sky. A volunteer astronomer named Jerry Ehman was reading the printout days later when he saw a run of characters — 6EQUJ5 — climbing far above the noise. He circled it and wrote one word: "Wow!"
Why 72 seconds? Big Ear didn't move; it let Earth's rotation sweep the sky past it. Any fixed point in space crossed its view in about 72 seconds. So the signal lasted at least as long as the telescope could see it.
It was near the hydrogen frequency — the one frequency many scientists guessed aliens might use. People have pointed telescopes at that patch of sky in Sagittarius many times since. Nothing.
So why has nobody caught it again? Here's the honest answer: nobody knows. In 2024, a research team proposed a natural explanation — a cold hydrogen cloud that briefly brightened, possibly lit up by a burst from a magnetar. It's a serious idea. It hasn't been confirmed.
That's the pattern of this whole list. Every signal starts at "aliens." Most of them end at "us." A few are still sitting at the bottom of the ladder, waiting.

**[6:55–7:03] THE CLOSE — one ask**
[ON SCREEN: thang 10 nấc đầy đủ; ba nấc cuối vẫn nhấp nháy "UNSOLVED"]

If you want the next one, I'm doing every planet that shouldn't exist. Subscribe, and it'll be waiting for you.

---

## 7. Phần mô tả video (bản nháp theo `/yt-seo`)

```
Every strange signal from space, from the Wow! signal to fast radio bursts, ranked from solved to still unsolved.

Sources: [dán link NASA / Nature / các bài báo đã đối chiếu]

00:00 The 72-second signal
00:28 LGM-1
01:10 Perytons
01:44 SHGb02+14a
02:11 Ross 128
02:34 BLC1
03:08 The Lorimer Burst
03:50 FRB 121102
04:16 FRB 20180916B
04:39 GLEAM-X J162759
05:06 ASKAP J1832-0911
05:30 The Wow! signal
```

Ba truy vấn video này cần thắng trên YouTube: "wow signal explained", "strange signals from space",
"fast radio bursts explained". Tiêu đề và hai dòng đầu mô tả đều đã chứa các từ này.

## 8. Việc còn thiếu

- **Voice profile:** kênh mới chưa có video nào, nên chưa có file `voice.md`. Anh chọn giọng (giọng
  mình hay AI voice có bản quyền), tốc độ, mức nghiêm túc hay hài hước, rồi điền
  `.claude/youtube/voice.template.md`. Từ video thứ hai, mọi skill sẽ viết theo giọng đó.
- **Đối chiếu nguồn** cho toàn bộ sự kiện trong kịch bản.
- Sau khi đăng 2–3 video, chạy `/yt-retention` trên file retention xuất từ YouTube Studio để biết
  người xem bỏ đi ở đâu.

---

**Ship it, or change it?**
