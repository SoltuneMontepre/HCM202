# Slide image recipes. src files live in 12_assets/downloaded (see 12_assets/DOWNLOAD_LIST.md for licences).
# box = slide box in inches (w, h); focus = point kept in frame; precrop = (l, t, r, b) fractions removed first.

MANIFEST = {
    "hero": dict(src="h1a_hcm_portrait_c1946.jpg", box=(6.28, 7.5), focus=(0.5, 0.36), treat="duotone",
                 dark="#24060A", mid="#7E3A2A", light="#F2DDBB", contrast=1.08,
                 alpha_fade=("left", 0.0, 0.42), vignette=0.3,
                 caption="Chủ tịch Hồ Chí Minh, khoảng 1946 · ảnh tư liệu, phạm vi công cộng (Wikimedia Commons)"),
    "s4": dict(src="h2b_ba_dinh_1945-09-02.jpg", box=(5.45, 7.5), focus=(0.48, 0.55), treat="sepia",
               caption="Lễ đài Quảng trường Ba Đình, Hà Nội, 2/9/1945 · ảnh tư liệu, phạm vi công cộng (Wikimedia Commons)"),
    "s12": dict(src="h1b_hcm_portrait_trang_su_moi_1945.jpg", precrop=(0.285, 0.205, 0.335, 0.37), box=(4.58, 7.5),
                focus=(0.5, 0.42), treat="duotone", dark="#1E0305", mid="#6E2A22", light="#EBD3AE", contrast=1.05,
                caption="Chân dung Hồ Chí Minh in trong sách “Trang sử mới” (1945) · Gallica/BnF, phạm vi công cộng"),
    "s15": dict(src="h2a_ba_dinh_le_dai_1945-09-02.jpg", precrop=(0.0, 0.0, 0.03, 0.27), box=(13.33, 7.5),
                focus=(0.5, 0.5), treat="duotone", dark="#2A0405", mid="#7A1A16", light="#E9C9A0", contrast=1.15,
                caption="Lễ đài Ba Đình, 2/9/1945 · Trung tâm Lưu trữ quốc gia III — luutru.gov.vn (phạm vi công cộng)"),
    "s3bg": dict(src="h2d_quoc_hoi_khoa_I_1946-03-02.jpg", precrop=(0.0, 0.0, 0.0, 0.06), box=(4.55, 7.5),
                 focus=(0.5, 0.62), treat="duotone", dark="#140102", mid="#3A0607", light="#6E2E24", contrast=1.15, vignette=0.5,
                 caption="Đại biểu Quốc hội khóa I, 2/3/1946 · ảnh tư liệu, phạm vi công cộng (quochoi.vn qua Wikimedia Commons)"),
    "s5strip": dict(src="h2c_cong_giao_ngay_doc_lap_1945.jpg", box=(7.0, 1.2), focus=(0.42, 0.18), treat="sepia",
                    caption="2/9/1945: khối Trường Thần học Công giáo trong đoàn mít tinh Ngày Độc lập · album Philippe Devillers, nay tại Bảo tàng Lịch sử Quốc gia (phạm vi công cộng)"),
    # slide 8 — four groups
    "s8_1": dict(src="c2e_child_gift_village.jpg", box=(2.92, 2.6), focus=(0.5, 0.42), treat="warm", caption=""),
    "s8_2": dict(src="c2a_tree_planting_phanthiet.jpg", box=(2.92, 2.6), focus=(0.55, 0.55), treat="warm", caption=""),
    "s8_3": dict(src="c2c_volunteer_elderly_binhphuoc.jpg", box=(2.92, 2.6), focus=(0.55, 0.68), treat="warm", caption=""),
    "s8_4": dict(src="c2f_book_bus.jpg", box=(2.92, 2.6), focus=(0.5, 0.45), treat="warm", caption=""),
    # slide 9 — scale-up strip (heights grow with scale)
    "s9_1": dict(src="c3a_classroom_hanoi.jpg", box=(2.2, 1.7), focus=(0.62, 0.5), treat="warm", caption=""),
    "s9_2": dict(src="c3c_usth_students.jpg", box=(2.65, 1.95), focus=(0.5, 0.55), treat="warm", caption=""),
    "s9_3": dict(src="c2d_children_volunteers_binhphuoc.jpg", box=(3.1, 2.2), focus=(0.55, 0.45), treat="warm", caption=""),
    "s9_4": dict(src="c3f_flags_dusk_hcmc.jpg", box=(3.55, 2.45), focus=(0.6, 0.55), treat="warm", amount=0.1, brightness=1.28, caption=""),
}

# "ĐẠI" photo mosaic (slide 5): 4 columns x 3 rows, read left→right, top→bottom
MOSAIC = [  # order: Đ (2x2), Ạ (2x2), dot of Ạ, I (3 rows)
    ("c1m_hmong_woman_laocai.jpg", (0.55, 0.35)),
    ("c1a_farmer_hoian.jpg", (0.45, 0.4)),
    ("c1q_elderly_vendor_hanoi.jpg", (0.62, 0.42)),
    ("c1e_workshop_hcmc.jpg", (0.5, 0.5)),
    ("c1g_teacher_chalkboard.jpg", (0.74, 0.35)),
    ("c1j_graduates_hanoi_law.jpg", (0.56, 0.2)),
    ("c1i_health_worker_2021.jpg", (0.5, 0.35)),
    ("c1z_fisherman_namdinh.jpg", (0.55, 0.4)),
    ("c1s_devotee_danang.jpg", (0.5, 0.6), (0.36, 0.1, 0.64, 0.75)),  # dot: bowing figure + altar
    ("c1n_gong_kontum.jpg", (0.45, 0.5)),
    ("c1u_easter_procession_thaibinh.jpg", (0.5, 0.5), (0.5, 0.66, 1.0, 1.0)),  # robed participants, not the cross
    ("c1d_construction_cantho.jpg", (0.5, 0.4)),
]
MOSAIC_CAPTION = "Ghép từ 12 ảnh chụp tại Việt Nam (Unsplash, Pexels) · nguồn từng ảnh ở phụ lục"
