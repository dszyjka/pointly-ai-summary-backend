from enum import Enum


class ResponseType(str, Enum):
    bullet_points = 'Bullet Points'
    paragraph = 'Paragraph'
    tldr = 'TL;DR'
    qa = 'Q&A'
    executive = 'Executive Summary'
    key_metrics = 'Key Metrics'
    action_items = 'Action Items'
    explanation = 'Explanation'
    business = 'Business Report'