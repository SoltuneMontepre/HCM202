"""Small helper layer over python-pptx for the HCM great-national-unity deck.

Everything is positioned in inches on a 13.333 x 7.5 in (16:9) canvas.
Text stays native and editable; photographic treatments are baked by imgfx.py.
"""
import re
from copy import deepcopy
from lxml import etree
from pptx import Presentation
from vn_wrap import bind_compounds
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn
from PIL import Image

W, H = 13.333, 7.5
# Fonts (SIL OFL, Google Fonts; files in 12_assets/fonts/src, installed per-user, embedded on export)
DISPLAY = "Phudu"                  # headline family; bold runs are drawn with DISPLAY_HEAVY
DISPLAY_HEAVY = "Phudu ExtraBold"
DISPLAY_BLACK = "Phudu Black"
BODY = "Be Vietnam Pro"
BODY_SEMI = "Be Vietnam Pro SemiBold"
BODY_BOLD = "Be Vietnam Pro"       # use bold=True
BODY_SCALE = 0.93                  # Be Vietnam Pro is ~8% wider than the old Segoe UI; keeps line breaks and apparent size
ITALIC_SCALE = 0.91                # Phudu has no italic: display italics are set in Be Vietnam Pro Italic
DISPLAY_SCALE = 1.1                # Phudu is narrow (caps ~77% of Constantia's width): headlines >= 20 pt get 10% larger

C = dict(
    burg="5B0808", crim="7A0B0C", red="9C1214", warm="C33734",
    ivory="FAF5E8", cream="EFE3CE", gold="B68A45", gold2="D2AA50",
    brown="4C3026", ink="2A1712", muted="6E564B", white="FFFFFF", black="000000",
    deep="3A0405", paper2="F3E8D6",
)

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"


def rgb(h):
    return RGBColor.from_string(C.get(h, h))


def new_deck():
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    return prs


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


# ------------------------------------------------------------------ images
def add_bg(slide, path):
    pic = slide.shapes.add_picture(str(path), 0, 0, Inches(W), Inches(H))
    pic.name = "Background"
    # move to back
    sp = pic._element
    sp.getparent().remove(sp)
    slide.shapes._spTree.insert(2, sp)
    return pic


def add_img(slide, path, x, y, w, h, focus=(0.5, 0.5), name=None, shape=None, radius=None, alpha=None):
    """Place an image filling the box (object-fit: cover) by cropping, never stretching.
    focus = (fx, fy) in 0..1 — the point of the source image to keep centred."""
    with Image.open(path) as im:
        iw, ih = im.size
    box_ar = w / h
    img_ar = iw / ih
    pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(w), Inches(h))
    if img_ar > box_ar:  # too wide -> crop left/right
        keep = box_ar / img_ar
        cx = min(max(focus[0] - keep / 2, 0), 1 - keep)
        pic.crop_left, pic.crop_right = cx, 1 - keep - cx
    elif img_ar < box_ar:  # too tall -> crop top/bottom
        keep = img_ar / box_ar
        cy = min(max(focus[1] - keep / 2, 0), 1 - keep)
        pic.crop_top, pic.crop_bottom = cy, 1 - keep - cy
    if shape is not None:
        pic.auto_shape_type = shape
        if radius is not None:
            _set_adj(pic._element.spPr, radius)
    if alpha is not None:
        set_pic_alpha(pic, alpha)
    if name:
        pic.name = name
    return pic


def add_img_fit(slide, path, x, y, w=None, h=None, name=None):
    """Place an image at its natural aspect ratio given a width or a height."""
    with Image.open(path) as im:
        iw, ih = im.size
    if w is not None and h is None:
        h = w * ih / iw
    elif h is not None and w is None:
        w = h * iw / ih
    pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        pic.name = name
    return pic


def set_pic_alpha(pic, alpha):
    """alpha 0..1 opacity of a picture."""
    blip = pic._element.find(".//" + qn("a:blip"))
    for old in blip.findall(qn("a:alphaModFix")):
        blip.remove(old)
    el = etree.SubElement(blip, qn("a:alphaModFix"))
    el.set("amt", str(int(alpha * 100000)))


