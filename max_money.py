start_block_reward = 50
reward_interval = 210000


def max_money():
    current_reward = 50 * 10**8
    total = 0

    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2

    return total


if __name__ == "__main__":
    total = max_money()

    print(f"Total BTC to ever be created is {total} Satoshis.")
