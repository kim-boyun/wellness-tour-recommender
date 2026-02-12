"""
설문 문항 정의 및 클러스터 메타데이터.
UI/로직과 분리해 데이터만 관리합니다.
"""

# 7개 문항 정의 (관광객 유형 분류용)
QUESTIONS = {
    "q1": {
        "title": "1. 한국에 머무를 계획 기간은 얼마나 되나요?",
        "category": "체류 기간",
        "options": [
            "1~6일 (단기 관광)",
            "7~10일 (일반적인 여행)",
            "11~20일 (중장기 여행)",
            "21일 이상 (장기 체류)"
        ],
        "weights": {
            0: {"cluster_0": 0, "cluster_1": 1, "cluster_2": 2},
            1: {"cluster_0": 0, "cluster_1": 2, "cluster_2": 0},
            2: {"cluster_0": 1, "cluster_1": 1, "cluster_2": 0},
            3: {"cluster_0": 3, "cluster_1": 0, "cluster_2": 0}
        }
    },
    "q2": {
        "title": "2. 1인 1일 예상 지출액은 어느 정도인가요? (USD 기준)",
        "category": "지출 수준",
        "options": [
            "$0~150 (저예산형)",
            "$151~350 (중간 예산형)",
            "$351~700 (고예산형)",
            "$701 이상 (프리미엄형)"
        ],
        "weights": {
            0: {"cluster_0": 3, "cluster_1": 0, "cluster_2": 0},
            1: {"cluster_0": 0, "cluster_1": 2, "cluster_2": 0},
            2: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 1},
            3: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 3}
        }
    },
    "q3": {
        "title": "3. 한국 방문은 몇 번째인가요?",
        "category": "방문 경험",
        "options": [
            "처음 방문",
            "2~3번째 방문",
            "4~5번째 방문",
            "6번째 이상 방문"
        ],
        "weights": {
            0: {"cluster_0": 0, "cluster_1": 2, "cluster_2": 0},
            1: {"cluster_0": 1, "cluster_1": 2, "cluster_2": 0},
            2: {"cluster_0": 1, "cluster_1": 0, "cluster_2": 1},
            3: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 3}
        }
    },
    "q4": {
        "title": "4. 주된 숙박 형태는 무엇에 가장 가깝나요?",
        "category": "숙박 유형",
        "options": [
            "친척이나 친구 집",
            "호텔이나 리조트",
            "게스트하우스나 호스텔",
            "에어비앤비나 콘도미니엄"
        ],
        "weights": {
            0: {"cluster_0": 3, "cluster_1": 0, "cluster_2": 0},
            1: {"cluster_0": 0, "cluster_1": 2, "cluster_2": 1},
            2: {"cluster_0": 1, "cluster_1": 1, "cluster_2": 0},
            3: {"cluster_0": 0, "cluster_1": 1, "cluster_2": 1}
        }
    },
    "q5": {
        "title": "5. 전통문화 체험(한복 입기, 전통 음식 만들기 등)에 대한 관심도는?",
        "category": "문화 체험",
        "options": [
            "매우 높다 - 꼭 체험하고 싶다",
            "어느 정도 있다 - 기회가 되면 해보고 싶다",
            "잘 모르겠다 - 상황에 따라",
            "관심이 낮다 - 별로 중요하지 않다"
        ],
        "weights": {
            0: {"cluster_0": 1, "cluster_1": 2, "cluster_2": 0},
            1: {"cluster_0": 1, "cluster_1": 1, "cluster_2": 0},
            2: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 0},
            3: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 1}
        }
    },
    "q6": {
        "title": "6. 박물관이나 전시관 관람에 대한 의향은?",
        "category": "문화 관람",
        "options": [
            "매우 높다 - 여러 곳을 방문하고 싶다",
            "어느 정도 있다 - 1-2곳 정도는 가보고 싶다",
            "잘 모르겠다 - 시간이 남으면",
            "관심이 낮다 - 굳이 가지 않아도 된다"
        ],
        "weights": {
            0: {"cluster_0": 1, "cluster_1": 2, "cluster_2": 0},
            1: {"cluster_0": 1, "cluster_1": 1, "cluster_2": 0},
            2: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 0},
            3: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 1}
        }
    },
    "q7": {
        "title": "7. 아래 중 가장 본인의 여행 스타일에 가까운 것은?",
        "category": "여행 스타일",
        "options": [
            "오래 머물며 여유있게 지인도 만나고 문화도 천천히 즐긴다",
            "평균적인 일정으로 주요 명소와 체험을 균형있게 본다",
            "짧게 강하게! 쇼핑·미식 등 소비 중심으로 효율적으로 즐긴다"
        ],
        "weights": {
            0: {"cluster_0": 3, "cluster_1": 0, "cluster_2": 0},
            1: {"cluster_0": 0, "cluster_1": 3, "cluster_2": 0},
            2: {"cluster_0": 0, "cluster_1": 0, "cluster_2": 3}
        }
    }
}


def get_cluster_info():
    """3개 클러스터(관광객 유형) 메타데이터."""
    return {
        0: {
            "name": "경제적 웰니스 관광객",
            "english_name": "Economic Wellness Tourist",
            "description": "한국에 오래 머물며, 저예산으로 문화를 천천히 체험하는 유형입니다.",
            "characteristics": ["장기 체류", "지인 방문", "저예산", "문화 체험"],
            "color": "#3498DB",
            "percentage": 10.9,
            "count": 282,
            "key_factors": {
                "체류기간": "21일 이상",
                "지출수준": "저예산형",
                "방문경험": "재방문자",
                "숙박형태": "지인집"
            }
        },
        1: {
            "name": "일반 웰니스 관광객",
            "english_name": "General Wellness Tourist",
            "description": "일반적인 관광 일정과 예산으로 한국의 주요 명소와 문화를 균형있게 체험하는 대표적인 관광객 유형입니다.",
            "characteristics": ["표준 일정", "균형 예산", "문화 관심", "호텔 선호"],
            "color": "#2ECC71",
            "percentage": 81.0,
            "count": 2099,
            "key_factors": {
                "체류기간": "7-10일",
                "지출수준": "중간 예산형",
                "방문경험": "처음 또는 재방문",
                "숙박형태": "호텔/리조트"
            }
        },
        2: {
            "name": "프리미엄 웰니스 관광객",
            "english_name": "Premium Wellness Tourist",
            "description": "짧은 기간 동안 고예산으로 쇼핑, 미식 등을 집중적으로 즐기는 경험 많은 재방문 고객입니다.",
            "characteristics": ["단기 집중", "고예산", "쇼핑 중심", "효율 추구"],
            "color": "#E37745",
            "percentage": 8.1,
            "count": 210,
            "key_factors": {
                "체류기간": "1-6일",
                "지출수준": "고예산형",
                "방문경험": "다수 재방문",
                "숙박형태": "프리미엄 숙소"
            }
        }
    }