def _set_adj(spPr, val):
    geom = spPr.find(qn("a:prstGeom"))
    av = geom.find(qn("a:avLst"))
    if av is None:
        av = etree.SubElement(geom, qn("a:avLst"))
    for g in list(av):
        av.remove(g)
    gd = etree.SubElement(av, qn("a:gd"))
    gd.set("name", "adj")
    gd.set("fmla", f"val {int(val)}")


# ------------------------------------------------------------------ shapes
def _alpha(fill_parent, alpha):
    """add <a:alpha> to the colour inside a solidFill"""
    clr = fill_parent.find(qn("a:srgbClr"))
    if clr is not None and alpha is not None and alpha < 1:
        a = etree.SubElement(clr, qn("a:alpha"))
        a.set("val", str(int(alpha * 100000)))


def rect(slide, x, y, w, h, fill=None, line=None, line_w=None, alpha=None, radius=None, shape=None, name=None, line_alpha=None, dash=None):
    st = shape or (MSO_SHAPE.ROUNDED_RECTANGLE if radius is not None else MSO_SHAPE.RECTANGLE)
    s = slide.shapes.add_shape(st, Inches(x), Inches(y), Inches(w), Inches(h))
    if radius is not None and st == MSO_SHAPE.ROUNDED_RECTANGLE:
        _set_adj(s._element.spPr, radius)
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = rgb(fill)
        _alpha(s.fill._xPr.find(qn("a:solidFill")), alpha)
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = rgb(line)
        s.line.width = Pt(line_w or 1)
        if line_alpha is not None:
            ln = s._element.spPr.find(qn("a:ln"))
            _alpha(ln.find(qn("a:solidFill")), line_alpha)
        if dash:
            ln = s._element.spPr.find(qn("a:ln"))
            pd = etree.SubElement(ln, qn("a:prstDash"))
            pd.set("val", dash)
    s.shadow.inherit = False
    tf = s.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    if name:
        s.name = name
    return s


def grad_rect(slide, x, y, w, h, stops, angle=0, name=None):
    """stops: list of (pos 0..1, hex, alpha 0..1). angle in degrees (0 = left->right, 90 = top->bottom)."""
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.line.fill.background()
    s.shadow.inherit = False
    spPr = s._element.spPr
    for tag in ("a:solidFill", "a:noFill", "a:gradFill"):
        for el in spPr.findall(qn(tag)):
            spPr.remove(el)
    grad = etree.Element(qn("a:gradFill"))
    grad.set("rotWithShape", "1")
    gs_lst = etree.SubElement(grad, qn("a:gsLst"))
    for pos, hexc, a in stops:
        gs = etree.SubElement(gs_lst, qn("a:gs"))
        gs.set("pos", str(int(pos * 100000)))
        clr = etree.SubElement(gs, qn("a:srgbClr"))
        clr.set("val", hexc)
        if a < 1:
            al = etree.SubElement(clr, qn("a:alpha"))
            al.set("val", str(int(a * 100000)))
    lin = etree.SubElement(grad, qn("a:lin"))
    lin.set("ang", str(int(angle * 60000)))
    lin.set("scaled", "0")
    # gradFill must come right after the geometry
    geom = spPr.find(qn("a:prstGeom"))
    geom.addnext(grad)
    if name:
        s.name = name
    return s


def line(slide, x1, y1, x2, y2, color, width=1.0, alpha=None, dash=None, name=None):
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    ln.line.color.rgb = rgb(color)
    ln.line.width = Pt(width)
    lnel = ln._element.spPr.find(qn("a:ln"))
    if alpha is not None:
        _alpha(lnel.find(qn("a:solidFill")), alpha)
    if dash:
        pd = etree.SubElement(lnel, qn("a:prstDash"))
        pd.set("val", dash)
    if name:
        ln.name = name
    return ln


def arrow(slide, x1, y1, x2, y2, color, width=1.5, name=None):
    ln = line(slide, x1, y1, x2, y2, color, width, name=name)
    lnel = ln._element.spPr.find(qn("a:ln"))
    te = etree.SubElement(lnel, qn("a:tailEnd"))
    te.set("type", "triangle")
    te.set("w", "med")
    te.set("len", "med")
    return ln


