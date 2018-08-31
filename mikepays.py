# Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:
#
# If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
# Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
# How much is Michael going to pay? Calculate the amount with two decimals, if necessary.

def michael_pays(costs):
    if costs < 5:
        return round(costs, 2)
    if costs <= 30:
        return round(costs * 0.66666666666, 2)
    if costs > 30:
        return round(costs - 10, 2)

print michael_pays(5)
print michael_pays(22)
print michael_pays(80)
