"""Keep Vietnamese two-syllable compounds on one line.

PowerPoint wraps at any space, so short labels and quotes kept splitting words such as
"mục / tiêu" or "dân / tộc". bind_compounds() joins the syllables of the compounds below with a
no-break space (U+00A0); deck_lib.text() applies it to every run of 24 pt or less.
"""
import re

COMPOUNDS = """
trả lời|công thức|dân chủ|khác nhau|tài khoản|đảng phái|đề cương|hình thức|lý luận|ngân hàng|quan điểm|hòa khí
|mục tiêu|mục đích|khác biệt|nhân dân|dân tộc|tôn giáo|giai cấp|tầng lớp|thống nhất|toàn tập|việt nam|mặt trận|đoàn kết
|chính đáng|lập trường|nhất trí|lợi ích|chiến lược|cách mạng|tư tưởng|giáo trình|hiệp thương|công nhân|nông dân|trí thức
|truyền thống|khoan dung|độ lượng|niềm tin|tương đồng|quy tụ|sức mạnh|xây dựng|triển khai|tầm nhìn|cả nước|nhà tạm|dột nát
|trung thực|lâu dài|quá khứ|nghề nghiệp|tuổi tác|cá tính|ví dụ|thông tin|thế hệ|tín ngưỡng|quê quán|vùng miền|sở thích
|làm việc|phản biện|trích dẫn|kiểm chứng|đối chiếu|bài giảng|đại học|thương mại|phạm vi|công cộng|tư liệu|chính thống
|hồ chí|chí minh|tô lâm|bí thư|quốc hội|đại hội|xã hội|người dùng|cộng đồng|quốc gia|học liệu|cao tuổi|neo đơn|trẻ em
|môi trường|khó khăn|điều kiện|nguyên tắc|phương thức|lực lượng|vai trò|chủ thể|nền tảng|liên minh|lãnh đạo|nghị quyết
|văn kiện|số liệu|chính trị|quốc tế|độc lập|tổ quốc|nhân nghĩa|yêu nước|bàn bạc|giải pháp|tình thế|nhất thời|thành công
|nhiệm vụ|hàng đầu|ý nghĩa|quyết định|toàn dân|giống nhau|đồng nhất|tranh luận|văn hóa|lắng nghe|phản hồi|giơ tay
|ngón tay|bàn tay|thẻ màu|tình huống|liêm chính|học thuật|trách nhiệm|nội dung|cuối cùng|thuyết trình|sinh viên
|thành viên|ma trận|bố cục|hiển thị|giấy phép|rõ ràng|sơ đồ|lập trình|kịch bản|dàn ý|tìm kiếm|chỉnh sửa|nhật ký|cam kết
|công cụ|bản in|câu hỏi|đáp án|biểu quyết|điểm chung|quy mô|phức tạp|thế giới|tạp chí|cứu trợ|ủng hộ|đồng bào
"""

_PAIRS = [
    re.compile(r"(?<!\w)(" + re.escape(a) + r") (" + re.escape(b) + r")(?!\w)", re.IGNORECASE)
    for a, b in (c.strip().split(" ", 1) for c in COMPOUNDS.replace("\n", "").split("|") if c.strip())
]


def bind_compounds(t):
    """Join the syllables of known compounds with a no-break space."""
    for rx in _PAIRS:
        t = rx.sub("\\1\u00a0\\2", t)
    return t


if __name__ == "__main__":
    s = bind_compounds("Hồ Chí Minh: đoàn kết thực sự là mục đích phải nhất trí. ĐOÀN KẾT DÂN TỘC")
    print(s.replace("\u00a0", "~"))
