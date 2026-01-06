# This module is based on the rubpy library.
# Used and modified with permission from the original author.
# Original source: https://github.com/shayanheidari01/rubika

import re
import markdownify

from rubxy import enums

from typing import List, Dict, Any


def _utf16_offsets(text: str) -> List[int]:
    acc = 0
    offsets = [0]
    for ch in text:
        acc += 2 if ord(ch) > 0xFFFF else 1
        offsets.append(acc)
    return offsets


ENTITY_MAP = {
    ">": ("Quote", None),
    "```": ("Pre", 1),
    "**": ("Bold", 2),
    "`": ("Mono", 3),
    "__": ("Italic", 4),
    "--": ("Underline", 5),
    "~~": ("Strike", 6),
    "||": ("Spoiler", 7),
    "[": ("Link", 8),
}

MENTION_KIND = {"u": "User", "g": "Group", "c": "Channel", "b": "Bot"}

PATTERN = re.compile(
    r"(?:^(?:> ?[^\n]*\n?)+)|```([\s\S]*?)```|\*\*([^\n*]+?)\*\*|`([^\n`]+?)`|__([^\n_]+?)__|--([^\n-]+?)--|~~([^\n~]+?)~~|\|\|([^\n|]+?)\|\||\[([^\]]+?)\]\((\S+)\)",
    re.MULTILINE | re.DOTALL,
)


class Markdown:
    def __init__(self, parse_mode: enums.ParseMode):
        self.parse_mode = parse_mode
    
    def parser(self, text: str):
        if self.parse_mode is enums.ParseMode.HTML:
            text = markdownify.markdownify(text)
        
        return self.parse(text)

    def parse(self, text: str) -> Dict[str, Any]:
        entities: List[Dict[str, Any]] = []
        visible_text = text
        removed_utf16 = 0
        removed_chars = 0
        utf16_map = _utf16_offsets(text)

        for match in PATTERN.finditer(text):
            token = match.group(0)
            start, end = match.span()

            start_utf16 = utf16_map[start] - removed_utf16
            start_char = start - removed_chars

            for prefix, (kind, group_id) in ENTITY_MAP.items():
                if not token.startswith(prefix):
                    continue

                if kind == "Quote":
                    lines = [l.lstrip("> ").lstrip(">") for l in token.splitlines()]
                    content = "\n".join(lines)
                else:
                    gs = match.start(group_id)
                    ge = match.end(group_id)
                    content = match.group(group_id) if gs != -1 else ""

                inner = self.parse(content) if kind not in ("Pre", "Link") else {"text": content}
                clean = inner["text"]

                length = len(clean.encode("utf-16-be")) // 2

                entity = {
                    "type": kind,
                    "from_index": start_utf16,
                    "length": length,
                }

                if kind == "Pre":
                    lang = clean.split("\n", 1)[0].strip()
                    if lang:
                        entity["language"] = lang

                if kind == "Link":
                    url = match.group(9)
                    prefix_type = MENTION_KIND.get(url[0])

                    if prefix_type:
                        entity["type"] = "MentionText"
                        entity["mention_text_object_type"] = prefix_type
                        entity["mention_text_object_guid"] = url
                        entity["mention_text_user_id"] = url
                    else:
                        entity["link_url"] = url
                        entity["link"] = {
                            "type": "hyperlink",
                            "hyperlink_data": {"url": url},
                        }

                entities.append(entity)

                if inner.get("metadata"):
                    for sub in inner["metadata"]["meta_data_parts"]:
                        sub["from_index"] += start_utf16
                        entities.append(sub)

                utf16_removed = utf16_map[end] - utf16_map[start] - length
                char_removed = (end - start) - len(clean)

                visible_text = (
                    visible_text[:start_char]
                    + clean
                    + visible_text[end - removed_chars :]
                )

                removed_utf16 += utf16_removed
                removed_chars += char_removed
                break

        return {
            "text": visible_text.strip(),
            "metadata": {
                "meta_data_parts": entities
            } if entities else None
        }