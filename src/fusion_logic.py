def fusion(emotion, pose, action, audio):
    if action == "Fight" or audio in ["Gunshot","Scream"]:
        return "HIGH THREAT"
    elif pose == "Fall" and emotion in ["Fear","Distress"]:
        return "MEDIUM THREAT"
    elif action == "Loitering":
        return "LOW THREAT"
    else:
        return "SAFE"
