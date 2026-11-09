#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVA-01 Masterpiece Theme Processor for GitHub Profile 3D Contrib.
Applies NERV Tactical Red, EVA-01 Berserk Neon Green, and A.T. Field Amber Orange.
"""

import colorsys
import os
import re
import sys

def main():
    src_path = "profile-3d-contrib/profile-night-green.svg"
    dest_path = "profile-3d-contrib/profile-eva-01.svg"

    if not os.path.exists(src_path):
        print(f"Error: Source file '{src_path}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(src_path, "r", encoding="utf-8") as f:
        svg = f.read()

    # ==========================================
    # 1. 提交數字：精準鎖定 NERV 警戒紅 (#FF1E27)
    # ==========================================
    pos = svg.lower().find("contributions")
    if pos != -1:
        start_pos = max(0, pos - 400)
        prefix = svg[start_pos:pos]
        
        pattern = r'(<(?:text|tspan)\b[^>]*>)(\s*\d+\s*)(</(?:text|tspan)>)'
        matches = list(re.finditer(pattern, prefix, flags=re.IGNORECASE))
        if matches:
            last_m = matches[-1]
            open_tag, num_str, close_tag = last_m.groups()
            if 'fill=' in open_tag:
                open_tag = re.sub(r'fill=["\'][^"\']+["\']', 'fill="#FF1E27"', open_tag)
            else:
                open_tag = open_tag[:-1] + ' fill="#FF1E27" font-weight="bold">'
            new_tag = f"{open_tag}{num_str}{close_tag}"
            prefix = prefix[:last_m.start()] + new_tag + prefix[last_m.end():]
            svg = svg[:start_pos] + prefix + svg[pos:]

    svg = re.sub(
        r'(>\s*)(\d+)(\s*contributions\s*<)',
        r'\1<tspan fill="#FF1E27" font-weight="bold">\2</tspan> contributions<',
        svg,
        count=1,
        flags=re.IGNORECASE
    )

    # ==========================================
    # 2. 語言圓形圖：EVA 全機體代表色矩陣
    # ==========================================
    pie_colors = {
        "#f1e05a": "#F29600",  # 零號機 綾波麗橘黃 (EV-05)
        "#3572A5": "#19325C",  # Mark.06 渚薰深藍
        "#e34c26": "#D9001B",  # 二號機 明日香裝甲紅
        "#3178c6": "#E85298",  # 八號機 真希波特裝粉
        "#563d7c": "#8A3FFC",  # 初號機 高光亮紫
        "#89e051": "#39FF14",  # 初號機 螢光綠 (EV-04)
    }
    for old_c, new_c in pie_colors.items():
        svg = re.sub(re.escape(old_c), new_c, svg, flags=re.IGNORECASE)

    # ==========================================
    # 3. 核心 3D 柱體與底座：HLS 運算＋快取回寫
    # ==========================================
    color_cache = {}

    def process_3d_color(r_val, g_val, b_val):
        key = (r_val, g_val, b_val)
        if key in color_cache:
            return color_cache[key]

        r, g, b = r_val / 255.0, g_val / 255.0, b_val / 255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)

        # A. 背景大底座 -> 使徒純黑
        if l < 0.16 and s < 0.25:
            result = "#000000"
        # B. 跑道地盤與底座格線 -> 螢光綠導引軌道
        elif 0.16 <= l < 0.40 and s < 0.28:
            result = "#15441E"
        elif 0.40 <= l < 0.55 and s < 0.28:
            result = "#39FF14"
        # C. 標籤文字 -> 使徒純白
        elif s < 0.15 and l >= 0.55:
            result = "#FFFFFF"
        # D. 3D 柱體分色
        elif (g_val > r_val) and (g_val > b_val) and s > 0.15:
            if (g_val >= 135 and l >= 0.46) or (r_val >= 70 and l >= 0.44):
                result = "#39FF14"  # 頂面：暴走螢光青綠
            else:
                if l >= 0.30:
                    result = "#7B2CBF"  # 側面受光亮紫
                elif l >= 0.20:
                    result = "#5A189A"  # 側面中調紫
                else:
                    result = "#3C096C"  # 側面背光暗紫
        else:
            result = None

        color_cache[key] = result
        return result

    protected = {
        c.strip().upper() for c in list(pie_colors.values()) + [
            "#FF1E27", "#39FF14", "#00FF66", "#FFFFFF", "#000000",
            "#15441E", "#28C70E", "#1A8A08", "#7B2CBF", "#5A189A", "#3C096C",
            "#FF7900", "#FFA500", "#FF4500"
        ]
    }

    def hex_cleaner(m):
        c = m.group(0).upper()
        if c in protected:
            return m.group(0)
        r, g, b = int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
        new_c = process_3d_color(r, g, b)
        return new_c if new_c else m.group(0)

    def rgb_cleaner(m):
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        new_c = process_3d_color(r, g, b)
        return new_c if new_c else m.group(0)

    svg = re.sub(r'#[0-9a-fA-F]{6}', hex_cleaner, svg)
    svg = re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', rgb_cleaner, svg)

    # =========================================================================
    # 4. 右上角能力雷達圖：A.T. Field 琥珀橙相位網格 × 初號機暴走青綠力場侵蝕
    # =========================================================================
    def replace_radar_polygon(match):
        tag = match.group(0)
        
        # A. 外層同心多邊形網格：A.T. Field 經典琥珀橙相位環
        if 'fill="none"' in tag or "fill:none" in tag or "fill='none'" in tag:
            tag = re.sub(r'stroke=["\'][^"\']+["\']', 'stroke="#FF7900"', tag)
            tag = re.sub(r'stroke:\s*[^;"]+', 'stroke:#FF7900', tag)
            if 'stroke-opacity=' in tag:
                tag = re.sub(r'stroke-opacity=["\'][^"\']+["\']', 'stroke-opacity="0.75"', tag)
            else:
                tag = tag[:-1] + ' stroke-opacity="0.75">'
            return tag

        # B. 核心數據多邊形：初號機暴走螢光青綠
        tag = re.sub(r'fill=["\'][^"\']+["\']', 'fill="#39FF14"', tag)
        tag = re.sub(r'stroke=["\'][^"\']+["\']', 'stroke="#00FF66"', tag)
        tag = re.sub(r'fill:\s*[^;"]+', 'fill:#39FF14', tag)
        tag = re.sub(r'stroke:\s*[^;"]+', 'stroke:#00FF66', tag)
        
        if 'fill-opacity=' in tag:
            tag = re.sub(r'fill-opacity=["\'][^"\']+["\']', 'fill-opacity="0.45"', tag)
        else:
            tag = tag[:-1] + ' fill-opacity="0.45">'

        if 'stroke-width=' in tag:
            tag = re.sub(r'stroke-width=["\'][^"\']+["\']', 'stroke-width="2"', tag)
        else:
            tag = tag[:-1] + ' stroke-width="2">'
            
        return tag

    svg = re.sub(r'<polygon\b[^>]+>', replace_radar_polygon, svg, flags=re.IGNORECASE)

    # C. 雷達圖五軸放射線：A.T. Field 能量軸線
    def replace_radar_line(match):
        tag = match.group(0)
        tag = re.sub(r'stroke=["\'][^"\']+["\']', 'stroke="#FFA500"', tag)
        tag = re.sub(r'stroke:\s*[^;"]+', 'stroke:#FFA500', tag)
        if 'stroke-opacity=' in tag:
            tag = re.sub(r'stroke-opacity=["\'][^"\']+["\']', 'stroke-opacity="0.55"', tag)
        else:
            tag = tag[:-1] + ' stroke-opacity="0.55">'
        return tag

    svg = re.sub(r'<line\b[^>]+>', replace_radar_line, svg, flags=re.IGNORECASE)

    # ==========================================
    # 5. 輸出前結構完整性檢查
    # ==========================================
    if not svg.strip().endswith("</svg>"):
        print("Warning: Generated SVG does not properly close with </svg>", file=sys.stderr)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print("Successfully rendered EVA-01 Masterpiece with A.T. Field!")

if __name__ == "__main__":
    main()
