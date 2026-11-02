def baho_aniqla(ball):
    if 90 <= ball <= 100:
        return "A'lo"
    elif 70 <= ball <= 89:
        return "Yaxshi"
    elif 50 <= ball <= 69:
        return "Qoniqarli"
    else:
        return "Qoniqarsiz"

def ortacha_hisobla(ballar):
    return sum(ballar) / len(ballar) if ballar else 0

def eng_yaxshi_ball(ballar):
    return max(ballar) if ballar else 0