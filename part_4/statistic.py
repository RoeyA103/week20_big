import re
from collections import Counter


class Statistic:

    def __init__(self, logger, hostile_list: list, semi_hostile_list: list):
        self.logger = logger
        self.hostile_list = [w.lower() for w in hostile_list]
        self.semi_hostile_list = [w.lower() for w in semi_hostile_list]

        self.logger.info("Statistic created")

    def normalize(self, text: str):
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return text

    def get_bds_threat_level(self,bds_percent)->str:
        if bds_percent >=7:
            return "high"
        if bds_percent < 3:
            return "none"
        return "medium"

    def calculate_hate_percent(self, text: str)->dict:

        clean_text = self.normalize(text)

        words = clean_text.split()
        total_words = len(words)

        if total_words == 0:
            return {"hate_percent": 0}

        counter = Counter(words)

        hostile_count = 0
        semi_count = 0


        for word in self.hostile_list:
            if " " not in word:
                hostile_count += counter[word]

        for word in self.semi_hostile_list:
            if " " not in word:
                semi_count += counter[word]


        for phrase in self.hostile_list:
            if " " in phrase:
                hostile_count += clean_text.count(phrase)

        for phrase in self.semi_hostile_list:
            if " " in phrase:
                semi_count += clean_text.count(phrase)


        score = hostile_count + (semi_count * 0.5)

        bds_percent = (score / total_words) * 100

        self.logger.debug("Statistic - text statistics calculate successfuly")

        return {
            "bds_percent": round(bds_percent, 2),
            "is_bds": bds_percent >= 7,
            "bds_threat_level": self.get_bds_threat_level(bds_percent)
        }