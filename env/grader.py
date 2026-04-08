def grade(env):
    total = len(env.emails)
    handled = sum(1 for e in env.emails if e.handled)
    return min(max(handled / total, 0.0), 1.0)