from .models import Email

TASKS = {
    "easy": {
        "emails": [
            Email(id="1", subject="Server Down", content="Server not working", true_priority="high"),
            Email(id="2", subject="Lunch", content="Pizza today", true_priority="low"),
            Email(id="3", subject="Invoice", content="Pay invoice", true_priority="medium"),
        ],
        "time_remaining": 10
    },
    "medium": {
        "emails": [
            Email(id=str(i), subject=f"Email {i}", content="important", true_priority="high" if i%2==0 else "low")
            for i in range(1,7)
        ],
        "time_remaining": 20
    },
    "hard": {
        "emails": [
            Email(id=str(i), subject=f"Task {i}", content="urgent", true_priority="high" if i%3==0 else "medium")
            for i in range(1,11)
        ],
        "time_remaining": 30
    }
}