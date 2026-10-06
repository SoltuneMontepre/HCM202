/* Unity Lab — 3 tình huống vận dụng (CONTEMPORARY APPLICATION).
   Không có backend: mọi lựa chọn chỉ nằm trong trình duyệt của người chơi.
   Nội dung lý luận ở mục "principle" phải khớp với 05_theory-verification.md. */

(function () {
  "use strict";

  // ------------------------------------------------------------------ CONFIG
  var CONFIG = {
    groupLine: "Dự án học tập · Môn Tư tưởng Hồ Chí Minh · Đại học FPT",
    presentSeconds: 120
  };

  // Phong cách xử lý khác biệt (diễn giải của nhóm, không phải phân loại của giáo trình)
  var STYLES = {
    connect: { name: "Người kết nối", color: "VÀNG", cls: "style-connect",
      text: "Bạn thường tìm điểm chung trước khi chọn phe. Bạn không xóa khác biệt, mà tìm cách để khác biệt cùng hướng về một mục tiêu chung.",
      watch: "Lưu ý: kết nối cần thời gian và kỹ năng điều phối — đôi khi vẫn phải ra quyết định khi chưa ai hoàn toàn hài lòng." },
    decide: { name: "Người quyết đoán", color: "ĐỎ", cls: "style-decide",
      text: "Bạn ưu tiên sự rõ ràng, tốc độ và bảo vệ tập thể bằng những quyết định dứt khoát.",
      watch: "Lưu ý: biểu quyết là cách ra quyết định hợp lệ; nhưng nếu bỏ qua bước bàn bạc, thắng một cuộc biểu quyết — hay một cuộc tranh luận — chưa chắc đã có được sự đồng thuận thật." },
    avoid: { name: "Người giữ hòa khí", color: "KEM", cls: "style-avoid",
      text: "Bạn quý sự êm ấm và tránh làm ai tổn thương.",
      watch: "Lưu ý: tránh va chạm có thể giữ hòa khí trên bề mặt, nhưng mâu thuẫn chưa được nói ra vẫn còn đó." },
    mixed: { name: "Người linh hoạt", color: "NHIỀU MÀU", cls: "style-mixed",
      text: "Mỗi tình huống bạn chọn một cách khác nhau — bạn đọc bối cảnh trước khi hành động.",
      watch: "Câu hỏi để nghĩ tiếp: điều gì khiến bạn đổi cách xử lý giữa các tình huống?" }
  };

  var WARMUP = {
    q: "Đoàn kết là gì?",
    options: [
      { k: "A", t: "Mọi người cùng một quan điểm, một cách nghĩ" },
      { k: "B", t: "Có khác biệt nhưng cùng hướng tới mục tiêu chung" },
      { k: "C", t: "Ý kiến thiểu số phải theo đa số" },
      { k: "D", t: "Tránh tranh luận để giữ hòa khí trong tập thể" }
    ]
  };

  // Mỗi phương án: style (connect/decide/avoid), priority, risk, principle {title, body, src}
  var CASES = [
    {
      tag: "Lớp học", icon: "class",
      title: "Bài thuyết trình nhóm",
      situation: "Nhóm 5 người, còn 3 ngày đến hạn. Hai bạn muốn làm video, hai bạn muốn làm slide truyền thống cho chắc. Bạn thứ năm — Minh — gần như chưa lên tiếng trong group chat. Bạn là nhóm trưởng.",
      question: "Bạn xử lý thế nào?",
      choices: [
        { style: "decide",
          t: "Bỏ phiếu ngay. Nếu hòa 2–2 thì nhóm trưởng quyết. Nhanh và rõ ràng.",
          priority: "Tốc độ và một quy tắc ai cũng hiểu.",
          risk: "Biểu quyết theo đa số là cách ra quyết định hợp lệ. Rủi ro ở đây là bỏ phiếu ngay, trước khi bàn bạc và trước khi mọi người — kể cả Minh — được nói ý kiến: phe “thua” có thể thấy mình bị gạt đi, mọi người làm việc nửa vời.",
          principle: "P_HIEPTHUONG" },
        { style: "connect",
          t: "Nhắn riêng hỏi ý Minh trước, rồi họp 15 phút: cả nhóm chốt mục tiêu chung (bài chắc kiến thức + lớp nhớ được), sau đó ghép phương án — slide làm xương sống, một đoạn video 60 giây để mở đầu.",
          priority: "Mục tiêu chung và tiếng nói của từng thành viên, kể cả người ít nói.",
          risk: "Tốn thêm thời gian, cần người điều phối tốt; không phải lúc nào cũng ghép được mọi ý kiến.",
          principle: "P_DIEMCHUNG" },
        { style: "avoid",
          t: "Tự chọn phương án an toàn (slide) mà không bàn với ai, để khỏi tranh cãi, rồi chia việc luôn.",
          priority: "Tránh xung đột, đi nhanh vào việc.",
          risk: "Tránh tranh cãi bằng cách tự quyết thay cả nhóm cũng là một dạng áp đặt: hai bạn muốn làm video thấy ý kiến bị bỏ qua, hòa khí chỉ ở bề mặt, nhóm trưởng một mình gánh trách nhiệm và nhóm mất một ý tưởng sáng tạo.",
          principle: "P_HIEPTHUONG" }
      ]
    },
    {
      tag: "Câu lạc bộ", icon: "club",
      title: "Người từng làm hỏng việc",
      situation: "CLB tình nguyện chuẩn bị chiến dịch hè. Năm ngoái, Lan bỏ dở một nhiệm vụ khiến cả đội vất vả. Năm nay Lan xin tham gia lại và nói mình đã thay đổi. Một số thành viên phản đối.",
      question: "CLB nên làm gì?",
      choices: [
        { style: "avoid",
          t: "Nhận Lan lại nhưng không nhắc gì đến chuyện cũ cho vui vẻ.",
          priority: "Không khí êm ấm, tránh làm ai khó xử.",
          risk: "Vấn đề cũ không được giải quyết; những người phản đối có thể bất mãn ngầm. Mâu thuẫn không biến mất chỉ vì không ai nói ra.",
          principle: "P_THATSU" },
        { style: "decide",
          t: "Từ chối. Rủi ro lặp lại là có thật, tập thể cần an toàn.",
          priority: "Sự ổn định và giảm rủi ro cho chiến dịch.",
          risk: "Đóng cửa với một người đang muốn thay đổi; tập thể thu hẹp lại và tạo tiền lệ “sai một lần là mãi mãi”.",
          principle: "P_KHOANDUNG" },
        { style: "connect",
          t: "Nhận Lan lại sau một buổi nói chuyện thẳng thắn: nhìn lại chuyện cũ, thống nhất cam kết rõ ràng, giao một nhiệm vụ vừa sức và có người đồng hành.",
          priority: "Cho con người cơ hội thay đổi, đồng thời giữ trách nhiệm rõ ràng.",
          risk: "Cần thời gian theo sát; nếu buông lỏng, rủi ro cũ vẫn có thể lặp lại.",
          principle: "P_KHOANDUNG" }
      ]
    },
    {
      tag: "Mạng xã hội", icon: "chat",
      title: "Group chat nóng lên",
      situation: "Trong group chat của khóa, có người chia sẻ một bài đăng chế giễu giọng nói và thói quen của sinh viên đến từ một vùng miền. Bình luận bắt đầu chia phe, vài bạn đã dùng lời lẽ xúc phạm nhau.",
      question: "Bạn phản ứng thế nào?",
      choices: [
        { style: "connect",
          t: "Viết một bình luận bình tĩnh: nhắc rằng tất cả là bạn cùng khóa, đề nghị dừng lời lẽ xúc phạm; nhắn riêng hỏi thăm bạn bị chế giễu; báo quản trị nhóm nếu vẫn tiếp diễn.",
          priority: "Tôn trọng khác biệt vùng miền và bảo vệ điểm chung — cộng đồng của khóa.",
          risk: "Có thể bị phản bác hoặc kéo vào tranh cãi; cần giữ bình tĩnh và lời lẽ đúng mực. Một bình luận không giải quyết được mọi chuyện.",
          principle: "P_TOANDAN" },
        { style: "avoid",
          t: "Tắt thông báo hoặc rời nhóm — không muốn dính vào.",
          priority: "Bảo vệ bản thân, tránh căng thẳng.",
          risk: "Im lặng có thể khiến lời lẽ xúc phạm trở thành “bình thường”; người bị chế giễu cảm thấy bị bỏ rơi.",
          principle: "P_TOANDAN" },
        { style: "decide",
          t: "Đăng một bài phản bác thật gắt để bảo vệ vùng miền của mình.",
          priority: "Bảo vệ danh dự của nhóm mình.",
          risk: "Tranh cãi leo thang, chia phe sâu hơn: có thể “thắng” cuộc tranh luận nhưng mất đi sự đoàn kết.",
          principle: "P_THATSU" }
      ]
    }
  ];

  // Nguyên tắc lý luận — chỉ dùng nội dung đã kiểm chứng (xem 05_theory-verification.md)
  var PRINCIPLES = {
    P_HIEPTHUONG: { title: "Hiệp thương dân chủ",
      body: "Theo bài giảng Chương 5, Mặt trận dân tộc thống nhất hoạt động theo nguyên tắc hiệp thương dân chủ: mọi vấn đề đều được đưa ra để các thành viên cùng bàn bạc công khai, đi đến nhất trí, loại trừ mọi áp đặt hoặc dân chủ hình thức. Tinh thần này gần với điều Hồ Chí Minh viết về cách lãnh đạo trong Sửa đổi lối làm việc: đem các ý kiến khác nhau “so đi sánh lại”, cho đến khi có “một ý kiến mà mọi người đều tán thành, hoặc số đông người tán thành”.",
      src: "Bài giảng Chương 5 của lớp (TS. Hà Triệu Huy), mục II.3.b — nguyên tắc 3 của Mặt trận · Hồ Chí Minh, Sửa đổi lối làm việc (10-1947), mục Cách lãnh đạo, Toàn tập t.5, tr.336" },
    P_DIEMCHUNG: { title: "Thống nhất mục tiêu và lợi ích",
      body: "Theo bài giảng Chương 5, khối đại đoàn kết chỉ bền chặt, lâu dài khi có sự thống nhất cao độ về mục tiêu và lợi ích: Mặt trận hoạt động trên cơ sở bảo đảm lợi ích tối cao của dân tộc và quyền lợi cơ bản của các tầng lớp nhân dân, giải quyết hài hòa lợi ích chung và lợi ích riêng. Nói chuyện với cán bộ, công nhân Nhà máy điện Yên Phụ và Nhà máy đèn Bờ Hồ (Hà Nội, tháng 12‑1954), Hồ Chí Minh nói: “Tuy khác nhau nhưng cùng chung một mục đích.” Nghị quyết 23‑NQ/TW (2003) cũng nêu: lấy mục tiêu độc lập, thống nhất, dân giàu, nước mạnh… “làm điểm tương đồng”.",
      src: "Bài giảng Chương 5 của lớp (TS. Hà Triệu Huy), mục II.3.b — nguyên tắc 2 của Mặt trận · Hồ Chí Minh, Toàn tập t.9, tr.203 · NQ 23-NQ/TW (12/3/2003)" },
    P_KHOANDUNG: { title: "Khoan dung, độ lượng với con người và niềm tin vào nhân dân",
      body: "Đây là những điều kiện để xây dựng khối đại đoàn kết. Hồ Chí Minh: “Năm ngón tay cũng có ngón vắn ngón dài. Nhưng vắn dài đều họp nhau lại nơi bàn tay. […] Vậy nên ta phải khoan hồng đại độ.”",
      src: "Bài giảng Chương 5 của lớp (TS. Hà Triệu Huy), mục II.2.b — điều kiện 2 và 3 · Thư gửi đồng bào Nam Bộ (1946), Toàn tập t.4, tr.280" },
    P_THATSU: { title: "Đoàn kết thực sự: vừa đoàn kết, vừa đấu tranh",
      body: "“Đoàn kết thực sự nghĩa là mục đích phải nhất trí và lập trường cũng phải nhất trí. Đoàn kết thực sự nghĩa là vừa đoàn kết, vừa đấu tranh, học những cái tốt của nhau, phê bình những cái sai của nhau và phê bình trên lập trường thân ái, vì nước, vì dân.”",
      src: "Hồ Chí Minh, nói tại Hội nghị mở rộng Ủy ban Trung ương MTTQ Việt Nam, 19-3-1958 · Toàn tập t.11, tr.362 · Bài giảng Chương 5 của lớp, nguyên tắc 4 của Mặt trận" },
    P_TOANDAN: { title: "Đại đoàn kết là đoàn kết toàn dân",
      body: "Chủ thể của khối đại đoàn kết là toàn dân — mọi người Việt Nam yêu nước, không phân biệt dân tộc, tôn giáo, giai cấp, tầng lớp, tuổi tác, giới tính, giàu nghèo; nền tảng là công nhân, nông dân và trí thức. Trong Thư gửi đồng bào Nam Bộ (1-6-1946), khẳng định Nam Bộ là một phần không thể tách rời của nước Việt Nam, Hồ Chí Minh viết: “Đồng bào Nam Bộ là dân nước Việt Nam. Sông có thể cạn, núi có thể mòn, song chân lý đó không bao giờ thay đổi!” Liên hệ câu này với chuyện tôn trọng khác biệt vùng miền trong một tập thể là cách vận dụng của nhóm.",
      src: "Bài giảng Chương 5 của lớp (TS. Hà Triệu Huy), mục II.2.a · Thư gửi đồng bào Nam Bộ (1-6-1946), Toàn tập t.4, tr.280" }
  };

  var SUMMARY = ["P_TOANDAN", "P_DIEMCHUNG", "P_HIEPTHUONG", "P_KHOANDUNG", "P_THATSU"];

  // ------------------------------------------------------------------ STATE
  var state = { step: "home", idx: 0, picks: [], warmup: null, warmupAfter: null };
  var app = document.getElementById("app");
  var topbar = document.getElementById("topbar");
  var progressText = document.getElementById("progressText");
  var progressFill = document.getElementById("progressFill");
  var floatCta = document.getElementById("floatCta");
  var wipe = document.getElementById("wipe");
  var wipePanel = document.getElementById("wipePanel");
  var LETTERS = ["A", "B", "C"];
  var MEDIA = window.UL_MEDIA || { faces: [], wide: {}, credits: [], mosaic: "" };

  // ------------------------------------------------------------------ MOTION (optional: GSAP, ScrollTrigger, SplitText, Lenis, confetti)
  var G = window.gsap;
  var REDUCED = !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  var ANIM = !!G && !REDUCED;
  var ST = ANIM && window.ScrollTrigger ? window.ScrollTrigger : null;
  var SPLIT = ANIM && window.SplitText ? window.SplitText : null;
  if (ANIM) {
    document.documentElement.classList.add("anim");
    if (ST) G.registerPlugin(ST);
    if (SPLIT) G.registerPlugin(SPLIT);
  }
  var ctx = null, lenis = null, heroObserver = null, busy = false;
  var lastX = innerWidth / 2, lastY = innerHeight / 2;
  document.addEventListener("pointerdown", function (e) { lastX = e.clientX; lastY = e.clientY; }, { passive: true });

  function motion(fn) {  // every tween / ScrollTrigger / SplitText made inside is reverted when the screen changes
    if (!ANIM) return;
    if (ctx) ctx.revert();
    ctx = G.context(fn, app);
  }
  function cleanup() {
    if (ctx) { ctx.revert(); ctx = null; }
    if (lenis) { G.ticker.remove(lenisRaf); lenis.destroy(); lenis = null; }
    if (heroObserver) { heroObserver.disconnect(); heroObserver = null; }
    floatCta.hidden = true;
  }
  function lenisRaf(t) { if (lenis) lenis.raf(t * 1000); }
  function smoothScroll() {  // desktop mouse/trackpad only; touch keeps native scrolling
    if (!ANIM || !window.Lenis || lenis || !(window.matchMedia && window.matchMedia("(pointer: fine)").matches)) return;
    lenis = new window.Lenis({ lerp: 0.1 });
    if (ST) lenis.on("scroll", ST.update);
    G.ticker.add(lenisRaf);
    G.ticker.lagSmoothing(0);
  }
  var PALETTE = ["#D2AA50", "#F0CF7A", "#FAF5E8", "#C33734", "#9C1214"];
  function burst(opts) {
    if (!ANIM || !window.confetti) return;
    window.confetti(Object.assign({ particleCount: 90, spread: 75, startVelocity: 42, ticks: 220, zIndex: 70,
      colors: PALETTE, disableForReducedMotion: true }, opts || {}));
  }
  function burstFrom(el, opts) {
    if (!el) return;
    var r = el.getBoundingClientRect();
    burst(Object.assign({ origin: { x: (r.left + r.width / 2) / innerWidth, y: (r.top + r.height / 2) / innerHeight } }, opts || {}));
  }
  function rnd(a, b) { return function () { return a + Math.random() * (b - a); }; }

  // screen change: a burgundy panel sweeps over, the next screen is built underneath, the panel leaves
  function swap(next) {
    if (!ANIM) { next(); return; }
    if (busy) return;
    busy = true;
    wipe.style.display = "block";
    G.timeline({ onComplete: function () { wipe.style.display = "none"; busy = false; } })
      .fromTo(wipePanel, { yPercent: 110 }, { yPercent: 0, duration: 0.42, ease: "power3.in" })
      .fromTo(".wipe-mark", { scale: 0.7, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.28, ease: "back.out(2.2)" }, "-=0.12")
      .add(next)
      .to(wipePanel, { yPercent: -110, duration: 0.58, ease: "power3.out", delay: 0.06 });
  }
  function enter() {  // content of a game screen rises in
    motion(function () {
      G.from(".screen > .card > *, .screen > .result-hero > *, .screen > .stack > *",
        { y: 26, autoAlpha: 0, duration: 0.55, stagger: 0.05, ease: "power3.out", clearProps: "transform,opacity,visibility", delay: 0.12 });
    });
  }
  function tap(btn, done) {  // ripple + small gold burst on a chosen answer
    btn.classList.add("chosen");
    if (!ANIM) { done(); return; }
    var r = btn.getBoundingClientRect(), size = Math.max(r.width, r.height) * 2.4;
    var x = (lastX >= r.left && lastX <= r.right) ? lastX : r.left + r.width / 2;
    var y = (lastY >= r.top && lastY <= r.bottom) ? lastY : r.top + r.height / 2;
    var rip = document.createElement("span");
    rip.className = "ripple";
    rip.style.cssText = "width:" + size + "px;height:" + size + "px;left:" + (x - r.left - size / 2) + "px;top:" + (y - r.top - size / 2) + "px";
    btn.appendChild(rip);
    G.to(rip, { scale: 1, autoAlpha: 0, duration: 0.6, ease: "power2.out" });
    G.fromTo(btn, { scale: 0.96 }, { scale: 1, duration: 0.4, ease: "back.out(3)" });
    burst({ particleCount: 28, spread: 55, startVelocity: 24, scalar: 0.7, ticks: 110, origin: { x: x / innerWidth, y: y / innerHeight } });
    setTimeout(done, 280);
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  var ICONS = {
    class: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5h18v11H3z"/><path d="M8 20h8M12 16v4"/></svg>',
    club: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M2 20c0-3.3 2.7-6 6-6s6 2.7 6 6M10 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/></svg>',
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/></svg>'
  };

  function setProgress(n) {
    progressText.textContent = n + "/3";
    progressFill.style.width = (n / 3 * 100) + "%";
  }

  function render(html, opts) {
    opts = opts || {};
    cleanup();
    topbar.hidden = !opts.bar;
    app.className = opts.cls || (opts.wide ? "wide" : "");
    app.innerHTML = '<section class="screen">' + html + "</section>";
    app.focus({ preventScroll: true });
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
    requestAnimationFrame(function () { window.scrollTo({ top: 0, left: 0, behavior: "instant" }); });
  }

  // ------------------------------------------------------------------ LANDING (home)
  function imgTag(o, eager, alt) {
    if (!o) return "";
    return '<img src="' + o.src + '" alt="' + esc(alt !== undefined ? alt : (o.alt || "")) + '"' +
      (o.w ? ' width="' + o.w + '" height="' + o.h + '"' : "") +
      ' loading="' + (eager ? "eager" : "lazy") + '" decoding="async">';
  }
  function marquee(cols) {
    var faces = MEDIA.faces || [];
    var out = "";
    for (var c = 0; c < cols; c++) {
      var list = faces.filter(function (f, i) { return i % cols === c; });
      var seq = list.concat(list).map(function (f) { return imgTag(f, true, ""); }).join("");
      out += '<div class="col"><div class="track" style="--dur:' + (38 + c * 7) + 's">' + seq + "</div></div>";
    }
    return '<div class="l-marquee" aria-hidden="true">' + out + "</div>";
  }

  function home() {
    state = { step: "home", idx: 0, picks: [], warmup: null, warmupAfter: null };
    var W = MEDIA.wide || {};
    var faces = (MEDIA.faces || []).map(function (f) {
      return '<figure>' + imgTag(f, false) + '<figcaption>' + esc(f.alt) + '</figcaption></figure>';
    }).join("");
    var hist = [
      ["h_badinh", "2/9/1945", "Lễ đài Quảng trường Ba Đình, Hà Nội · ảnh tư liệu (Wikimedia Commons)"],
      ["h_congiao", "2/9/1945", "Khối Trường Thần học Công giáo trong đoàn mít tinh Ngày Độc lập · album Philippe Devillers, Bảo tàng Lịch sử Quốc gia"],
      ["h_quochoi", "2/3/1946", "Đại biểu Quốc hội khóa I · quochoi.vn (Wikimedia Commons)"],
      ["h_ledai", "2/9/1945", "Toàn cảnh lễ đài Ba Đình · Trung tâm Lưu trữ quốc gia III — luutru.gov.vn"]
    ].map(function (h) {
      return '<figure class="h-card">' + imgTag(W[h[0]], false) + '<figcaption><b>' + h[1] + '</b>' + esc(h[2]) + '</figcaption></figure>';
    }).join("");
    var scale = [
      ["w_class", "LỚP HỌC", "sở thích, cách làm việc"],
      ["w_usth", "TRƯỜNG", "ngành học, quê quán, vùng miền"],
      ["w_tractor", "CỘNG ĐỒNG", "thế hệ, nghề nghiệp, tín ngưỡng"],
      ["w_flags", "QUỐC GIA", "dân tộc, tôn giáo, giai tầng, lợi ích"]
    ].map(function (s) {
      return '<div class="scale-item"><div class="img">' + imgTag(W[s[0]], false) + '</div><div><h3>' + s[1] + '</h3><p>' + esc(s[2]) + '</p></div></div>';
    }).join("");
    var cases = CASES.map(function (c, i) {
      return '<article class="case-card"><span class="n">' + (i + 1) + '</span><span class="case-tag">' + ICONS[c.icon] + esc(c.tag) + '</span>' +
        '<h3>' + esc(c.title) + '</h3><p>' + esc(c.situation.split(". ")[0]) + '.</p></article>';
    }).join("");
    var NP = 14, parts = "";
    for (var k = 0; k < NP; k++) parts += '<span class="p" data-i="' + k + '"></span>';
    var credits = (MEDIA.credits || []).map(function (c) {
      return '<li>' + esc(c.what) + ' — ' + esc(c.author) + ' · ' + esc(c.license) + ' · <a href="' + esc(c.page) + '" target="_blank" rel="noopener">nguồn</a></li>';
    }).join("");

    render(
      '<section class="l-hero" id="top">' + marquee(3) + '<div class="l-hero-shade"></div>' +
        '<div class="l-hero-content">' +
          '<span class="kicker">Tư tưởng Hồ Chí Minh · Đại đoàn kết dân tộc</span>' +
          '<h1 class="wordmark"><span class="w1">UNITY</span><span class="w2">LAB</span></h1>' +
          '<p class="lead">Bạn xử lý khác biệt như thế nào?</p>' +
          '<ul class="chips"><li>3 tình huống</li><li>~2 phút</li><li>Không chấm đúng / sai</li></ul>' +
          '<div class="hero-actions"><button class="btn btn-glow" id="start" type="button">Bắt đầu ngay <span aria-hidden="true">→</span></button>' +
          '<a class="scroll-hint" href="#story">Khám phá câu chuyện <span aria-hidden="true">↓</span></a></div>' +
          '<p class="foot"><strong>Tình huống là mô phỏng của nhóm</strong> (vận dụng đương đại), không phải nội dung giáo trình. Lựa chọn của bạn chỉ lưu trên máy bạn, không gửi đi đâu.</p>' +
        '</div>' +
      '</section>' +

      '<section class="l-sec l-neq" id="story">' +
        '<div style="text-align:center"><span class="label interp">Diễn giải của nhóm</span></div>' +
        '<h2 class="split"><span>ĐOÀN KẾT <span class="neq">≠</span></span> <span>ĐỒNG NHẤT</span></h2>' +
        '<div class="neq-stage" aria-hidden="true">' + parts + '<div class="center">ĐIỂM<br>CHUNG</div></div>' +
        '<div class="neq-legend"><div><b>ĐỒNG NHẤT</b>ai cũng giống hệt nhau</div><div><b>ĐOÀN KẾT</b>khác nhau — nhưng cùng hướng về điểm chung</div></div>' +
        '<blockquote class="quote"><p>“Tuy khác nhau nhưng cùng chung một mục đích.”</p>' +
        '<cite>Hồ Chí Minh, nói chuyện với cán bộ, công nhân Nhà máy điện Yên Phụ và Nhà máy đèn Bờ Hồ, 12-1954 · Toàn tập, t.9, tr.203</cite></blockquote>' +
      '</section>' +

      '<section class="l-sec l-faces">' +
        '<span class="label theory">Lý luận cốt lõi · Đoàn kết toàn dân</span>' +
        '<h2 class="split"><span>AI NẰM TRONG</span> <span class="gold">CHỮ “ĐẠI”?</span></h2>' +
        '<div class="mosaic-wrap">' + (MEDIA.mosaic ? '<img src="' + MEDIA.mosaic + '" alt="Chữ ĐẠI ghép từ 12 ảnh chụp những người Việt Nam khác nhau" loading="lazy" decoding="async">' : '') + '</div>' +
        '<p class="big-answer split">TOÀN <span>DÂN</span></p>' +
        '<p class="body">Chủ thể của khối đại đoàn kết là toàn thể nhân dân — mọi người Việt Nam yêu nước, không phân biệt dân tộc, tôn giáo, đảng phái, giai cấp, tầng lớp, già trẻ, gái trai, giàu nghèo; nền tảng là công nhân, nông dân và trí thức.</p>' +
        '<div class="face-grid">' + faces + '</div>' +
        '<blockquote class="quote"><p>“Bất kỳ đàn ông, đàn bà, bất kỳ người già, người trẻ, không chia tôn giáo, đảng phái, dân tộc. Hễ là người Việt Nam thì phải đứng lên đánh thực dân Pháp để cứu Tổ quốc.”</p>' +
        '<cite>Hồ Chí Minh, Lời kêu gọi toàn quốc kháng chiến, 19-12-1946 · Toàn tập, t.4, tr.534</cite></blockquote>' +
      '</section>' +

      '<section class="l-history" id="history">' +
        '<div class="h-head"><span class="label theory">Tư liệu lịch sử · phạm vi công cộng</span>' +
        '<h2 class="split" style="font-size:clamp(46px,12vw,110px)">1945 <span style="color:var(--gold-2)">—</span> 1946</h2>' +
        '<p class="body" style="font-size:18px;color:rgba(250,245,232,.84);max-width:640px">Những ngày đầu của nước Việt Nam Dân chủ Cộng hòa, qua ảnh tư liệu.</p></div>' +
        '<div class="h-scroller"><div class="h-track">' + hist +
          '<figure class="h-card quote-card"><p>“Đoàn kết, đoàn kết,<br>đại đoàn kết,<br>Thành công, thành công,<br>đại thành công.”</p>' +
          '<cite>Hồ Chí Minh, Đại hội đại biểu Mặt trận Tổ quốc Việt Nam lần thứ II, 25-4-1961 · Toàn tập, t.13, tr.120</cite></figure>' +
        '</div></div>' +
      '</section>' +

      '<section class="l-sec l-scale">' +
        '<span class="label app">Vận dụng của nhóm</span>' +
        '<h2 class="split"><span>TỪ MỘT LỚP HỌC</span> <span class="gold">ĐẾN CẢ QUỐC GIA</span></h2>' +
        '<div class="scale-list">' + scale + '</div>' +
        '<p class="body" style="margin-top:30px">Quy mô càng lớn, khác biệt càng phức tạp — vì vậy càng cần một điểm tương đồng ở tầm cao hơn.</p>' +
        '<blockquote class="quote"><p>“…lấy mục tiêu giữ vững độc lập, thống nhất của Tổ quốc, vì dân giàu, nước mạnh, xã hội công bằng, dân chủ, văn minh làm điểm tương đồng…”</p>' +
        '<cite>Nghị quyết 23-NQ/TW (12/3/2003) · tulieuvankien.dangcongsan.vn</cite></blockquote>' +
      '</section>' +

      '<section class="l-sec l-cases">' +
        '<span class="label app">Unity Lab · 3 tình huống</span>' +
        '<h2 class="split"><span>KHÔNG CÓ ĐÁP ÁN</span> <span class="gold">ĐÚNG / SAI</span></h2>' +
        '<p class="body">Chỉ có lựa chọn, lý do và rủi ro — mỗi lựa chọn gắn với một luận điểm lý luận về đại đoàn kết, có ghi nguồn.</p>' +
        '<div class="case-cards">' + cases + '</div>' +
      '</section>' +

      '<section class="l-final">' +
        '<h2 class="split">SẴN <span style="color:var(--gold-2)">SÀNG?</span></h2>' +
        '<button class="btn btn-glow" id="start2" type="button">Bắt đầu Unity Lab <span aria-hidden="true">→</span></button>' +
        '<p class="foot" style="max-width:640px;margin:26px auto 0">' + esc(CONFIG.groupLine) + '<br>Các trích dẫn Hồ Chí Minh đã đối chiếu nguyên văn với Toàn tập (NXB CTQG Sự thật, 2011); trích Nghị quyết 23-NQ/TW theo tulieuvankien.dangcongsan.vn. Tình huống, “phong cách” và các phần ghi “Diễn giải / Vận dụng của nhóm” là phần của nhóm.</p>' +
        '<details class="credits"><summary>Nguồn ảnh &amp; phông chữ</summary><ul>' + credits +
          '<li>Phông chữ: Phudu, Be Vietnam Pro (SIL Open Font License) · Hoạ tiết trống đồng: nhóm tự vẽ.</li></ul>' +
          '<p>Ảnh đã được thu nhỏ, cắt khung và chỉnh màu; ảnh CC BY-SA 4.0 được chia sẻ lại theo cùng giấy phép.</p></details>' +
      '</section>',
      { cls: "landing" }
    );
    var go = function (e) { burstFrom(e && e.currentTarget, { particleCount: 70, spread: 80, startVelocity: 38 }); swap(warmup); };
    document.getElementById("start").onclick = go;
    document.getElementById("start2").onclick = go;
    floatCta.onclick = go;
    var hint = app.querySelector(".scroll-hint");
    hint.onclick = function (e) {
      e.preventDefault();
      var t = document.getElementById("story");
      if (lenis) lenis.scrollTo(t, { duration: 1.4 }); else t.scrollIntoView({ behavior: REDUCED ? "auto" : "smooth" });
    };
    neqFinal(!ANIM);  // without animation: show the "converged" picture straight away
    if ("IntersectionObserver" in window) {  // floating CTA once the hero is off screen
      var heroEl = app.querySelector(".l-hero");
      heroObserver = new IntersectionObserver(function (en) { floatCta.hidden = en[0].isIntersecting; }, { threshold: 0.05 });
      heroObserver.observe(heroEl);
    }
    if (ANIM) {
      var startAnim = function () { if (state.step === "home" && app.classList.contains("landing")) landingMotion(); };
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(startAnim); else startAnim();
    }
  }

  // the "≠" picture: identical dots (a grid) -> diverse shapes converging around a shared centre
  var SHAPES = ["50% 50% 50% 50%", "18% 18% 18% 18%", "50% 0% 50% 0%", "0% 0% 0% 0%", "50% 50% 8% 50%"];  // 4 values each so GSAP can morph them
  var NEQ_COLORS = ["#D2AA50", "#C33734", "#FAF5E8", "#F0CF7A", "#9C1214", "#EFE3CE", "#B68A45"];
  function neqTarget(i, n) {
    var a = (i / n) * Math.PI * 2 - Math.PI / 2;
    var rx = 330 + (i % 3) * 45, ry = 205 + (i % 2) * 40;
    return { xPercent: Math.cos(a) * rx, yPercent: Math.sin(a) * ry, scale: 0.65 + ((i * 37) % 9) / 10,
      rotation: (i * 53) % 90 - 45, backgroundColor: NEQ_COLORS[i % NEQ_COLORS.length], borderRadius: SHAPES[i % SHAPES.length], opacity: 1 };
  }
  function neqGrid(i, n) {
    var cols = 7, row = Math.floor(i / cols), col = i % cols;
    return { xPercent: (col - (cols - 1) / 2) * 125, yPercent: (row - 0.5) * 125, scale: 1, rotation: 0, backgroundColor: "#EFE3CE", borderRadius: "50% 50% 50% 50%", opacity: 0.85 };
  }
  function neqFinal(apply) {
    if (!apply) return;
    var ps = app.querySelectorAll(".neq-stage .p"), n = ps.length;
    ps.forEach(function (p, i) {
      var t = neqTarget(i, n);
      p.style.transform = "translate(" + t.xPercent + "%," + t.yPercent + "%) rotate(" + t.rotation + "deg) scale(" + t.scale + ")";
      p.style.background = t.backgroundColor; p.style.borderRadius = t.borderRadius; p.style.opacity = 1;
    });
    var c = app.querySelector(".neq-stage .center");
    if (c) { c.style.opacity = 1; c.style.transform = "translate(-50%,-50%) scale(1)"; }
  }

  function landingMotion() {
    motion(function () {
      // 1) hero entrance: letters fly in, everything else rises, then a gold burst from the title
      var tl = G.timeline({ defaults: { ease: "power3.out" } });
      tl.from(".l-marquee", { scale: 1.45, autoAlpha: 0, duration: 1.5, ease: "expo.out" }, 0);
      if (SPLIT) {
        var hs = SPLIT.create(".l-hero .wordmark .w1, .l-hero .wordmark .w2", { type: "chars" });
        tl.from(hs.chars, { yPercent: 130, rotation: rnd(-40, 40), scale: 0.5, autoAlpha: 0, duration: 0.85, stagger: 0.05, ease: "back.out(1.7)" }, 0.1);
      }
      tl.from(".l-hero .kicker", { y: 16, autoAlpha: 0, duration: 0.5 }, 0.05)
        .from(".l-hero .lead, .l-hero .chips li, .hero-actions > *, .l-hero .foot", { y: 24, autoAlpha: 0, stagger: 0.06, duration: 0.6 }, 0.45)
        .add(function () { burstFrom(app.querySelector(".l-hero .wordmark"), { particleCount: 140, spread: 120, startVelocity: 50, scalar: 0.95 }); }, 0.8);
      if (!ST) return;
      // 2) parallax hero on scroll
      G.to(".l-marquee", { yPercent: 12, ease: "none", scrollTrigger: { trigger: ".l-hero", start: "top top", end: "bottom top", scrub: true } });
      G.to(".l-hero-content", { yPercent: -18, autoAlpha: 0.2, ease: "none", scrollTrigger: { trigger: ".l-hero", start: "top top", end: "bottom top", scrub: true } });
      // 3) every section heading: letters rise in
      G.utils.toArray(".l-sec h2.split, .l-history h2.split, .l-final h2.split, .big-answer.split").forEach(function (h) {
        var parts = SPLIT ? SPLIT.create(h, { type: "chars" }).chars : [h];
        G.from(parts, { yPercent: 110, autoAlpha: 0, rotation: rnd(-12, 12), duration: 0.7, stagger: 0.025, ease: "back.out(1.6)",
          scrollTrigger: { trigger: h, start: "top 85%" } });
      });
      G.utils.toArray(".l-sec .label, .l-sec p.body, .quote, .h-head .label, .h-head p, .neq-legend").forEach(function (el) {
        G.from(el, { y: 34, autoAlpha: 0, duration: 0.8, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 88%" } });
      });
      // 4) ≠ : identical grid scatters into a diverse ring around the shared centre (scrubbed)
      var ps = G.utils.toArray(".neq-stage .p"), n = ps.length;
      ps.forEach(function (p, i) { G.set(p, neqGrid(i, n)); });
      G.set(".neq-stage .center", { x: 0, y: 0, xPercent: -50, yPercent: -50, scale: 0.2, autoAlpha: 0 });
      var nt = G.timeline({ scrollTrigger: { trigger: ".neq-stage", start: "top 75%", end: "bottom 35%", scrub: 1 } });
      ps.forEach(function (p, i) { nt.to(p, Object.assign({ duration: 1, ease: "power2.inOut" }, neqTarget(i, n)), i * 0.03); });
      nt.to(".neq-stage .center", { scale: 1, autoAlpha: 1, duration: 0.6, ease: "back.out(2)" }, 0.55);
      G.fromTo(".l-neq .neq", { rotation: -90, scale: 0.4 }, { rotation: 0, scale: 1, ease: "elastic.out(1, .5)", duration: 1.4,
        scrollTrigger: { trigger: ".l-neq h2", start: "top 80%" } });
      // 5) the ĐẠI mosaic opens like an aperture, faces fly in from everywhere
      G.fromTo(".mosaic-wrap", { clipPath: "inset(42% 42% 42% 42% round 40px)", scale: 0.85 },
        { clipPath: "inset(0% 0% 0% 0% round 0px)", scale: 1, ease: "none", scrollTrigger: { trigger: ".mosaic-wrap", start: "top 90%", end: "top 30%", scrub: 1 } });
      G.from(".face-grid figure", { y: 90, rotation: rnd(-14, 14), scale: 0.8, autoAlpha: 0, duration: 0.9, ease: "back.out(1.4)",
        stagger: { each: 0.05, from: "random" }, scrollTrigger: { trigger: ".face-grid", start: "top 85%" } });
      // 6) history: pinned horizontal gallery
      var track = app.querySelector(".h-track"), hist = app.querySelector(".l-history");
      var dist = function () { return Math.max(0, track.scrollWidth - innerWidth + 36); };
      G.to(track, { x: function () { return -dist(); }, ease: "none",
        scrollTrigger: { trigger: hist, start: "top top", end: function () { return "+=" + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true, anticipatePin: 1 } });
      // 7) classroom -> nation: each picture grows in, a little bigger each step
      G.utils.toArray(".scale-item").forEach(function (it, i) {
        G.from(it.querySelector(".img"), { scale: 0.55 + i * 0.05, autoAlpha: 0, y: 60, rotation: i % 2 ? 4 : -4, ease: "power3.out", duration: 1,
          scrollTrigger: { trigger: it, start: "top 88%" } });
        G.from(it.querySelector("h3"), { x: -40, autoAlpha: 0, duration: 0.7, delay: 0.15, ease: "power3.out", scrollTrigger: { trigger: it, start: "top 88%" } });
      });
      // 8) case cards flip up
      G.from(".case-card", { rotationX: -75, y: 80, autoAlpha: 0, transformOrigin: "50% 100%", duration: 1, ease: "back.out(1.3)", stagger: 0.14,
        scrollTrigger: { trigger: ".case-cards", start: "top 85%" } });
      if (window.matchMedia && window.matchMedia("(pointer: fine)").matches) {  // desktop: cards tilt toward the pointer
        G.utils.toArray(".case-card").forEach(function (card) {
          card.addEventListener("mouseenter", function () { G.to(card, { rotationX: 4, rotationY: -6, y: -6, duration: 0.45, ease: "power3.out", overwrite: "auto" }); });
          card.addEventListener("mouseleave", function () { G.to(card, { rotationX: 0, rotationY: 0, y: 0, duration: 0.6, ease: "elastic.out(1, .6)", overwrite: "auto" }); });
        });
      }
      // 9) final call: button pops + burst when it arrives
      G.from("#start2", { scale: 0.4, autoAlpha: 0, duration: 0.9, ease: "elastic.out(1, .5)",
        scrollTrigger: { trigger: "#start2", start: "top 92%", onEnter: function () { burstFrom(document.getElementById("start2"), { particleCount: 90, spread: 90 }); } } });
    });
    smoothScroll();
    if (ST) {
      window.addEventListener("load", function () { ST.refresh(); }, { once: true });
      app.querySelectorAll("img[loading=lazy]").forEach(function (im) { im.addEventListener("load", function () { ST.refresh(); }, { once: true }); });
    }
  }

  // ------------------------------------------------------------------ GAME SCREENS
  function pollButtons(selected) {
    return WARMUP.options.map(function (o) {
      return '<button class="choice" type="button" data-k="' + o.k + '" aria-pressed="' + (selected === o.k) + '">' +
        '<span class="letter">' + o.k + '</span><span>' + esc(o.t) + '</span></button>';
    }).join("");
  }

  function warmup() {
    state.step = "warmup";
    render(
      '<div class="card">' +
        '<span class="kicker">Khởi động · câu hỏi đầu buổi</span>' +
        '<h2>' + esc(WARMUP.q) + '</h2>' +
        '<p class="muted small" style="color:var(--muted)">Đầu buổi bạn đã giơ mấy ngón tay? Chọn lại đáp án đó (hoặc chọn theo trực giác). Cuối game bạn sẽ được chọn lại.</p>' +
        '<div class="poll">' + pollButtons(null) + '</div>' +
      '</div>'
    );
    enter();
    app.querySelectorAll(".poll .choice").forEach(function (b) {
      b.onclick = function () { tap(b, function () { state.warmup = b.dataset.k; state.idx = 0; swap(showCase); }); };
    });
  }

  function showCase() {
    state.step = "case";
    var c = CASES[state.idx];
    var choices = c.choices.map(function (ch, i) {
      return '<button class="choice" type="button" data-i="' + i + '"><span class="letter">' + LETTERS[i] + '</span><span>' + esc(ch.t) + '</span></button>';
    }).join("");
    render(
      '<div class="card">' +
        '<span class="case-tag">' + ICONS[c.icon] + 'Tình huống ' + (state.idx + 1) + ' · ' + esc(c.tag) + '</span>' +
        '<h2>' + esc(c.title) + '</h2>' +
        '<p class="situation">' + esc(c.situation) + '</p>' +
        '<p class="question">' + esc(c.question) + '</p>' +
        '<div class="choices">' + choices + '</div>' +
      '</div>',
      { bar: true }
    );
    setProgress(state.idx + 1);
    enter();
    app.querySelectorAll(".choices .choice").forEach(function (b) {
      b.onclick = function () { tap(b, function () { state.picks[state.idx] = +b.dataset.i; swap(feedback); }); };
    });
  }

  function feedback() {
    state.step = "feedback";
    var c = CASES[state.idx];
    var i = state.picks[state.idx];
    var ch = c.choices[i];
    var p = PRINCIPLES[ch.principle];
    var others = c.choices.map(function (o, j) {
      if (j === i) return "";
      return '<li><strong>' + LETTERS[j] + '.</strong> Ưu tiên: ' + esc(o.priority) + ' <em>Rủi ro:</em> ' + esc(o.risk) + '</li>';
    }).join("");
    var last = state.idx === CASES.length - 1;
    render(
      '<div class="card">' +
        '<span class="case-tag">' + ICONS[c.icon] + 'Phản hồi · Tình huống ' + (state.idx + 1) + '</span>' +
        '<div class="picked"><span class="letter">' + LETTERS[i] + '</span><span>' + esc(ch.t) + '</span></div>' +
        '<div class="fb-block"><h3>Lựa chọn này ưu tiên điều gì?</h3><p>' + esc(ch.priority) + '</p></div>' +
        '<div class="fb-block"><h3>Rủi ro của lựa chọn này?</h3><p>' + esc(ch.risk) + '</p></div>' +
        '<div class="fb-block principle"><h3>Luận điểm lý luận liên quan</h3><p><strong>' + esc(p.title) + '.</strong> ' + esc(p.body) + '</p><span class="src">Nguồn: ' + esc(p.src) + '</span></div>' +
        '<details class="others"><summary>So sánh với 2 lựa chọn còn lại</summary><ul>' + others + '</ul></details>' +
        '<div class="actions"><button class="btn" id="next" type="button">' + (last ? "Xem kết quả" : "Tình huống tiếp theo") + '</button></div>' +
      '</div>',
      { bar: true }
    );
    setProgress(state.idx + 1);
    enter();
    document.getElementById("next").onclick = function () {
      if (last) { swap(result); } else { state.idx++; swap(showCase); }
    };
  }

  function profile() {
    var count = { connect: 0, decide: 0, avoid: 0 };
    state.picks.forEach(function (pi, ci) { count[CASES[ci].choices[pi].style]++; });
    var best = "mixed";
    Object.keys(count).forEach(function (k) { if (count[k] >= 2) best = k; });
    return { key: best, count: count };
  }

  var STYLE_COLORS = {
    connect: ["#D2AA50", "#F0CF7A", "#FAF5E8", "#B68A45"],
    decide: ["#C33734", "#9C1214", "#F0CF7A", "#FAF5E8"],
    avoid: ["#EFE3CE", "#FAF5E8", "#D2AA50", "#B68A45"],
    mixed: ["#D2AA50", "#C33734", "#EFE3CE", "#F0CF7A", "#9C1214"]
  };

  function result() {
    state.step = "result";
    var pr = profile();
    var st = STYLES[pr.key];
    var journey = state.picks.map(function (pi, ci) {
      var s = CASES[ci].choices[pi].style;
      return '<div class="' + STYLES[s].cls + '"><b>' + LETTERS[pi] + '</b>' + esc(CASES[ci].tag) + '</div>';
    }).join("");
    var list = SUMMARY.map(function (k) {
      var p = PRINCIPLES[k];
      return '<li><details><summary><strong>' + esc(p.title) + '</strong></summary><p>' + esc(p.body) + '</p><span class="src">' + esc(p.src) + '</span></details></li>';
    }).join("");
    render(
      '<div class="result-hero">' +
        '<span class="kicker">3/3 · Hoàn thành</span>' +
        '<h1>Bạn vừa hoàn thành Unity Lab.</h1>' +
        '<div class="badge ' + st.cls + '"><div><small>THẺ ' + esc(st.color) + '</small>' + esc(st.name) + '</div></div>' +
        '<p class="color-code">Khi nhóm thuyết trình hỏi, hãy giơ tay theo màu thẻ của bạn.</p>' +
      '</div>' +
      '<div class="stack">' +
        '<div class="card">' +
          '<span class="kicker">Cách bạn xử lý khác biệt</span>' +
          '<p style="margin-top:8px">' + esc(st.text) + '</p>' +
          '<p class="small" style="color:var(--muted)">' + esc(st.watch) + '</p>' +
          '<div class="journey">' + journey + '</div>' +
          '<p class="small" style="color:var(--muted);margin:6px 0 0">“Phong cách” là cách nhóm gợi ý để tự soi chiếu — không phải phân loại trong giáo trình.</p>' +
        '</div>' +
        '<div class="card">' +
          '<span class="kicker">Quay lại câu hỏi khởi động</span>' +
          '<h2>' + esc(WARMUP.q) + '</h2>' +
          '<p class="small" style="color:var(--muted)">Lúc đầu bạn chọn <strong>' + esc(state.warmup || "—") + '</strong>. Sau 3 tình huống, bạn chọn lại?</p>' +
          '<div class="poll" id="poll2">' + pollButtons(state.warmupAfter) + '</div>' +
          '<div id="pollNote"></div>' +
        '</div>' +
        '<div class="card">' +
          '<span class="kicker">Những luận điểm bạn vừa chạm tới</span>' +
          '<p class="small" style="color:var(--muted);margin:6px 0 0">Chạm vào từng luận điểm để xem trích dẫn và nguồn.</p>' +
          '<ol class="principles">' + list + '</ol>' +
          '<p class="small" style="color:var(--muted);margin-top:10px">Trích dẫn đã đối chiếu nguyên văn với Hồ Chí Minh Toàn tập (NXB CTQG Sự thật, 2011); phần khái quát lý luận theo bài giảng Chương 5 của lớp (TS. Hà Triệu Huy), đối chiếu thêm đề cương các trường và bài viết chính thống (chưa đối chiếu bản in giáo trình 2021). Tình huống và “phong cách” là phần vận dụng, diễn giải của nhóm.</p>' +
        '</div>' +
        '<div class="actions"><button class="btn ghost" id="again" type="button">Chơi lại</button></div>' +
      '</div>'
    );
    if (ANIM) {
      motion(function () {
        var tl = G.timeline({ delay: 0.15 });
        tl.from(".result-hero .kicker", { y: 14, autoAlpha: 0, duration: 0.4 });
        if (SPLIT) {
          var sp = SPLIT.create(".result-hero h1", { type: "words,chars" });
          tl.from(sp.chars, { yPercent: 120, rotation: rnd(-25, 25), autoAlpha: 0, duration: 0.6, stagger: 0.02, ease: "back.out(1.8)" }, 0.1);
        }
        tl.from(".badge", { scale: 0, rotation: -220, duration: 1.1, ease: "elastic.out(1, .55)",
            onStart: function () {
              var col = STYLE_COLORS[pr.key];
              setTimeout(function () {
                burstFrom(app.querySelector(".badge"), { particleCount: 170, spread: 110, startVelocity: 55, colors: col });
                setTimeout(function () {
                  burst({ particleCount: 90, angle: 60, spread: 70, origin: { x: 0, y: 0.75 }, colors: col });
                  burst({ particleCount: 90, angle: 120, spread: 70, origin: { x: 1, y: 0.75 }, colors: col });
                }, 380);
              }, 300);
            } }, 0.45)
          .from(".color-code", { y: 16, autoAlpha: 0, duration: 0.5 }, 1.0)
          .from(".stack > *", { y: 40, autoAlpha: 0, stagger: 0.1, duration: 0.6, ease: "power3.out", clearProps: "transform,opacity,visibility" }, 1.1);
        G.to(".badge", { y: -6, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: -1, delay: 1.8 });
      });
    }
    app.querySelectorAll("#poll2 .choice").forEach(function (b) {
      b.onclick = function () {
        state.warmupAfter = b.dataset.k;
        app.querySelectorAll("#poll2 .choice").forEach(function (x) { x.setAttribute("aria-pressed", x === b); });
        var same = state.warmup === state.warmupAfter;
        document.getElementById("pollNote").innerHTML =
          '<div class="compare"><div><b>Lúc đầu</b>' + esc(state.warmup || "—") + '</div><div><b>Bây giờ</b>' + esc(state.warmupAfter) + '</div></div>' +
          '<p class="small" style="color:var(--muted);margin-top:10px">' + (same ? "Bạn giữ nguyên lựa chọn." : "Bạn đã đổi lựa chọn.") +
          ' Nhóm sẽ cùng cả lớp quay lại câu hỏi này ngay ở slide tiếp theo.</p>';
        if (ANIM) G.from("#pollNote > *", { y: 12, autoAlpha: 0, stagger: 0.08, duration: 0.4 });
      };
    });
    document.getElementById("again").onclick = function () { swap(home); };
  }

  // ------------------------------------------------------------------ PRESENTER MODE
  // Mở: .../?present  → QR thật của chính địa chỉ đang chạy + đồng hồ đếm ngược, nền ảnh chuyển động.
  function presenter() {
    state.step = "present";
    var url = location.href.split("?")[0].split("#")[0].replace(/index\.html$/, "");
    render(
      '<div class="present-bg" aria-hidden="true">' + marquee(4) + '</div>' +
      '<div class="present">' +
        '<div class="left">' +
          '<p class="present-cta">Quét mã để tham gia</p>' +
          '<h1 class="wordmark">UNITY<span>LAB</span></h1>' +
          '<p class="url">' + esc(url) + '</p>' +
          '<div class="timer" id="timer">' + fmt(CONFIG.presentSeconds) + '</div>' +
          '<div class="actions" style="justify-content:center"><button class="btn" id="go" type="button">Bắt đầu đếm giờ</button></div>' +
        '</div>' +
        '<div class="qr-box" id="qr" role="img" aria-label="Mã QR dẫn tới Unity Lab"><p style="color:#5B0808;margin:40px 0">Đang tạo mã QR…</p></div>' +
      '</div>',
      { wide: true }
    );
    if (ANIM) {
      motion(function () {
        var tl = G.timeline({ defaults: { ease: "power3.out" } });
        tl.from(".present-bg", { autoAlpha: 0, duration: 1.2 }, 0);
        if (SPLIT) {
          var sp = SPLIT.create(".present .wordmark", { type: "chars" });
          tl.from(sp.chars, { yPercent: 130, rotation: rnd(-30, 30), autoAlpha: 0, stagger: 0.05, duration: 0.8, ease: "back.out(1.7)" }, 0.1);
        }
        tl.from(".present-cta, .url, .timer, .present .actions", { y: 24, autoAlpha: 0, stagger: 0.08, duration: 0.6 }, 0.35)
          .from(".qr-box", { scale: 0.3, rotation: 12, autoAlpha: 0, duration: 1.1, ease: "elastic.out(1, .6)" }, 0.4);
      });
    }
    loadQR(function (ok) {
      var box = document.getElementById("qr");
      if (!ok) { box.innerHTML = '<p style="color:#5B0808">Không tải được thư viện QR (cần Internet). Hãy dùng địa chỉ bên dưới.</p>'; return; }
      var qr = window.qrcode(0, "M");
      qr.addData(url);
      qr.make();
      box.innerHTML = qr.createSvgTag({ cellSize: 8, margin: 32, scalable: true });  // margin is in px: 32 = 4 modules (quiet zone)
    });
    var left = CONFIG.presentSeconds, timer = null;
    document.getElementById("go").onclick = function (e) {
      if (timer) return;
      burstFrom(e.currentTarget, { particleCount: 80, spread: 90 });
      timer = setInterval(function () {
        left = Math.max(0, left - 1);
        var t = document.getElementById("timer");
        t.textContent = fmt(left);
        if (ANIM && left <= 10) G.fromTo(t, { scale: 1.18, color: "#F0CF7A" }, { scale: 1, color: "#D2AA50", duration: 0.6, ease: "back.out(3)" });
        if (!left) { clearInterval(timer); burstFrom(t, { particleCount: 200, spread: 140, startVelocity: 60 }); }
      }, 1000);
    };
  }

  function fmt(s) { return Math.floor(s / 60) + ":" + ("0" + (s % 60)).slice(-2); }

  function loadQR(cb) {
    var srcs = [
      "https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js",
      "https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.min.js"
    ];
    (function next(i) {
      if (window.qrcode) return cb(true);
      if (i >= srcs.length) return cb(false);
      var s = document.createElement("script");
      s.src = srcs[i];
      s.onload = function () { cb(!!window.qrcode); };
      s.onerror = function () { next(i + 1); };
      document.head.appendChild(s);
    })(0);
  }

  document.getElementById("homeLink").onclick = function () { swap(home); };
  if (/[?&]present\b/.test(location.search) || location.hash === "#present") presenter(); else home();
})();
