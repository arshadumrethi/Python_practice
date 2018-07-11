Talks
    if costs < 5:
        return round(costs, 2)
    if costs <= 30:
        return round(costs * 0.66666666666, 2)
    if costs > 30:
        return round(costs - 10, 2)

print michael_pays(5)
print michael_pays(22)
print michael_pays(80)