def shadow(shape, blur=18, dist=6, alpha=0.35, color="000000", angle=90):
    spPr = shape._element.spPr
    eff = spPr.find(qn("a:effectLst"))
    if eff is None:
        eff = etree.SubElement(spPr, qn("a:effectLst"))
    for old in list(eff):
        eff.remove(old)
    sh = etree.SubElement(eff, qn("a:outerShdw"))
    sh.set("blurRad", str(int(Pt(blur))))
    sh.set("dist", str(int(Pt(dist))))
    sh.set("dir", str(int(angle * 60000)))
    sh.set("algn", "t")
    sh.set("rotWithShape", "0")
    clr = etree.SubElement(sh, qn("a:srgbClr"))
    clr.set("val", color)
    a = etree.SubElement(clr, qn("a:alpha"))
    a.set("val", str(int(alpha * 100000)))


# ------------------------------------------------------------------ text
def text(slide, x, y, w, h, paras, font=BODY, size=20, color="ink", bold=False, italic=False,
         align="l", anchor="t", spacing=None, char=None, name=None, margin=0, autofit=False, para_after=None,
         hang=None):
    """paras: str | list of paragraphs; a paragraph is str or list of runs;
    a run is str or dict(t=..., font, size, color, bold, italic, char)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT, "j": PP_ALIGN.JUSTIFY}[align]
        if spacing:
            p.line_spacing = spacing
        if para_after is not None:
            p.space_after = Pt(para_after)
        if hang:  # hanging indent (inches): wrapped lines align under the text, not the bullet
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(Inches(hang)))); pPr.set("indent", str(-int(Inches(hang))))
        runs = para if isinstance(para, list) else [para]
        for run in runs:
            if isinstance(run, str):
                run = {"t": run}
            if run.get("size", size) <= 24:  # keep Vietnamese compounds on one line
                run = dict(run, t=bind_compounds(run["t"]))
            parts = run["t"].split("\n")
            for j, part in enumerate(parts):
                if j:
                    p.add_line_break()
                    br = p._p.findall(qn("a:br"))[-1]
                    brPr = etree.SubElement(br, qn("a:rPr"))
                    brPr.set("sz", str(int(run.get("size", size) * 100)))
                for seg in _ARROWS.split(part):  # Be Vietnam Pro / Phudu have no arrow glyphs: draw them in Segoe UI
                    if seg:
                        _fmt_run(p.add_run(), dict(run, t=seg, font=ARROW_FONT) if _ARROWS.fullmatch(seg) else dict(run, t=seg),
                                 font, size, bold, italic, color, char)
    if name:
        tb.name = name
    return tb


ARROW_FONT = "Segoe UI"
_ARROWS = re.compile("([←-⇿]+)")


def _fmt_run(r, run, font, size, bold, italic, color, char):
    r.text = run["t"]
    f = r.font
    name, sz = run.get("font", font), run.get("size", size)
    b, it = run.get("bold", bold), run.get("italic", italic)
    if name in (DISPLAY, DISPLAY_HEAVY, DISPLAY_BLACK):
        if it:                      # no italic in Phudu -> real italic from the body family
            name, sz = BODY, sz * ITALIC_SCALE
        elif b and name == DISPLAY:  # bold headline -> the ExtraBold cut (no synthetic bold)
            name, b = DISPLAY_HEAVY, False
        elif name != DISPLAY:
            b = False
        if not it and sz >= 20:
            sz = sz * DISPLAY_SCALE
    elif name.startswith("Be Vietnam Pro"):
        sz = sz * BODY_SCALE
    f.name = name
    f.size = Pt(round(sz * 2) / 2)
    f.bold = b
    f.italic = it
    col = run.get("color", color)
    f.color.rgb = rgb(C.get(col, col))
    ch = run.get("char", char)
    rPr = r._r.get_or_add_rPr()
    if ch is not None:
        rPr.set("spc", str(int(ch * 100)))
    # make East-Asian / complex script fall back to same face (avoids odd glyph swaps)
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = etree.SubElement(rPr, qn(tag))
        el.set("typeface", name)


def pill(slide, x, y, label, fill, color, size=11, line=None, h=0.34, pad=0.16, char=1.5, font=BODY, bold=True, name=None, w=None):
    """Small rounded label; width estimated from text length."""
    est = w or (len(label) * (size * 0.0102 + char * 0.0139) + pad * 2)
    s = rect(slide, x, y, est, h, fill=fill, line=line, line_w=1.25, radius=50000, name=name)
    tf = s.text_frame
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = rgb(C.get(color, color))
    r._r.get_or_add_rPr().set("spc", str(int(char * 100)))
    return s


TAGS = {
    "A": ("LÝ LUẬN CỐT LÕI", "gold2", "burg", None),
    "B": ("DIỄN GIẢI CỦA NHÓM", None, None, None),  # outline; colours depend on bg
    "C": ("VẬN DỤNG ĐƯƠNG ĐẠI", "warm", "white", None),
}


def content_tags(slide, kinds, dark, x_right=W - 0.45, y=0.38, stack=False):
    """Content-type tags, right-aligned at the top. kinds e.g. ["A", "B"]. stack=True puts them in a column."""
    xs = x_right
    shapes = []
    for k in (kinds if stack else reversed(kinds)):
        if stack:
            xs = x_right
        label, fill, col, _ = TAGS[k]
        size = 10
        w = len(label) * 0.112 + 0.34
        xs -= w
        if k == "B":
            col = "ivory" if dark else "burg"
            s = pill(slide, xs, y, label, None, col, size=size, line=C["ivory"] if dark else C["burg"], w=w, name=f"Tag {label}")
        else:
            s = pill(slide, xs, y, label, fill, col, size=size, w=w, name=f"Tag {label}")
        shapes.append(s)
        xs -= 0.12
        if stack:
            y += 0.44
    return shapes


def folio(slide, n, total, dark, x=0.6, y=7.0, label="ĐẠI ĐOÀN KẾT DÂN TỘC"):
    col = "cream" if dark else "muted"
    return text(slide, x, y, 4.5, 0.3, [[{"t": f"{n:02d}", "bold": True, "color": "gold2" if dark else "red"},
                                        {"t": f"  /  {total:02d}    {label}"}]],
                size=10, color=col, char=1.2, name="Folio")


def source_note(slide, txt, dark, x=None, y=6.98, w=7.6, align="r"):
    x = (W - 0.5 - w) if x is None else x
    return text(slide, x, y, w, 0.34, txt, size=10, color="cream" if dark else "muted", align=align, italic=True, name="Source")


# ------------------------------------------------------------------ notes / transitions / animation
def notes(slide, txt):
    slide.notes_slide.notes_text_frame.text = txt


def _insert_after_csld(slide, el):
    sld = slide._element
    # order: cSld, clrMapOvr, transition, timing, extLst
    anchor = sld.find(qn("p:clrMapOvr"))
    if anchor is None:
        anchor = sld.find(qn("p:cSld"))
    existing_tr = sld.find(qn("p:transition"))
    if el.tag == qn("p:timing") and existing_tr is not None:
        anchor = existing_tr
    anchor.addnext(el)


def transition_fade(slide, speed="med"):
    tr = etree.Element(qn("p:transition"))
    tr.set("spd", speed)
    etree.SubElement(tr, qn("p:fade"))
    _insert_after_csld(slide, tr)


def fade_sequence(slide, clicks, dur=600):
    """clicks: list of lists of shapes; each inner list fades in together on one click.
    Exported PNG/PDF show the final state (all visible)."""
    ids = iter(range(3, 10000))
    root = etree.Element(qn("p:timing"))
    tnLst = etree.SubElement(root, qn("p:tnLst"))
    par = etree.SubElement(tnLst, qn("p:par"))
    ctn_root = etree.SubElement(par, qn("p:cTn"), id="1", dur="indefinite", restart="never", nodeType="tmRoot")
    ch_root = etree.SubElement(ctn_root, qn("p:childTnLst"))
    seq = etree.SubElement(ch_root, qn("p:seq"), concurrent="1", nextAc="seek")
    ctn_main = etree.SubElement(seq, qn("p:cTn"), id="2", dur="indefinite", nodeType="mainSeq")
    ch_main = etree.SubElement(ctn_main, qn("p:childTnLst"))
    bld_ids = []
    for group in clicks:
        p_click = etree.SubElement(ch_main, qn("p:par"))
        c_click = etree.SubElement(p_click, qn("p:cTn"), id=str(next(ids)), fill="hold")
        st = etree.SubElement(c_click, qn("p:stCondLst"))
        etree.SubElement(st, qn("p:cond"), delay="indefinite")
        ch_click = etree.SubElement(c_click, qn("p:childTnLst"))
        p_inner = etree.SubElement(ch_click, qn("p:par"))
        c_inner = etree.SubElement(p_inner, qn("p:cTn"), id=str(next(ids)), fill="hold")
        st2 = etree.SubElement(c_inner, qn("p:stCondLst"))
        etree.SubElement(st2, qn("p:cond"), delay="0")
        ch_inner = etree.SubElement(c_inner, qn("p:childTnLst"))
        for i, shp in enumerate(group):
            spid = str(shp.shape_id)
            p_eff = etree.SubElement(ch_inner, qn("p:par"))
            c_eff = etree.SubElement(p_eff, qn("p:cTn"), id=str(next(ids)), presetID="10", presetClass="entr",
                                     presetSubtype="0", fill="hold", grpId="0",
                                     nodeType="clickEffect" if i == 0 else "withEffect")
            st3 = etree.SubElement(c_eff, qn("p:stCondLst"))
            etree.SubElement(st3, qn("p:cond"), delay="0")
            ch_eff = etree.SubElement(c_eff, qn("p:childTnLst"))
            sset = etree.SubElement(ch_eff, qn("p:set"))
            cb = etree.SubElement(sset, qn("p:cBhvr"))
            c_set = etree.SubElement(cb, qn("p:cTn"), id=str(next(ids)), dur="1", fill="hold")
            st4 = etree.SubElement(c_set, qn("p:stCondLst"))
            etree.SubElement(st4, qn("p:cond"), delay="0")
            tgt = etree.SubElement(cb, qn("p:tgtEl"))
            etree.SubElement(tgt, qn("p:spTgt"), spid=spid)
            anl = etree.SubElement(cb, qn("p:attrNameLst"))
            an = etree.SubElement(anl, qn("p:attrName"))
            an.text = "style.visibility"
            to = etree.SubElement(sset, qn("p:to"))
            etree.SubElement(to, qn("p:strVal"), val="visible")
            ae = etree.SubElement(ch_eff, qn("p:animEffect"), transition="in", filter="fade")
            cb2 = etree.SubElement(ae, qn("p:cBhvr"))
            etree.SubElement(cb2, qn("p:cTn"), id=str(next(ids)), dur=str(dur))
            tgt2 = etree.SubElement(cb2, qn("p:tgtEl"))
            etree.SubElement(tgt2, qn("p:spTgt"), spid=spid)
            if shp._element.tag == qn("p:sp"):
                bld_ids.append(spid)
    prev = etree.SubElement(seq, qn("p:prevCondLst"))
    pc = etree.SubElement(prev, qn("p:cond"), evt="onPrev", delay="0")
    etree.SubElement(etree.SubElement(pc, qn("p:tgtEl")), qn("p:sldTgt"))
    nxt = etree.SubElement(seq, qn("p:nextCondLst"))
    nc = etree.SubElement(nxt, qn("p:cond"), evt="onNext", delay="0")
    etree.SubElement(etree.SubElement(nc, qn("p:tgtEl")), qn("p:sldTgt"))
    if bld_ids:
        bl = etree.SubElement(root, qn("p:bldLst"))
        for sid in bld_ids:
            etree.SubElement(bl, qn("p:bldP"), spid=sid, grpId="0", animBg="1")
    _insert_after_csld(slide, root)


def group(slide, shapes, name=None):
    """Group existing shapes (keeps z-order position of the first)."""
    grp = slide.shapes.add_group_shape(shapes)
    if name:
        grp.name = name
    return grp
