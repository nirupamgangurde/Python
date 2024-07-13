from plyer import notification
import random

randomno = []
randomno.append(random.randint(1,6))
print(randomno)

notification.notify(
    title="Random Number",
    message=f"Random Number is {randomno}"
)